#!/usr/bin/env python3

import xlina
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('-f','--file',help='ASA Config Input file',required=True)

args = argparser.parse_args()
if args.file:
    file = args.file 


def main(file):
    x = xlina.LINA()
    x.print_list(x.generate_header_h1('Organized Auto NAT Configuration'))
    x.print_list(x.group_auto_nat_config(file))
    
    

if '__main__' in __name__:
    main(file)
