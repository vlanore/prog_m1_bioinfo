import read_fasta, matplotlib.pyplot, sys

f = read_fasta.read_fasta("data/example.fasta")

rr = []
for s in f:
    r = []
    for l in s[1]:
        le = False
        il = 0
        for i in range(len(r)):
            if r[i][0] == l:
                le = True
                il = i
                break
        if not le:
            r.append((l, 1))
        else:
            r[i] = (l, r[i][1] + 1)
    r = sorted(r)
    t = 0
    for e in r:
        t += e[1]
    ls = []
    c = []
    for e in r:
        ls.append(e[0])
        c.append(e[1])

    print(r)
    print(t)
    print(ls)
    rr.append((s[0], ls, c))

matplotlib.pyplot.bar(rr[0][1], rr[0][2])
matplotlib.pyplot.bar(rr[0][1], rr[1][2], bottom=rr[0][2])
matplotlib.pyplot.show()