#!/usr/bin/env python3

# Produce the json file that defines
# the configuration of the problem

problem = 'MH22logic_circuit_3'
config_dir = 'configurations'

import json
from pathlib import Path
import itertools

configurations = []

def accept_config(A, B, C, gate):
    notcount = int(A[1]) + int(B[1]) + int(C[1])
    return(1<=notcount<=2)

for A in [('short','0','$A'),('inline not','1','~$A')]:
    for B in [('short','0','$B'),('inline not','1','~$B')]:
        for C in [('short','0','$C'),('inline not','1','~$C')]:
            for gate in [('or','0','|'),('and','1','&')]:
                if accept_config(A, B, C, gate):   
                    configurations.append({
                        "filename": A[1]+B[1]+C[1]+gate[1],
                        "Atogate": A[0],
                        "Btogate": B[0],
                        "Ctogate": C[0],
                        "gate": gate[0],
                        "perl_function": ' '.join(['(',A[2],gate[2],B[2],gate[2],C[2],')' ])
                        })

json_out = Path(config_dir) / (problem+'.json')

with open(json_out, "w") as write_file:
    json.dump(configurations, write_file)
