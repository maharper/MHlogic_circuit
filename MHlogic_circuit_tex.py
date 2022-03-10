#!/usr/bin/env python3
"""logic_circuit_tex.py reads configuration data from <project>.json and
a LaTeX template from <project>.tex.jinja and combines them into multiple tex files
to produce the images needed by the problem.
"""

project = 'MH20logic_circuit_1'
config_dir = 'configurations'
tex_dir = 'tex'

from argparse import ArgumentParser
from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader, StrictUndefined

parser = ArgumentParser(description='Combine configuration json and jinja template into tex code.')
parser.add_argument('project', help = 'Project name to process')
parser.add_argument('--configuration', help = 'JSON configuration file, defaults to ./configurations/<project>.json')
parser.add_argument('--tex', help = 'Sub-directory for output tex, defaults to ./<project>/tex/')

args = parser.parse_args()

project = args.project
config_file = args.configuration if args.configuration is not None else Path(config_dir) / (project+'.json')
template_file = project+'.tex.jinja'
tex_dir = args.tex if args.tex is not None else Path(project) / tex_dir

file_loader = FileSystemLoader(['.','templates'])

latex_jinja_env = Environment(
    block_start_string =    '\BLOCK{',
    block_end_string =      '}',
    variable_start_string = '\VAR{',
    variable_end_string =   '}',
    comment_start_string =  '\#{',
    comment_end_string =    '}',
    line_statement_prefix = '%-',
    line_comment_prefix =   '%#',
    trim_blocks = True,
    autoescape = False,
    loader=file_loader,
    )
 
template = latex_jinja_env.get_template(template_file)

with open(config_file, "r") as read_file:
    configurations = json.load(read_file)

Path.mkdir(tex_dir, parents=True, exist_ok=True)
for configuration in configurations:
    tex_document = template.render(configuration, undefined=StrictUndefined)
    with open(Path(tex_dir)/(configuration["filename"]+'.tex'),'w') as output:
        output.write(tex_document)