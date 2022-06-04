#!/usr/bin/env python3
"""Produces WeBWorK pg code from JSON configuration and a jinja template.

See --help for parameters
"""

from argparse import ArgumentParser
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

project = 'MHlogic_circuit'

def main():

    args = parse_args()
    configurations = get_configs(args.configuration)
    pg_code = produce_pg(args.template, configurations)
    write_pg(pg_code, args.pg)

def parse_args():
 
    config_dir =  'configurations'
    templ_dir = 'templates'
#    pg_dir = 'pg'
    pg_dir = ''
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('problem', help = 'Problem name to process')
    parser.add_argument('--configuration', help = f'JSON configuration file, defaults to ./{config_dir}/<problem>.json')
    parser.add_argument('--template', help = f'PG input template file, defaults to ./{templ_dir}/<problem>.pg.jinja')
    parser.add_argument('--pg', help = f'PG output file, defaults to ./<problem>/{pg_dir}/problem.pg')
    args = parser.parse_args()
    if args.configuration is None: args.configuration = Path(config_dir) / (args.problem+'.json')
    if args.template is None: args.template = Path(templ_dir) / (args.problem+'.pg.jinja')
    if args.pg is None: args.pg = Path(args.problem) / pg_dir / 'problem.pg'
    return(args)

def get_configs(config_file):

    with open(config_file, "r") as read_file:
        configurations = json.load(read_file)
    return(configurations)

def produce_pg(template_file, configurations):

    file_loader = FileSystemLoader(template_file.parent)
    pg_jinja_env = Environment(
        trim_blocks = True,
        autoescape = False,
        loader=file_loader,
        )
    template = pg_jinja_env.get_template(template_file.name)
    return(template.render({'configurations':configurations}, undefined=StrictUndefined))

def write_pg(pg_code, pg_file):

    Path(pg_file).parent.mkdir(parents=True, exist_ok=True)
    with open(pg_file,'w', newline='\n') as output:
        output.write(pg_code)

if __name__ == '__main__':
    main()






    



