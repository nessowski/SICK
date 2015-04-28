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
import time
import string
import platform
import socket
import ConfigParser
from sys import stdout as stdout

sys.path.append("lib")
from termcolor import *

import draw


VERSION = "SICK alpha v0.0.2"
OS = platform.system() + " " + platform.release()
CONNECTION = socket.socket()
CONNECTED = False

BUFF = ""
settings = None

HEIGHT, WIDTH = os.popen('stty size', 'r').read().split()

class Settings(object):
    def __init__(self, MAINnick, MAINuser, MAINreal):
        self.MAINnick = MAINnick
        self.MAINuser = MAINuser
        self.MAINreal = MAINreal

def main():
    global BUFF, CONNECTION
    loadConfig()
    stdout.write( "Welcome to " )
    stdout.write( colored("SICK", "green" ) )
    stdout.write( ", the client so sick it might make you toss your cookies.\n" )
    # Splash thing here.
    stdout.write( "For help, type help." )
    while True:
		try:
			newInput = raw_input("\n> ")
		except:
			pass
		else:
			if newInput == "help":
				print( "Most important commands:")
				print( "\tserver <ip> <port> [ssl=False] - Connects to a server" )
				print( "\tcommands - Displays a list of all commands" )
				print( "\texit - Exits SICK (don't use this one)" )
			elif newInput == "exit":
				print( "SICK is going down NOW!" )
				time.sleep(1)
				sys.exit()
		
		if CONNECTED:
			pass
		else:
			pass

def connect(ip, port, ssl=False):
    global CONNECTION

    if not ssl:
        CONNECTION.connect((ip, port))
        CONNECTION.send("NICK %s\r\n" % settings.MAINnick)
        CONNECTION.send("USER %s %s null :%s\r\n" % (settings.MAINuser, ip, settings.MAINreal) )

def loadConfig():
    global settings

    configParser = ConfigParser.RawConfigParser()
    configFilePath = "sick.conf"
    configParser.read(configFilePath)
    settings = Settings( configParser.get("main", "nick"), configParser.get("main", "user"), configParser.get("main", "real") )

if __name__ == "__main__":

    draw.drawtopbar(WIDTH)

    main()

#EOF
