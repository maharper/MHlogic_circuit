# project
PROJECT=MH20logic_circuit_1

# Python
PYTHON=py

# LaTeX
LATEX=latexmk

# convert
CONVERT=magick
CONVERT_INPUT_OPTIONS=-density 300
CONVERT_OUTPUT_OPTIONS=-resize 640 -quality 90 -alpha remove

# pdf2svg
PDF2SVG=inkscape
PDF2SVG_INPUT_OPTIONS=
PDF2SVG_OUTPUT_OPTIONS=

# lower case .tex only
TEX_FILES=$(wildcard *.tex)
PDF_FILES=$(patsubst %.tex, %.pdf, $(TEX_FILES))
PNG_FILES=$(patsubst %.tex, %.png, $(TEX_FILES))
SVG_FILES=$(patsubst %.tex, %.svg, $(TEX_FILES))


# build images
.PHONY : pngs
pngs : $(PNG_FILES)

%.png : %.pdf
	$(CONVERT) $(CONVERT_INPUT_OPTIONS) $< $(CONVERT_OUTPUT_OPTIONS) $@

# build svg
.PHONY : svgs
svgs : $(SVG_FILES)

%.svg : %.pdf
	$(PDF2SVG) -f $< -A $@

# build pdfs
.PHONY : pdfs
pdfs : $(PDF_FILES)

%.pdf : %.tex
	$(LATEX) $<

# build tex
.PHONY : tex
tex    : $(TEX_FILES)

%.tex  : $(PROJECT)_tex.py $(PROJECT).tex.jinja $(PROJECT).json Makefile
	$(PYTHON) $<	

$(PROJECT).json : $(PROJECT)_configure.py
	$(PYTHON) $<
	
.PHONY : all
all    : $(PROJECT)_tex.py Makefile
	$(PYTHON) $<
	make

# clean
.PHONY : clean
clean : 
	latexmk -c
	rm *.tex

# variables
.PHONY : variables
variables:
	@echo TEX_FILES: $(TEX_FILES)
	@echo PDF_FILES: $(PDF_FILES)
	@echo PNG_FILES: $(PNG_FILES)

