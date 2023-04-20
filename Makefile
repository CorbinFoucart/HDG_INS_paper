# toggle between elsarticle_main and arxiv_main to build each version
#DOCNAME=arxiv_main
DOCNAME=main

all: report

.PHONY: clean

report:
	pdflatex $(DOCNAME).tex
	bibtex $(DOCNAME).aux
	pdflatex $(DOCNAME).tex
	pdflatex $(DOCNAME).tex

view: report
	open $(DOCNAME).pdf

clean:
	rm *.blg *.bbl *.aux *.log *.out *.spl
