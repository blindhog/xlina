#!/usr/bin/env python3

import xlina
import argparse
from ciscoconfparse import CiscoConfParse

argparser = argparse.ArgumentParser()
argparser.add_argument('-f','--files',help='ASA Config Input files',required=True,nargs="*")
argparser.add_argument('-a','--acl',help='Specify Access-list',required=False)
argparser.add_argument('--hitcnt',help='Only use access-lists with hitcnt numbers',action='store_true',required=False)

args = argparser.parse_args()

hitcnt = False
acl = ''

if args.files:
    file_list = args.files

if args.acl:
    acl = args.acl

if args.hitcnt:
    hitcnt = args.hitcnt




def main(file_list,acl,hitcnt):
    for file in file_list:
        x = xlina.LINA()
        hostname = ''
        confparse = CiscoConfParse(file)
        hostname = confparse.find_lines('^hostname')[0].split(' ')[1]
        x.print_list(x.generate_header_h1('{} - Organized ACLs and associated Objects -'.format(hostname)))
        x.print_list(x.group_acls_objects(file,acl,hitcnt))
   
if '__main__' in __name__:
    main(file_list,acl,hitcnt)
    