#!/usr/bin/env python

#
# view-toggle-show-hide-layers.py is heavily based on view-unhide-all-layers.py
# (https://github.com/morevnaproject/synfig) by Konstantin Dmitriev Copyright (c) 2012.
#
# view-toggle-show-hide-layers.py is copyright <d.j.a.y> 2014.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

import os
import sys

def process(filename):

	# Read the input file
	inputfile_f = open(filename, 'r')
	inputfile_contents = inputfile_f.readlines()
	inputfile_f.close()

	# Now write results to the same file
	inputfile_f = open(filename, 'w')

	for line in inputfile_contents:
		if "<layer " in line:
			if ' active="false" ' in line:
				inputfile_f.write(line.replace(' active="false" ',' active="true" '))
			else:
				inputfile_f.write(line.replace(' active="true" ',' active="false" '))
		else:
			inputfile_f.write(line)
	inputfile_f.close()

if len(sys.argv) < 2:
	sys.exit()
else:
	process(sys.argv[1])

