#!/usr/bin/env python
"""Example of DocOpt

Usage:
  docopt_example.py (-h | --help)
  docopt_example.py --version
  docopt_example.py aws [--az=<az>] [--sg=<sg>] [--ssh_user=<sshuser>] [--ssh_key=<sshkey>] [--instance_type=<instance_type>] [--ami_id=<ami_id>] [--roles=<roles> ...] 
  docopt_example.py azure [--roles=<roles> ...] 
  docopt_example.py digitalocean [--roles=<roles> ...] 

Options:
  -h --help     		Show this screen.
  --az=availability zone  	AWS availability zone  		[default: US-EAST-1A]
  --sg=securitygroup  		AWS security group  		[default: mvco-0]
  --ssh_user=ssh_user 		SSH user account name  		[default: ubuntu]
  --ssh_key=ssh_key 		SSH private key name  		[default: mvco-0]
  --inst_type=intst_type 	AWS instance type  		[default: m1.small]
  --ami_id=ami_id 		AWS ami id  			[default: ami-a73264ce]
  --roles=csv of roles 		Roles to apply to new node  	[default: a,b,c]
  --version     		Show version.


"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)
