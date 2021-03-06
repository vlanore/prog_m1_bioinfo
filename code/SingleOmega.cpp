#include <cmath>
#include "components/ChainCheckpoint.hpp"
#include "components/ChainDriver.hpp"
#include "components/ConsoleLogger.hpp"
#include "components/InferenceAppArgParse.hpp"
#include "components/MoveScheduler.hpp"
#include "components/StandardTracer.hpp"
#include "components/restart_check.hpp"
#include "data_preparation.hpp"
#include "lib/CodonSubMatrix.hpp"
#include "lib/CodonSuffStat.hpp"
#include "lib/PoissonSuffStat.hpp"
#include "submodels/branch_array.hpp"
#include "submodels/global_omega.hpp"
#include "submodels/nuc_rates.hpp"
#include "submodels/submodel_external_interface.hpp"

using namespace std;

class LegacyArrayProxy : public BranchSelector<double> 
{
    std::vector<double> &data_ref;
    const Tree &tree_ref;

  public:
    LegacyArrayProxy(std::vector<double> &data_ref, const Tree &tree_ref)
        : data_ref(data_ref), tree_ref(tree_ref) 
        {}

    virtual const Tree &GetTree() const override 
    { return tree_ref; }
    virtual const double &GetVal(int index) const override    
    {
        return data_ref[index];
    }
};

TOKEN(global_omega)
TOKEN(branch_lengths)
TOKEN(nuc_rates)
TOKEN(codon_statespace)
TOKEN(codon_submatrix)
TOKEN(branch_adapter)
TOKEN(phyloprocess)
TOKEN(bl_suffstats)
TOKEN(path_suffstats)
TOKEN(nucpath_suffstats)

template <class Gen>
auto make_globom(PreparedData &data, Gen &gen) 
{
    auto global_omega = globom::make_fixed(1.0, 1.0, gen);

    auto branch_lengths = make_branchlength_array(data.parser, 0.1, 1.0);

         auto nuc_rates = make_nucleotide_rate(normalize(
                                              {1, 1, 1, 1, 1, 1}),
        1. / 6,
        normalize(
            {1, 1, 1, 1}),
        1. / 4, gen);

         auto codon_statespace = dynamic_cast<const CodonStateSpace *>(data.alignment.GetStateSpace());

    auto codon_sub_matrix = std::make_unique<MGOmegaCodonSubMatrix>(
        codon_statespace, &get<nuc_matrix>(nuc_rates), get<omega, value>(global_omega));

         auto branch_adapter =
        std::make_unique<LegacyArrayProxy>(get<bl_array, value>(branch_lengths), *data.tree);
    auto phyloprocess = std::make_unique<PhyloProcess>(
                 data.tree.get(), &data.alignment, branch_adapter.get(), nullptr, codon_sub_matrix.get());
    phyloprocess->Unfold();

    // suff stats
    PoissonSuffStatBranchArray bl_suffstats
        {*data.tree};
    PathSuffStat path_suffstats;
    NucPathSuffStat nucpath_suffstats;

    return make_model(global_omega_ = move(global_omega), branch_lengths_ = move(branch_lengths),
        nuc_rates_ = move(nuc_rates), codon_statespace_ = codon_statespace,
              codon_submatrix_ = move(codon_sub_matrix), branch_adapter_ = move(branch_adapter),
        phyloprocess_ = move(phyloprocess), bl_suffstats_ = bl_suffstats,
                  path_suffstats_ = path_suffstats, nucpath_suffstats_ = nucpath_suffstats);
}

int main(int argc, char *argv[]) 
{
    // parsing command-line arguments
    ChainCmdLine cmd   
        {argc, argv, "SingleOmega", ' ', "0.1"};
    InferenceAppArgParse args(cmd);
    cmd.parse();

    // input data
    auto data = prepare_data(args.alignment.getValue(), args.treefile.getValue());

    // random generator
              auto gen = make_generator();
                    // model
                    auto model = make_globom(data, gen);
                    // move schedule
                    auto touch_matrices = [&model]()   
                    {
                        auto &nuc_matrix = get<nuc_rates, struct nuc_matrix>(model);
                        nuc_matrix.CopyStationary(get<nuc_rates, eq_freq, value>(model));
                        nuc_matrix.CorruptMatrix();
                        codon_submatrix_(model).SetOmega(get<global_omega, omega, value>(model));
                        codon_submatrix_(model).CorruptMatrix();
                    };

    auto scheduler = make_move_scheduler([&gen, &touch_matrices, &model]() 
    {
        // move phyloprocess
        touch_matrices();
        phyloprocess_(model).Move(1.0);

        // move omega
        for (int rep = 0; rep < 10; rep++)
                    {
                        // move omega
                        path_suffstats_(model).Clear();
                        path_suffstats_(model).AddSuffStat(phyloprocess_(model));
                        auto globom_logprob = [&model]()

                        
                        { return path_suffstats_(model).GetLogProb(codon_submatrix_(model)); };
                        globom::move(global_omega_(model), globom_logprob, gen);

            // move nuc rates
            touch_matrices();
            nucpath_suffstats_(model).Clear();
            nucpath_suffstats_(model).AddSuffStat(codon_submatrix_(model), path_suffstats_(model));

            auto nucrates_logprob = [&model]()
            {
                return nucpath_suffstats_(model).GetLogProb(
                    get<nuc_rates, nuc_matrix>(model), codon_statespace_(model));
            };
            move_exch_rates(nuc_rates_(model), 0.1, nucrates_logprob, gen);
            move_exch_rates(nuc_rates_(model), 0.03, nucrates_logprob, gen);
            move_exch_rates(nuc_rates_(model), 0.01, nucrates_logprob, gen);
                    move_eq_freqs(nuc_rates_(model), 0.1, nucrates_logprob, gen);
                    move_eq_freqs(nuc_rates_(model), 0.03, nucrates_logprob, gen);
                    touch_matrices();
                }
            });

            // initializing components
            ChainDriver chain_driver
        {cmd.chain_name(), args.every.getValue(), args.until.getValue()};

    ConsoleLogger console_logger;
    // ChainCheckpoint chain_checkpoint(cmd.chain_name() + ".param", chain_driver, model);
    StandardTracer trace(model, cmd.chain_name());

            // registering components to chain driver
            chain_driver.add(scheduler);
            chain_driver.add(console_logger);
            // chain_driver.add(chain_checkpoint);
            chain_driver.add(trace);

            // launching chain!
            chain_driver.go();
}
