# MHlogic_circuit

My goal was to learn how to produce multiple images for inclusion in a single WW problem.
It is possible, of course, to write pg code which will call TikZ from WW
and produce excellent images for a problem on-the-fly, post-randomization.
Using TikZ from withing WW is under active development.
The approach here _pre-produces_ the images, putting less load on the server when the questions are active.
Of course, this requires more storage on the server, but disk capacity isn't an issue for us now.

## Tool chain

* _LaTeX_ including TikZ produces pdf
* _ImageMagik_: pdf -> pngs
* _dvisvgm_: pdf -> svgs
* The _LaTeX_ files are based on a _Jinja_ template
* The _pg_ file is created from a _Jinja_ template
* Configuration of each problem rests in a _json_ file.
* _Python_ files control the Jinja templates
* a _make_ file controls the whole shebang

## Requirements

* python
    - pathlib requires >= 3.6
* jinja2
* make (I use choco to install make under windows)
* [imagemagick](https://imagemagick.org)
    - which relies on [Ghostscript](https://www.ghostscript.com/)
* a modern LaTeX
    - including TikZ and CircuiTikZ
    - including latexmk
    - including dvisvgm

## Initial files (for my reference only)

* Starting LaTeX from C:\Users\Malcolm\Documents\Computing\LaTeX\Sandbox\Circuitkz\Circuitkz_1.tex as logic_circuit_1.tex.jinja
* Starting makefile from C:\Users\Malcolm\Documents\Computing\LaTeX\Examples\digraph
* python control file from C:\Users\Malcolm\Documents\Computing\Jinja\Jinja Experimentation 2020-12-14 and
* C:\Users\Malcolm\Documents\Computing\Jinja\TTL255 Tutorial

Almost no traces of these original sources remain in the current version of the project ;-).
