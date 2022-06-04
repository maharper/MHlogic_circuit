#!/usr/bin/env python3
"""Produces TeX code from JSON configuration and a jinja template.

The problem name is required, see --help for the other prarameters.
"""

from argparse import ArgumentParser
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

project = 'MHlogic_circuit'

def main():

    args = parse_args()
    configurations = get_configs(args.configuration)
    Path(args.tex).mkdir(parents=True, exist_ok=True)
    write_tex(configurations, args.template, args.tex)
    list_configurations(args.problem, configurations)

def parse_args():
 
    config_dir =  'configurations'
    templ_dir = 'templates'
#    tex_dir = 'tex'
    tex_dir = ''
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('problem', help = 'Problem name to process')
    parser.add_argument('--configuration', help = f'JSON configuration file, defaults to ./{config_dir}/<problem>.json')
    parser.add_argument('--template', help = f'PG input template file, defaults to ./{templ_dir}/<problem>.tex.jinja')
    parser.add_argument('--tex', help = f'TEX output directory, defaults to ./<problem>/{tex_dir}/')
    args = parser.parse_args()
    if args.configuration is None: args.configuration = Path(config_dir) / (args.problem+'.json')
    if args.template is None: args.template = Path(templ_dir) / (args.problem+'.tex.jinja')
    if args.tex is None: args.tex = Path(args.problem) / tex_dir
    return(args)

def get_configs(config_file):

    with open(config_file, "r") as read_file:
        configurations = json.load(read_file)
    return(configurations)

def write_tex(configurations, template_file, out_dir):

    template = get_tex_template(template_file)
    Path.mkdir(out_dir, parents=True, exist_ok=True)
    with open(Path(out_dir)/'tex.stamp','w') as stamp:
        for configuration in configurations:
            tex_document = template.render(configuration, undefined=StrictUndefined)
            with open(Path(out_dir)/(configuration["filename"]+'.tex'),'w') as output:
                output.write(tex_document)
            stamp.write(configuration["filename"])

def get_tex_template(template_file):

    file_loader = FileSystemLoader(template_file.parent)
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
    return(latex_jinja_env.get_template(template_file.name))

def list_configurations(problem, configurations):

    Path.mkdir(Path(problem), parents=True, exist_ok=True)
    with open(Path(problem)/'configurations','w') as configurations_list:
        configurations_list.write(problem+"_FILE_STEM_LIST=")
        for configuration in configurations:
            configurations_list.write(configuration["filename"]+' ')

if __name__ == '__main__':
    main()