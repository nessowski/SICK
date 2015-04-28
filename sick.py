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
import threading
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
    print( "For help, type help." )
    inputThread = SICKinput()
    inputThread.start()


def connect(ip, port, ssl=False):
    global CONNECTION, CONNECTED
    
    CONNECTED = True

    if not ssl:
        CONNECTION.connect( (ip, int(port) ) )
    
	#time.sleep(3)
	CONNECTION.send("NICK %s\r\n" % settings.MAINnick)
	CONNECTION.send("USER %s %s null :%s\r\n" % (settings.MAINuser, ip, settings.MAINreal) )

class SICKinput( threading.Thread ):
	def run( self ):
		while True:
			try:
				newInput = raw_input( colored("> ", "yellow") )
			except:
				pass
			else:
				if newInput.startswith( "help" ):
					print( "Most important commands:")
					print( "\tserver <address> <port> [ssl=False] - Connects to a server (SSL will be implemented later)" )
					print( "\tcommands - Displays a list of all commands" )
					print( "\texit - Exits SICK (don't use this one: the ride never ends)" )
				elif newInput.startswith( "exit" ):
					print( "SICK is going down NOW!" )
					time.sleep(1)
					# TO MOTHERFUCKING DO

				elif newInput.startswith( "commands" ):
					print( "All commands: \n\thelp \n\tcommands \n\tserver \n\tjoin <channel> \n\ts <message> \n\tcs <channel> <message> \n\texit" )
				elif newInput.startswith( "server" ):
					listed = newInput.split( " " )
					try:
						listed[1]
					except:
						print( colored( "ER-002: No server address specified.", "green" ) )
					else:
						try:
							listed[2]
						except:
							print( colored( "ER-001: No server port specified.", "green" ) )
						else:
							connect( listed[1], listed[2] )
							
							outputThread = SICKoutput()
							outputThread.start()
				elif newInput.startswith( "join" ):
					listed = newInput.split( " " )
					try:
						listed[1]
					except:
						print( colored( "ER-004: No channel specified.", "green" ) )
					else:
						if not listed[1].startswith( "#" ):
							CONNECTION.send( "JOIN %s" % listed[1] )
						else:
							CONNECTION.send( "JOIN #%s" % listed[1] )
				else:
					print( colored( "ER-003: Unknown command.", "green" ) )

class SICKoutput( threading.Thread ):
	def run( self ):
		while True:
			if CONNECTED:
				get = CONNECTION.recv(2048)
				if get.startswith( "PING" ):
					get.split( " " )
					CONNECTION.send( "PONG %s" % get[1] )
				print get


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
