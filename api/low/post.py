#coding: utf-8
#
# getPostRaw
# getPostNoCT
# getPostInTag (TBD)
#
# scaret Email:  i @ scaret.in
# This api don't offer function like "getPostInDict" because it's a low-level
#     api, and a file string is regarded as the basic element.

import struct
import sys
import os
import functions
import re

boardFolder	=	"/home/bbs/bbshome/boards/"

def getPostRaw(boardName,filename):
	filename = filename[:14]
	f = open(boardFolder + boardName + os.path.sep + str(_getFileMapNum(filename)) + os.path.sep + filename)
	content = f.read()
	f.close()
	return content
	
def getPostNoCT(boardName,filename):
	filename = filename[:14]
	c = getPostRaw(boardName,filename)
	return functions.filterCT(c)

	
def _getFileMapNum(filename):
	return int(filename[-5]) < 5 and filename[-5:-2] or str(int(filename[-5])-5)+filename[-4:-2]
	
def _parsePost(str):
	pass

	
if __name__ == "__main__":
	print getPostRaw("comment","M.1348294481.A")
