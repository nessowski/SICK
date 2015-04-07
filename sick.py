#!/usr/bin/python
# coding=utf-8
#
# SICK is an IRC client.
# Please refer to README.md for more details.
#
# This file is released under the GNU General Public License v2.0,
# of which you should have received a copy with your download.
# If not, you can obtain a copy at http://www.gnu.org/licenses/gpl-2.0.txt
#
# Author: Marnix "Weloxux" Massar <weloxux@glowbug.nl>

import os
import sys
import platform
import socket
import ConfigParser
from sys import stdout as stdout

sys.path.append("lib")
from termcolor import *


VERSION = "SICK alpha v0.0.1a"
OS = platform.system() + " " + platform.release()
CONNECTION = socket.socket()

HEIGHT, WIDTH = os.popen('stty size', 'r').read().split()

class Settings(object):
    def __init__(self, MAINnick, MAINuser, MAINreal):
        self.MAINnick = MAINnick
        self.MAINuser = MAINuser


def connect(ip, port ssl=False):
    global CONNECTION

    if not ssl:
        s.connect(ip, port)
        s.send(
    

def drawtopbar(width):

	# First line:
	mline("top", width)

	# Second line:
	stdout.write( colored("║", "red", attrs=["dark"] ) )
	beginwriting = ( int(WIDTH) / 2 ) - ( VERSION.__len__() ) - 2

	i = 0
	
	while i < int(width):
		if i < beginwriting:
			stdout.write(" ")
		elif i == beginwriting:
			stdout.write( colored( VERSION + " ║ " + OS, "red", attrs=["dark"] ) )
			i += VERSION.__len__() + OS.__len__() + 4
		elif i >= int(width):
			pass #This can probably be done nicer
		else:
			stdout.write(" ")
		i += 1
	
	stdout.write( colored("║", "red", attrs=["dark"] ) )

	# Third line:
	mline("bot", width)

def mline(loc, width):
	if loc = "top":
		chars = ["╔", "╦", "╗"]
	elif loc = "bot":
		chars = ["╚", "╩", "╝"]

        stdout.write( colored(chars[0], "red", attrs=["dark"] ) )

        for i in xrange(int(width) - 2):
                mid = int(width) / 2 - 1
                if i != mid:
                        stdout.write( colored("═", "red", attrs=["dark"] ) )
                else:
                        stdout.write( colored(chars[1], "red", attrs=["dark"] ) )

        stdout.write( colored(chars[2], "red", attrs=["dark"] ) )

def main():
	while True:
            pass

def loadconfig():
    configParser = ConfigParser.RawConfigParser()
    configFilePath = "sick.conf"


if __name__ == "__main__":
	drawtopbar(WIDTH)

	main()

#EOF
