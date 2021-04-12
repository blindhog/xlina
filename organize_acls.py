#!/usr/bin/env python3

import xlina
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('-f','--files',help='ASA Config Input file',required=True,nargs='*')

args = argparser.parse_args()
if args.files:
    file_list = args.files

def main(file_list):
    for config in file_list:
        x = xlina.LINA()
        x.print_list(x.generate_header_h1('Organized ACLs and associated Objects'))
        x.print_list(x.group_acls_objects(config))
    
if '__main__' in __name__:
    main(file_list)