#! /usr/bin/python

# Produce the json file that defines
# the configuration of the problem

project = 'MH20logic_circuit_1'

import json

configuration = [
    {
        "filename": "000",
        "Atogate": "short",
        "gate": "or",
        "Btogate": "short"
        },
    {
        "filename": "001",
        "Atogate": "short",
        "gate": "or",
        "Btogate": "inline not"
        },
    ]
# configuration = {
    # "000": {
        # "filename": "000",
        # "Atogate": "short",
        # "gate": "or",
        # "Btogate": "short"
        # },
    # "001": {
        # "filename": "001",
        # "Atogate": "short",
        # "gate": "or",
        # "Btogate": "inline not"
        # },
    # }

configurations = []

for Atogate, Aname, Afunction in [('short','0','A'),('inline not','1','~A')]:
    for gate, gatename, gatefunction in [('or','0','or'),('and','1','and')]:
        for Btogate, Bname, Bfunction in [('short','0','B'),('inline not','1','~B')]:
            configurations.append({
                "filename": Aname+gatename+Bname,
                "Atogate": Atogate,
                "gate": gate,
                "Btogate": Btogate,
                "perl_function": Afunction+' '+gatefunction+' '+Bfunction
                })

json_out = project+'.json'

with open(json_out, "w") as write_file:
    json.dump(configurations, write_file)
    
# from jinja2 import Environment, FileSystemLoader, StrictUndefined
# file_loader = FileSystemLoader(['.','templates'])
# latex_jinja_env = Environment(
    # block_start_string =    '\BLOCK{',
    # block_end_string =      '}',
    # variable_start_string = '\VAR{',
    # variable_end_string =   '}',
    # comment_start_string =  '\#{',
    # comment_end_string =    '}',
    # line_statement_prefix = '%-',
    # line_comment_prefix =   '%#',
    # trim_blocks = True,
    # autoescape = False,
    # loader=file_loader,
    # )

# """ template = env.get_template('base.html.jinja')

# output = template.render(title='pretty standard')
 # """
 
# template = latex_jinja_env.get_template('logic_circuit_1.tex.jinja')

# for Agatelink, Agatename in [('short','A'),('inline not','nA')]:
    # for Bgatelink, Bgatename in [('short','B'),('inline not','nB')]:
        # for gate, gatename in [('or','or'),('and','and')]:
            # document = template.render(Agatelink=Agatelink,Bgatelink=Bgatelink,gate=gate,undefined=StrictUndefined)
            # tex_file=Agatename+gatename+Bgatename+'.tex'
            # with open(tex_file,'w') as output:
                # output.write(document)