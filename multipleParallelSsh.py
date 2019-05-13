#!/usr/bin/env python

import argparse
import signal
import os
import sys
import time

#import native client which supports- system SSHAgent
from pssh.clients import ParallelSSHClient
from pssh.exceptions import Timeout


#command line arguments parser routine
def get_args():
    parser = argparse.ArgumentParser(
        description='Script retrieves ip address and command from commandline')

    # Add arguments
    parser.add_argument(
        '-ch', '--host', type=str, nargs='+',help='host', required=True)
    parser.add_argument(
        '-u', '--user', type=str, help='user')
    parser.add_argument(
        '-c', '--command', type=str, help='command', required=True)

    args= parser.parse_args()

    #Assign args to variables
    host = args.host[0].split(",")
    print(host)
    user=args.user
    command = args.command
    print(command)
    print(user)
    return host,user,command

#SIGINT handler routine
def interrupt_handler(sig, frame):
    sys.exit(0)

#register with the signal object to handle the SIGINT
signal.signal(signal.SIGINT, interrupt_handler)

host ,user,command = get_args()

#creating a native client object with system defined SSHAgent forwading
#using SSH publickey authentication to remote host
client = ParallelSSHClient(host,user,pkey='id_rsa')
output = client.run_command(command)
try:
  client.join(output)
except Timeout:
  pass

#keyboard interrupt of Ctrl+C is handled below
for  host, host_out in output.items():
  try:
    for line in host_out.stdout:
        print("Host [%s] -%s\n" % (host, line)) 
    for line in host_out.stderr:
        pass
  except Timeout:
        continue 
  except(KeyboardInterrupt, SystemExit):
        print('exit handled')
        os.kill(os.getpid(),3)
