# TODO

## Block

- [X] WW pg code

## Release

- [X] revisit filenames nAorB vs 100 vs ?
- [x] Comment and document all code - check done
- [x] tag pg - check done
- [ ] Update `pyproject.toml` (although it is only used to create the virtual environment now)

### Template

- [ ] tweak circuit presentation. Colours, line widths etc

## Enhancement

- [x] PGML
- [x] incorporate venv code into the makefile
- [x] extend to NAND/NOR
- [x] extend to more complicated situation
    * [x] three inputs
    * [ ] ...
- [ ] extend 6 to 6b using NANDs and NORs

## Extension

- [ ] Use these images in _Given the circuit diagram, what is the corresponding logical expression?_ questions
- [ ] Use the same workflow/toolchain to produce digraph/relation questions for the earlier section of the course.

### Makefile

- [x] Get the production of svg working
- [ ] research GraphicsMagick vs ImageMagick
    * supposedly GraphicsMagick is faster and more stable while ImageMagick is more versatile and flexible.
    * not important as I am only using svgs for now.

### Image format

- [x] Pick a lane, png or svg
    * svg, works fine now with the addition of `#!latex \papercolor{white}` to the texs

### git

- [ ] update .gitignore to ignore the generated .pg files, `/configuration` files, and the `tex.stamps`.
