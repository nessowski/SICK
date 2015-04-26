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
    connect("irc.romhackersonline.com", 6667, ssl=False)
    while True:
        BUFF += CONNECTION.recv(2048)
        temp = string.split(BUFF, "\n")
        readbuffer = temp.pop()
        print readbuffer
        try:
            newi = raw_input() 
        except:
            pass

def connect(ip, port, ssl=False):
    global CONNECTION

    if not ssl:
        CONNECTION.connect((ip, port))
        CONNECTION.send("NICK %s\r\n" % settings.MAINnick)
        CONNECTION.send("USER %s %s null %s\r\n" % (settings.MAINuser, ip, settings.MAINreal) )

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
