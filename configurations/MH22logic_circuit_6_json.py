#!/usr/bin/env python3

# Produce the json file that defines
# the configuration of the problem

problem = 'MH22logic_circuit_6'
config_dir = 'configurations'

import json
from pathlib import Path

def accept_config(A, C,  B1, B2, gate1, g1o, gate2, g2o, gate3):

# Original configuration yields 160 circuits :-)
    B_negation_min = 0
    B_negation_max = 1
    total_negation_min = 1
    total_negation_max = 2
    in_negation_min = 0
    in_negation_max = 4
    gate_negation_min = 0
    gate_negation_max = 2
    and_gate_min = 0
    and_gate_max = 3

# New configuration 4 x 2 x 6 = 48 circuits, still a lot
    B_negation_min = 0
    B_negation_max = 2
    total_negation_min = 0
    total_negation_max = 6
    in_negation_min = 1
    in_negation_max = 1
    gate_negation_min = 1
    gate_negation_max = 1
    and_gate_min = 1
    and_gate_max = 2

    B_negation_count = sum(map(int,(B1[1], B2[1])))
    in_negation_count = sum(map(int,(A[1], B1[1], B2[1], C[1])))
    gate_negation_count = sum(map(int,(g1o[1], g2o[1])))
    total_negation_count = in_negation_count + gate_negation_count
    and_gate_count = sum(map(int,(gate1[1], gate2[1], gate3[1])))
    accept = (B_negation_min <= B_negation_count <= B_negation_max) \
        and (in_negation_min <= in_negation_count <= in_negation_max) \
        and (gate_negation_min <= gate_negation_count <= gate_negation_max) \
        and (total_negation_min <= total_negation_count <= total_negation_max) \
        and (and_gate_min <= and_gate_count <= and_gate_max)
    return(accept)

configurations = []

for A in [('short','0','$A'),('inline not','1','~$A')]:                             # Atogate, Aname, Afunction
    for C in [('short','0','$C'),('inline not','1','~$C')]:                         # Ctogate, Cname, Cfunction
        for B1 in [('short','0','$B'),('inline not','1','~$B')]:                    # Btogate1, Bname1, Bfunction1
            for B2 in [('short','0','$B'),('inline not','1','~$B')]:                # Btogate2, Bname2, Bfunction2
                for gate1 in [('or','0','|'),('and','1','&')]:                      # gate1, gate1name, gate1function
                    for g1o in [('short','0',''),('inline not','1','~')]:           # gate1out, gate1outname, gate1outfunction
                        for gate2 in [('or','0','|'),('and','1','&')]:              # gate2, gate2name, gate2function
                            for g2o in [('short','0',''),('inline not','1','~')]:   # gate2out, gate2outname, gate2outfunction
                                for gate3 in [('or','0','|'),('and','1','&')]:      # gate3, gate3name, gate3function
                                    if accept_config(A, C,  B1, B2, gate1, g1o, gate2, g2o, gate3):
                                        configurations.append({
                                            "filename": ''.join([A[1], C[1], B1[1], B2[1], gate1[1], g1o[1], gate2[1], g2o[1], gate3[1]]),
                                            "Atogate": A[0],
                                            "Ctogate": C[0],
                                            "Btogate1": B1[0],
                                            "Btogate2": B2[0],
                                            "gate1": gate1[0],
                                            "gate1out" : g1o[0],
                                            "gate2": gate2[0],
                                            "gate2out" : g2o[0],
                                            "gate3": gate3[0],
                                            "perl_function": ' '.join(['(',g1o[2],'(',A[2],gate1[2],B1[2],'))',gate3[2],'(',g2o[2],'(',B2[2],gate2[2],C[2],'))']),
                                            })

json_out = Path(config_dir) / (problem+'.json')

with open(json_out, "w") as write_file:
    json.dump(configurations, write_file, indent=4)
    