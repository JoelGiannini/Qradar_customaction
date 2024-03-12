#!/usr/bin/python
from ldap3 import Server, Connection, ALL
import json
import os
import sys
import argparse

def get_mail (args):
  user = args.user[0:10]
  server = Server(args.ldaphost)
  conn = Connection(server, args.ldapuser, args.ldappass, auto_bind=True)
  conn.search(args.ldapbasedn, f'(&(objectclass=person)(uid={args.user}))', attributes=['mail'])
  if len(conn.entries) == 0:
    return "desconocido"
  else:  
    entry = conn.entries[0].entry_to_json()
    entry = json.loads(entry)
    entry = entry['attributes']['mail'][0]
    return entry

## parser
parser = argparse.ArgumentParser(prog="ldap_get_mail",description='[Description]: Get mail from LDAP',epilog='[Usege exemple]:-----> ldap_get_mail.py -u ldap_user_uid')
parser.add_argument( '--ldaphost',  help='by default env: LDAP_URL')
parser.add_argument( '--ldapuser',  help='by default env: LDAPUSER')
parser.add_argument( '--ldappass', help='by default env: LDAPPASS')
parser.add_argument( '--ldapbasedn', help='by default env: LDAPBASEDN')
parser.add_argument( '--user', '-u',type=str, help='User to search mail from LDAP')

if len(sys.argv) < 2:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()
if args.ldaphost == None:
  if os.getenv( 'LDAP_URL') != "":
     args.ldaphost = os.getenv( 'LDAP_URL')
if args.ldapuser == None:
  if os.getenv( 'LDAPUSER') != "":
     args.ldapuser = os.getenv( 'LDAPUSER')
if  args.ldappass == None:
  if os.getenv( 'LDAPPASS' ) != "":
     args.ldappass = os.getenv( 'LDAPPASS')
if  args.ldapbasedn == None:
  if os.getenv( 'LDAPBASEDN' ) != "":
     args.ldapbasedn = os.getenv( 'LDAPBASEDN')
print (get_mail(args))

