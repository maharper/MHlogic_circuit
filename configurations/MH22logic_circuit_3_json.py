#!/usr/bin/env python3

# Produce the json file that defines
# the configuration of the problem

project = 'MH22logic_circuit_3'
config_dir = 'configurations'

from pathlib import Path
import json
Bnegations_min = 0
Bnegations_max = 1
negations_min = 1
negations_max = 2

configurations = []

for Atogate, Aname, Afunction in [('short','0','$A'),('inline not','1','~$A')]:
    for Ctogate, Cname, Cfunction in [('short','0','$C'),('inline not','1','~$C')]:
        for Btogate1, Bname1, Bfunction1 in [('short','0','$B'),('inline not','1','~$B')]:
            for Btogate2, Bname2, Bfunction2 in [('short','0','$B'),('inline not','1','~$B')]:
                for gate1, gate1name, gate1function in [('or','0','|'),('and','1','&')]:
                    for gate1out, gate1outname, gate1outfunction in [('short','0',''),('inline not','1','~')]:
                        for gate2, gate2name, gate2function in [('or','0','|'),('and','1','&')]:
                            for gate2out, gate2outname, gate2outfunction in [('short','0',''),('inline not','1','~')]:
                                for gate3, gate3name, gate3function in [('or','0','|'),('and','1','&')]:
                                    Bnegations = sum(map(int,(Bname1, Bname2)))
                                    total_negations = Bnegations + sum(map(int,(Aname, Cname,gate1outname,gate2outname)))
                                    if (Bnegations_min <= Bnegations <= Bnegations_max) and (negations_min <= total_negations <= negations_max):
                                        configurations.append({
                                            "filename": Aname+Cname+Bname1+Bname2+gate1name+gate1outname+gate2name+gate2outname+gate3name,
                                            "Atogate": Atogate,
                                            "Ctogate": Ctogate,
                                            "Btogate1": Btogate1,
                                            "Btogate2": Btogate2,
                                            "gate1": gate1,
                                            "gate1out" : gate1out,
                                            "gate2": gate2,
                                            "gate2out" : gate2out,
                                            "gate3": gate3,
                                            "perl_function": ' '.join(['(',gate1outfunction,'(',Afunction,gate1function,Bfunction1,'))',gate3function,'(',gate2outfunction,'(',Bfunction2,gate2function,Cfunction,'))']),
                                            })

json_out = Path(config_dir) / (project+'.json')

with open(json_out, "w") as write_file:
    json.dump(configurations, write_file)
    
