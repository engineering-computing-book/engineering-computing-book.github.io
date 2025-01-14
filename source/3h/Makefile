.PHONY: solution

solution: solution.md
	
%.txt: %.py
	python $< > $@

%.md: %.py
	publish $< md
	
%.docx: %.py
	publish $< docx
	