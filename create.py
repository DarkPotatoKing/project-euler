import os
import sys

try:
    num = int(sys.argv[1])
    filename = 'problem_{}.py'.format(str(num).zfill(3))
    command = 'cp -n template.py {}'.format(filename)
    os.system(command)
except IndexError as e:
    print 'Error: Please enter a problem number.'
