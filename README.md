The goal is to learn how to produce multiple images for inclusion in a single WW problem.

Tool chain

LaTeX including TikZ produces pdf
ImageMagik: pdf -> pngs
dvisvgm: pdf -> svgs
The LaTeX files are based on a Jinja template
The pg file is created from a jinja template
Configuration rests in a json file.
Python files control the Jinja templates
make file controls the whole she bang

Initial files:
Starting LaTeX from C:\Users\Malcolm\Documents\Computing\LaTeX\Sandbox\Circuitkz\Circuitkz_1.tex as logic_circuit_1.tex.jinja
Starting makefile from C:\Users\Malcolm\Documents\Computing\LaTeX\Examples\digraph
python control file from C:\Users\Malcolm\Documents\Computing\Jinja\Jinja Experimentation 2020-12-14 and C:\Users\Malcolm\Documents\Computing\Jinja\TTL255 Tutorial

## Requirements

* python
    * pathlib requires >= 3.6
* jinja2
* make (choco under windows)
* [imagemagick](https://imagemagick.org)
	* which relies on [Ghostscript](https://www.ghostscript.com/)
* a modern LaTeX
    * including latexmk
    * including dvisvgm
