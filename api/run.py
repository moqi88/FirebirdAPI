#!/usr/bin/python

import os

path = os.getcwd()
print "Current DIR:",path

cmd = "gcc -o low/checkPasswd low/checkPasswd.c"
print "Compiling:" , cmd
os.system(cmd)

export = 'export PATH="$PATH:' + path + '/low"'
print "EXPORTING:" + export
os.system(export)

export = 'export PATH="$PATH:' + path
print "EXPORTING:" + export
os.system(export)

workingdir = "/home/bbs/bbshome"
print "Changing dir to:",workingdir
os.chdir(workingdir)

os.system("python "+ path +"/entrance.py")
