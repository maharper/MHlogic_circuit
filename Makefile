# project
PROJECT=MH20logic_circuit_1
TEX_DIR=tex
FIG_DIR=figs

# Python
PYTHON=py

# LaTeX
LATEX=latexmk
LATEX_OPTIONS:=-cd -pdf

# convert
CONVERT=magick
CONVERT_INPUT_OPTIONS=-density 300
CONVERT_OUTPUT_OPTIONS=-resize 640 -quality 90 -alpha remove

# pdf2svg
PDF2SVG=dvisvgm
PDF2SVG_OPTIONS=--pdf --optimize=all --verbosity=3

# lower case .tex only
TEX_FILES=$(wildcard $(TEX_DIR)/*.tex)
PDF_FILES=$(TEX_FILES:$(TEX_DIR)%.tex=$(FIG_DIR)%.pdf)
PNG_FILES=$(TEX_FILES:$(TEX_DIR)%.tex=$(FIG_DIR)%.png)
SVG_FILES=$(TEX_FILES:$(TEX_DIR)%.tex=$(FIG_DIR)%.svg)
# PDF_FILES=$(patsubst %.tex, %.pdf, $(TEX_FILES))

# build images
.PHONY : pngs
pngs : $(PNG_FILES)

%.png : %.pdf
	$(CONVERT) $(CONVERT_INPUT_OPTIONS) $< $(CONVERT_OUTPUT_OPTIONS) $@

# build svg
.PHONY : svgs
svgs : $(SVG_FILES)

%.svg : %.pdf
	$(PDF2SVG) $(PDF2SVG_OPTIONS) $<

# build pdfs
.PHONY : pdfs
pdfs : $(PDF_FILES)

$(FIG_DIR)/%.pdf : $(TEX_DIR)/%.tex
	$(LATEX) $(LATEX_OPTIONS) $<
	mv $(TEX_DIR)/$*.pdf $(FIG_DIR)

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
	@echo SVG_FILES: $(SVG_FILES)

# for upload
$(PROJECT).tgz : $(PROJECT).pg $(PNG_FILES)
	rm -rf $(PROJECT)/
	mkdir $(PROJECT)/
	cp $^ $(PROJECT)/
	tar -czf $@ $(PROJECT)
	rm -r $(PROJECT)/


