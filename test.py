import getopt
import errno
import sys
import os

# print('sys.argv[0] =', sys.argv[0])             
# pathname = os.path.dirname(sys.argv[0])        
# print('path =', pathname)
# print('full path =', os.path.abspath(pathname)) 

# raise FileNotFoundError()
version = '1.0'
verbose = False
output_filename = 'default.out'


print('ARGV      :', sys.argv[1:])
# print(getopt.getopt(sys.argv[1:], 'o:v', ['output=',
                                        #   'verbose',
                                        #   'version=',
                                        #   ]))
options, remainder = getopt.getopt(sys.argv[1:], 'o:v', ['output=',
                                                         'verbose',
                                                         'version=',
                                                         ])
print("options:", options)
print("remainder:", remainder)


print('OPTIONS   :', options)
for opt, arg in options:
    if opt in ('-o', '--output'):
        output_filename = arg
    elif opt in ('-v', '--verbose'):
        verbose = True
    elif opt == '--version':
        version = arg

print()
print('VERSION   :', version)
print('VERBOSE   :', verbose)
print('OUTPUT    :', output_filename)
print('REMAINING :', remainder)
