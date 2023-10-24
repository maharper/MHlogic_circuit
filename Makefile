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
LATEX_OPTIONS:=-cd -pdf -quiet

# convert
CONVERT=magick
CONVERT_INPUT_OPTIONS=-density 300
CONVERT_OUTPUT_OPTIONS=-resize 640 -quality 90 -alpha remove

# pdf2svg
PDF2SVG=dvisvgm
PDF2SVG_OPTIONS=--pdf --optimize=all --verbosity=3 # --stdout

# Defines <problem>_FILE_STEM_LIST
# These include files are written by
# the <project>_tex.py <problem> calls
# under the %/tex.stamp %/configurations : rule
include $(addsuffix /configurations, $(PROBLEMS))

# build project
$(PROJECT).tgz : $(PROBLEMS:%=$(PROJECT)/%.tgz)
	echo $^
	tar -czf $@ $(PROBLEMS:%=$(PROJECT)/%/*)

# TODO sort out PRECIOUS, PHONY etc
# TODO, many PRECIOUS could be/should be SECONDARY
# SECONDARY can't have wildcards, PRECIOUS can.

.PRECIOUS : $(PROJECT)/%.tgz
.SECONDEXPANSION:
$(PROJECT)/%.tgz : $$(addprefix $$*/, $$(addsuffix .png, $$($$*_FILE_STEM_LIST))) $$(addprefix $$*/, $$(addsuffix .svg, $$($$*_FILE_STEM_LIST))) %/problem.pg
#	@echo $^
	rm -rf $(PROJECT)/$*
	mkdir -p $(PROJECT)/$*
	cp $*/*.png $(PROJECT)/$*
#	cp $*/*.svg $(PROJECT)/$*
	cp $*/problem.pg $(PROJECT)/$*/$*.pg
	tar -czf $@ -C $(PROJECT)/ $*

# build png
.SECONDEXPANSION :
.PRECIOUS : %.png
.PHONY : %/svgs svgs

pngs : $(addsuffix /pngs, $(PROBLEMS)) ;

%/pngs : $$(addprefix $$*/, $$(addsuffix .png, $$($$*_FILE_STEM_LIST))) ;
	
%.png : %.pdf
	$(CONVERT) $(CONVERT_INPUT_OPTIONS) $< $(CONVERT_OUTPUT_OPTIONS) $@

# build svg
.SECONDEXPANSION :
.PRECIOUS : %.svg
.PHONY : %/svgs svgs

svgs : $(addsuffix /svgs, $(PROBLEMS)) ;

%/svgs : $$(addprefix $$*/, $$(addsuffix .svg, $$($$*_FILE_STEM_LIST))) ;

%.svg : %.pdf
	$(PDF2SVG) $(PDF2SVG_OPTIONS) --output=$@ $< 

# build pdfs
.SECONDEXPANSION :
.PRECIOUS : %.pdf
.PHONY : %/pdfs pdfs

%.pdf : %.tex
	$(LATEX) $(LATEX_OPTIONS) $<
	
%/pdfs : $$(addprefix $$*/, $$(addsuffix .pdf, $$($$*_FILE_STEM_LIST))) ;

pdfs : $(addsuffix /pdfs, $(PROBLEMS)) ;

# build tex
.PHONY : texs
texs : $(addsuffix /tex.stamp, $(PROBLEMS)) ;

.PRECIOUS : %/tex.stamp
%/tex.stamp %/configurations : $(PROJECT)_tex.py $(TEMPLATES_DIR)/%.tex.jinja $(CONFIG_DIR)/%.json | venv
	mkdir -p $*
	$(PYTHON) $< $*
#	cp $*/$(TEX_DIR)/*.tex $*
	touch $*/tex.stamp

# build pg
.PRECIOUS : %/problem.pg
.PHONY : pgs

pgs : $(addsuffix /problem.pg, $(PROBLEMS)) ;

%/problem.pg : $(PROJECT)_pg.py $(TEMPLATES_DIR)/%.pg.jinja $(CONFIG_DIR)/%.json | venv
	$(PYTHON) $< $*
#	cp $*/$(PG_DIR)/problem.pg $*

# update configuration files
.PRECIOUS : $(CONFIG_DIR)/%.json
$(CONFIG_DIR)/%.json : $(CONFIG_DIR)/%_json.py
	$(PYTHON) $<

# clean
.PHONY : clean
clean : 
	rm -r $(PROBLEMS)
	rm -r $(PROJECT)
	rm -r $(PROJECT).tgz

# for python virtual environment
include Makefile.venv

