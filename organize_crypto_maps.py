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
        confparse = CiscoConfParse(file, syntax='asa')
        hostname = confparse.find_lines('^hostname')[0].split(' ')[1]
        x.print_list(x.generate_header_h1('{} - Organized L2L IPSec Configurations -'.format(hostname)))
        x.print_list(x.group_crypto_map_config(file))

if '__main__' in __name__:
    main(file_list)
