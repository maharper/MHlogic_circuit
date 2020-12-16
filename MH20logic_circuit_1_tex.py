#! /usr/bin/python

# Experimenting with the Jinja and LaTeX
# from https://tug.org/tug2019/slides/slides-ziegenhagen-python.pdf

project = 'MH20logic_circuit_1'

import json
from jinja2 import Environment, FileSystemLoader, StrictUndefined
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

""" template = env.get_template('base.html.jinja')

output = template.render(title='pretty standard')
 """
 
template = latex_jinja_env.get_template(project+'.tex.jinja')

with open(project+".json", "r") as read_file:
    configurations = json.load(read_file)
    
# for Agatelink, Agatename in [('short','A'),('inline not','nA')]:
    # for Bgatelink, Bgatename in [('short','B'),('inline not','nB')]:
        # for gate, gatename in [('or','or'),('and','and')]:
            # document = template.render(Agatelink=Agatelink,Bgatelink=Bgatelink,gate=gate,undefined=StrictUndefined)
            # tex_file=Agatename+gatename+Bgatename+'.tex'

for configuration in configurations:
    tex_document = template.render(configuration, undefined=StrictUndefined)
    with open(configuration["filename"]+'.tex','w') as output:
        output.write(tex_document)