#!/usr/bin/python3

import os, sys, subprocess

subprocess.check_call(['/bin/bash', '-c', 
                       'sudo apt-get purge --yes jenkins'])
subprocess.check_call(['/bin/bash', '-c', 
                       'sudo apt-get update -qq'])
subprocess.check_call(['/bin/bash', '-c', 
                       'sudo apt-get install --yes jenkins'])
subprocess.check_call(['/bin/bash', '-c', 
  '{0} {1}'.format(
    '/home/vagrant/permission.sh',
    '$(id -gn)')])
subprocess.check_call(
  ['/bin/bash',
   '/home/vagrant/run.sh',
   'false',
   'true'])
