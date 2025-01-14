.PHONY: main

main: main.md
	
%.txt: %.py
	python $< > $@

%.md: %.py
	publish $< md
	
%.docx: %.py
	publish $< docx
	