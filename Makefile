.PHONY: test
test: index.html
	cp index.html ../reveal.js
	firefox localhost:8000