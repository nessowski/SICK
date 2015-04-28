#!/usr/bin/python
# coding=utf-8
#
# Draw module for SICK
# Please refer to README.md for more details.
#
# This file is released under the GNU General Public License v2.0,
# of which you should have received a copy with your download.
# If not, you can obtain a copy at http://www.gnu.org/licenses/gpl-2.0.txt
#
# Author: Marnix "Weloxux" Massar <weloxux@glowbug.nl>

import os
import sys
from sys import stdout as stdout

sys.path.append("lib")
from termcolor import *

from sick import VERSION as VERSION
from sick import OS as OS

def drawtopbar(width):

	# First line:
	mline("top", width)

	# Second line:
	stdout.write( colored("║", "yellow" ) )
	beginwriting = ( int(width) / 2 ) - ( VERSION.__len__() ) - 2

	i = 0
	
	while i < int(width):
		if i < beginwriting:
			stdout.write(" ")
		elif i == beginwriting:
			stdout.write( colored( VERSION + " ║ " + OS, "yellow" ) )
			i += VERSION.__len__() + OS.__len__() + 4
		elif i >= int(width):
			pass # This can probably be done nicer
		else:
			stdout.write(" ")
		i += 1
	
	stdout.write( colored("║", "yellow" ) )

	# Third line:
	mline("bot", width)

def mline(loc, width):
	if loc == "top":
		chars = ["╔", "╦", "╗"]
	elif loc == "bot":
		chars = ["╚", "╩", "╝"]

        stdout.write( colored(chars[0], "yellow" ) )

        for i in xrange(int(width) - 2):
                mid = int(width) / 2 - 1
                if i != mid:
                        stdout.write( colored("═", "yellow" ) )
                else:
                        stdout.write( colored(chars[1], "yellow" ) )

        stdout.write( colored(chars[2], "yellow" ) )

        stdout.flush()
