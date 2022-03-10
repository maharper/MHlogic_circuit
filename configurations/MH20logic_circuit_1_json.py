#!/usr/bin/env python3

# Produce the json file that defines
# the configuration of the problem

project = 'MH20logic_circuit_1'
config_dir = 'configurations'

from pathlib import Path
import json


configurations = []

for Atogate, Aname, Afunction in [('short','0','$A'),('inline not','1','~$A')]:
    for gate, gatename, gatefunction in [('or','0','|'),('and','1','&')]:
        for Btogate, Bname, Bfunction in [('short','0','$B'),('inline not','1','~$B')]:
            configurations.append({
                "filename": Aname+gatename+Bname,
                "Atogate": Atogate,
                "gate": gate,
                "Btogate": Btogate,
                "perl_function": Afunction+' '+gatefunction+' '+Bfunction
                })

json_out = Path(config_dir) / (project+'.json')

with open(json_out, "w") as write_file:
    json.dump(configurations, write_file)
    
