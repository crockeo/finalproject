#!/usr/bin/python

#
# Entrance point to Crocode
#

# For checking the arguments
import sys

# For interpreting
import Interactive
import File

if len(sys.argv) > 2: print "Proper usage: crocode (<file location>)"
elif len(sys.argv) == 2: File.fload(sys.argv[1])
else: Interactive.interactive()
