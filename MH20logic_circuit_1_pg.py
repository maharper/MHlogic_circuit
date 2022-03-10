#!/usr/bin/env python3
"""logic_circuit_pg.py reads configuration data from <project>.json and
a pg template from <project>.pg.jinja and combines it into pg problem code.
"""

project = 'MH20logic_circuit_1'
config_dir = 'configurations'
# int_suffix = '_intermediates'
pg_dir = 'pg'

from argparse import ArgumentParser
from pathlib import Path
import json
from jinja2 import Environment, FileSystemLoader, StrictUndefined

parser = ArgumentParser(description='Combine configuration json and jinja template into pg code.')
parser.add_argument('project', help = 'Project name to process')
parser.add_argument('--configuration', help = 'JSON configuration file, defaults to ./configurations/<project>.json')
parser.add_argument('--pg', help = 'Sub-directory for output pg, defaults to ./<project>/pg/')

args = parser.parse_args()

project = args.project
config_file = args.configuration if args.configuration is not None else Path(config_dir) / (project+'.json')
template_file = project+'.pg.jinja'
pg_dir = args.pg if args.pg is not None else Path(project) / pg_dir


file_loader = FileSystemLoader(['.','templates'])

pg_jinja_env = Environment(
    trim_blocks = True,
    autoescape = False,
    loader=file_loader,
    )

template = pg_jinja_env.get_template(template_file)

with open(config_file, "r") as read_file:
    configurations = json.load(read_file)
    
pg_document = template.render({'configurations':configurations}, undefined=StrictUndefined)

Path.mkdir(pg_dir, parents=True, exist_ok=True)
with open(pg_dir / ('problem.pg'),'w', newline='\n') as output:
    output.write(pg_document)
