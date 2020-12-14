The goal is to learn how to produce multiple images for inclusion in a single WW problem.

Tool chain

LaTeX including TikZ produces pdf
ImageMagik: pdf -> image formats
The LaTeX files are based on a Jinja template
A Python file controls the Jinja template
make file controls the whole she bang

Not for now (real overkill) data stored in JSON or YAML file.

Initial files:
Starting LaTeX from C:\Users\Malcolm\Documents\Computing\LaTeX\Sandbox\Circuitkz\Circuitkz_1.tex as logic_circuit_1.tex.jinja
Starting makefile from C:\Users\Malcolm\Documents\Computing\LaTeX\Examples\digraph
python control file from C:\Users\Malcolm\Documents\Computing\Jinja\Jinja Experimentation 2020-12-14 and C:\Users\Malcolm\Documents\Computing\Jinja\TTL255 Tutorial