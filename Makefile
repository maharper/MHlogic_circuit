# project
PROJECT=MHlogic_circuit
PROBLEMS = MH20logic_circuit_1 MH22logic_circuit_2 MH22logic_circuit_3 MH22logic_circuit_3b MH22logic_circuit_6
CONFIG_DIR = configurations
TEX_DIR=tex
FIG_DIR=figs
PG_DIR=pg
TEMPLATES_DIR=templates

# Python
# PYTHON=py
PYTHON=$(VENV)/python

# LaTeX
LATEX=latexmk
LATEX_OPTIONS:=-cd -pdf

# convert
CONVERT=magick
CONVERT_INPUT_OPTIONS=-density 300
CONVERT_OUTPUT_OPTIONS=-resize 640 -quality 90 -alpha remove

# pdf2svg
PDF2SVG=dvisvgm
PDF2SVG_OPTIONS=--pdf --optimize=all --verbosity=3 # --stdout

# lower case .tex only
#TEX_FILES=$(wildcard $(TEX_DIR)/*.tex)
#PDF_FILES=$(TEX_FILES:$(TEX_DIR)%.tex=$(FIG_DIR)%.pdf)
#PNG_FILES=$(TEX_FILES:$(TEX_DIR)%.tex=$(FIG_DIR)%.png)
#SVG_FILES=$(TEX_FILES:$(TEX_DIR)%.tex=$(FIG_DIR)%.svg)
# PDF_FILES=$(patsubst %.tex, %.pdf, $(TEX_FILES))

# build project
# $(PROJECT).tgz : $(PG_DIR)/$(PROJECT).pg $(PNG_FILES) $(SVG_FILES)
	# rm -rf $(PROJECT)/
	# mkdir $(PROJECT)/
	# cp $^ $(PROJECT)/
	# tar -czf $@ $(PROJECT)
	# rm -r $(PROJECT)/

$(PROJECT).tgz : $(PROBLEMS:%=$(PROJECT)/%.tgz)
	echo $^
	tar -czf $@ $(PROBLEMS:%=$(PROJECT)/%/*)
	# rm -rf $(PROJECT)/
	# mkdir $(PROJECT)/
	# cp $^ $(PROJECT)/
	# tar -czf $@ $(PROJECT)
	# rm -r $(PROJECT)/

.PRECIOUS : $(PROJECT)/%.tgz
$(PROJECT)/%.tgz : %/$(FIG_DIR)/png.stamp %/$(FIG_DIR)/svg.stamp %/$(PG_DIR)/problem.pg
	rm -rf $(PROJECT)/$*
	mkdir -p $(PROJECT)/$*
	cp $*/$(FIG_DIR)/*.png $(PROJECT)/$*
	cp $*/$(FIG_DIR)/*.svg $(PROJECT)/$*
	cp $*/$(PG_DIR)/problem.pg $(PROJECT)/$*/$*.pg
	tar -czf $@ -C $(PROJECT)/ $*
#	rm -r $(PROJECT)/$*
# tar cvzf WW.tgz -C model201-901\ *

# build png
#.PHONY : pngs
#pngs : $(PNG_FILES)

# .PRECIOUS : %png.stamp
# %png.stamp : %pdf.stamp
	# echo $@,$*,$<
	# $(foreach file, $(wildcard $*/$(FIG_DIR)/*.pdf), $(CONVERT) $(CONVERT_INPUT_OPTIONS) $(file) $(CONVERT_OUTPUT_OPTIONS) $(subst .pdf,.png,$(file));)
	# touch $@

.PRECIOUS : %/$(FIG_DIR)/png.stamp
%/$(FIG_DIR)/png.stamp : %/$(FIG_DIR)/pdf.stamp  $(subst .pdf,.png,$(wildcard $\*/$(FIG_DIR)/*.pdf))
#	$(foreach file, $(wildcard $*/$(FIG_DIR)/*.pdf), $(CONVERT) $(CONVERT_INPUT_OPTIONS) $(file) $(CONVERT_OUTPUT_OPTIONS) $(subst .pdf,.png,$(file));)
	touch $@
#  $(subst .pdf,.png,$(wildcard $\*/figs/*.pdf))

.PRECIOUS : %.png	
%.png : %.pdf
	$(CONVERT) $(CONVERT_INPUT_OPTIONS) $< $(CONVERT_OUTPUT_OPTIONS) $@

# build svg
#.PHONY : svgs
#svgs : $(SVG_FILES)

#  $(subst pdf,svg,$(wildcard $\*/figs/*.pdf))

.PRECIOUS : %/$(FIG_DIR)/svg.stamp
%/$(FIG_DIR)/svg.stamp : %/$(FIG_DIR)/pdf.stamp $(subst .pdf,.svg,$(wildcard $\*/$(FIG_DIR)/*.pdf))
#	$(foreach file, $(wildcard $*/$(FIG_DIR)/*.pdf), $(PDF2SVG) $(PDF2SVG_OPTIONS) --output=$(subst .pdf,.svg,$(file)) $(file);)	
	touch $@

#  
# $(subst .pdf,.svg,$(wildcard $\*/$(FIG_DIR)/*.pdf))
.PRECIOUS : %.svg %/$(FIG_DIR)/pdf.stamp
%.svg : %.pdf
	$(PDF2SVG) $(PDF2SVG_OPTIONS) --output=$@ $< 

# build pdfs
#.PHONY : pdfs
#pdfs : $(PDF_FILES)

#$(FIG_DIR)/%.pdf : $(TEX_DIR)/%.tex
#	$(LATEX) $(LATEX_OPTIONS) $<
#	mv $(TEX_DIR)/$*.pdf $(FIG_DIR)

.PRECIOUS : %/$(FIG_DIR)/pdf.stamp
%/$(FIG_DIR)/pdf.stamp : %/$(TEX_DIR)/tex.stamp
	$(LATEX) $(LATEX_OPTIONS) $*/$(TEX_DIR)/*.tex
	mkdir -p $*/$(FIG_DIR)
	mv $*/$(TEX_DIR)/*.pdf $*/$(FIG_DIR)
	touch $@

# build tex
#.PHONY : tex
#tex    : $(TEX_FILES)

#%.tex  : $(PROJECT)_tex.py $(TEMPLATES_DIR)/$(PROJECT).tex.jinja $(PROJECT).json Makefile
#	$(PYTHON) $<	

.PRECIOUS : %/$(TEX_DIR)/tex.stamp
%/$(TEX_DIR)/tex.stamp : $(PROJECT)_tex.py $(TEMPLATES_DIR)/%.tex.jinja $(CONFIG_DIR)/%.json
	mkdir -p $*/$(TEX_DIR)/
	$(PYTHON) $< $*
	touch $*/$(TEX_DIR)/tex.stamp

# build pg
.PRECIOUS : %/$(PG_DIR)/problem.pg
%/$(PG_DIR)/problem.pg : $(PROJECT)_pg.py $(TEMPLATES_DIR)/%.pg.jinja $(CONFIG_DIR)/%.json
	$(PYTHON) $< $*

# Build configuration
# $(TEMPLATES_DIR)/$(PROJECT).json : $(PROJECT)_configure.py
.PRECIOUS : $(CONFIG_DIR)/%.json
$(CONFIG_DIR)/%.json : $(CONFIG_DIR)/%_json.py
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

# for python virtual environment
include Makefile.venv

