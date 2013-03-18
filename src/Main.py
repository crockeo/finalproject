#!/usr/bin/python

#
# Entrance point to Crocode
#

# For checking the arguments
import sys

# For interpreting
import Interactive
import File

# Error handling
def err(val):
    pass

if len(sys.argv) > 2: print "Proper usage: crocode (<file location>)"
elif len(sys.argv) == 2: val = File.fload(sys.argv[1])
else: val = Interactive.interactive()

if not val: err(val)
else: print "G'day mate."
