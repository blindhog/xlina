#!/usr/bin/env python3

import xlina
import argparse
from ciscoconfparse import CiscoConfParse

argparser = argparse.ArgumentParser()
argparser.add_argument('-f','--files',help='ASA Config Input files',required=True,nargs="*")

args = argparser.parse_args()

if args.files:
    file_list = args.files


def main(file_list):
    for file in file_list:
        x = xlina.LINA()
        hostname = ''
        confparse = CiscoConfParse(file)
        hostname = confparse.find_lines('^hostname')[0].split(' ')[1]
        x.print_list(x.generate_header_h1('{} - Organized Auto NAT Configurations -'.format(hostname)))
        x.print_list(x.group_auto_nat_config(file))

if '__main__' in __name__:
    main(file_list)
