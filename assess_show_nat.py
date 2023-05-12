#!/usr/bin/env python3
import pprint
import argparse
import collections
from ntc_templates.parse import parse_output

argparser = argparse.ArgumentParser()
argparser.add_argument('-f','--files',help='ASA Config Input files',required=True,nargs="*")
argparser.add_argument('-a','--all',help='Zero Hit Nat Statements',required=False,action='store_true')
argparser.add_argument('-c','--count',help='Show Hit Counts',required=False,action='store_true')
argparser.add_argument('-d','--debugging',help='Debug Data',required=False,action='store_true')
argparser.add_argument('-r','--remove',help='Remove Command Statements',required=False,action='store_true')
argparser.add_argument('-s','--show',help='Show run nat',required=False,action='store_true')
argparser.add_argument('-z','--zero',help='Zero Hit Nat Statements',required=False,action='store_true')

args = argparser.parse_args()

pp = pprint.PrettyPrinter(indent=4)

all_nat = False
script_debug = False
count = False
hitcnt0_nat = False
show = False
remove = False

if args.files:
    file_list = args.files
if args.count:
    count = args.count
if args.debugging:
    script_debug = args.debugging
if args.all:
    all_nat = args.all
if args.zero:
    hitcnt0_nat = args.zero
if args.remove:
    remove = args.remove
if args.show:
    show = args.show

def build_nat_config(nat,remove=False):
    output = []
    nat_command = ""
    # Section 1 = Manual NAT
    if nat['nat_section_number'] == "1":
        if remove == True:
            nat_command = nat_command + "no "
        nat_command = nat_command + "nat ({},{})".format(nat['source_interface'],nat['destination_interface'])
        # Section 3 = After-auto Manual NAT
        if nat['nat_section_number'] == "3":    
            nat_command = nat_command + " after-auto"
        nat_command = nat_command + " source {} {} {}".format(nat['source_type'],nat['source_real'],nat['source_mapped'])
        if (nat['destination_real'] != "") & (nat['destination_mapped'] != ""):
            nat_command = nat_command + " destination static {} {}".format(nat['destination_real'],nat['destination_mapped'])
        if (nat['service_real'] != "") & (nat['service_mapped'] != ""):
            nat_command = nat_command + " service {} {}".format(nat['service_real'],nat['service_mapped'])
        if nat['extended'] != "":
            nat_command = nat_command + " {}".format(nat['extended'])
        if nat['flat'] != "":
            nat_command = nat_command + " {}".format(nat['flat'])
        if nat['include_reserve'] != "":
            nat_command = nat_command + " {}".format(nat['include_reserve'])
        if nat['round_robin'] != "":
            nat_command = nat_command + " {}".format(nat['round_robin'])                    
        if nat['net_to_net'] != "":
            nat_command = nat_command + " {}".format(nat['net_to_net'])   
        if nat['dns'] != "":
            nat_command = nat_command + " {}".format(nat['dns']) 
        if nat['unidirectional'] != "":
            nat_command = nat_command + " {}".format(nat['unidirectional'])                         
        if nat['no_proxy_arp'] != "":
            nat_command = nat_command + " {}".format(nat['no_proxy_arp'])   
        if nat['route_lookup'] != "":
            nat_command = nat_command + " {}".format(nat['route_lookup'])                           
        if nat['inactive'] != "":
            nat_command = nat_command + " {}".format(nat['inactive'])                           
        if nat['description'] != "":
            nat_command = nat_command + " description {}".format(nat['description'])                           
        
        output.append(nat_command)

    # Section 2 = Auto NAT
    if nat['nat_section_number'] == "2":
        output.append("object network {}".format(nat['source_real']))
        nat_command = "  "
        if remove == True:
            nat_command = nat_command + "no "
        nat_command = nat_command + "nat ({},{}) {} {}".format(nat['source_interface'],nat['destination_interface'],nat['source_type'],nat['source_mapped'])
        if nat['net_to_net'] != "":
            nat_command = nat_command + " {}".format(nat['net_to_net'])   
        if nat['dns'] != "":
            nat_command = nat_command + " {}".format(nat['dns']) 
        if nat['service_protocol'] != "":
            nat_command = nat_command + " service {} {} {}".format(nat['service_protocol'],nat['service_real'],nat['service_mapped']) 
        if nat['no_proxy_arp'] != "":
            nat_command = nat_command + " {}".format(nat['no_proxy_arp'])   
        if nat['route_lookup'] != "":
            nat_command = nat_command + " {}".format(nat['route_lookup'])

        output.append(nat_command)

    return output

def main(file_list):
    for file in file_list:
        show_nat_output = open(file, "r")
        config_output = []
        hitcnt0_output = []

        nat_parsed = parse_output(platform="cisco_asa", command="show nat", data=show_nat_output.read())
        for nat in sorted(nat_parsed, key=lambda d: d['nat_section_number']):
            if script_debug == True:
                config_output.append("\n\n+---\n\n{}".format(nat))
            if count == True:
                config_output.append("\n!- Translated Hits: {}  Untranslated Hits: {}".format(nat['translate_hits'],nat['untranslate_hits']))
            config_output.extend(build_nat_config(nat,remove=remove))
            if (nat['translate_hits'] == "0") and (nat['untranslate_hits'] == "0"):
                if script_debug == True:
                    hitcnt0_output.append("\n\n+---\n\n{}".format(nat))
                if count == True:
                    hitcnt0_output.append("\n!- Translated Hits: {}  Untranslated Hits: {}".format(nat['translate_hits'],nat['untranslate_hits']))
                hitcnt0_output.extend(build_nat_config(nat,remove=remove))

    if all_nat == True:
        print("!==============================\n! All NAT Commands\n!==============================\n\n")
        for line in config_output:
            print(line)

    if hitcnt0_nat == True:
        print("!==============================\n! Unused NAT Commands \n!==============================\n\n")
        for line in hitcnt0_output:
            print(line)
        

if '__main__' in __name__:
    main(file_list)