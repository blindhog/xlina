#!/usr/bin/env python3

from xlina import print_list,generate_header_h1,group_auto_nat_config
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('-f','--file',help='ASA Config Input file',required=True)

args = argparser.parse_args()
if args.file:
    file = args.file 


def main(file):
    print_list(generate_header_h1('Organized Auto NAT Configuration'))
    print_list(group_auto_nat_config(file))
    
    

if '__main__' in __name__:
    main(file)
