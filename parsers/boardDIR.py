import struct
import sys
import os
import functions

boardFolder	=	"/home/bbs/bbshome/boards/"

DIRstruct 	=	["80s",		"76s",		"I",	"80s",		"I",		"4s",		"I",	"I"		]
order		=	["filename",	"owner",	"pnum",	"title",	"level",	"accessed",	"id",	"reid"	]


def getPostsList(boardName):
	return _getFileHeaders(boardName)

def _getFileHeaders(boardName):
	if boardName == "":
		return []
	try:
		f = open(boardFolder + boardName +"/.DIR","rb")
	#print boardFolder + boardName+ os.path.sep +".DIR"
	except:
		return []
	data = f.read()
	data = functions.parseStruct(DIRstruct,order,256,data)
	f.close()
	for thePost in data:
		endflag = thePost["filename"].find("\0")
		if endflag != -1:
			thePost["filename"] = thePost["filename"][0:endflag]
	return data
