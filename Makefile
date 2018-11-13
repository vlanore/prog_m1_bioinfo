.PHONY: launch
launch:
	if pgrep node; then kill `pgrep node`; fi
	reveal-md slides.md --highlight-theme tomorrow --disable-auto-open > reveal.output &

.PHONY: open
open:
	if pgrep node; then kill `pgrep node`; fi
	reveal-md slides.md --highlight-theme tomorrow > reveal.output &