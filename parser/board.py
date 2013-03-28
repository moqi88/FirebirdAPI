#coding: utf-8
#
# parse .BOARDS
# parse /boards/<board>/.DIR
# parse /boards/<board>/board.allow
#
# getBoards() 				boardname list
# getBoardsDetailed()		board dicts in a list
# getBoardDetailed(boardName)
# isBoard(boardName)		bool
# isKBoard(boardName)		bool(please make sure whether board exist)
# isInBoard(username,boardName)
#                           bool(please make sure whether board exist)
# getPostsList(boardName)	list(please make sure whether board exist)
#


import struct
import sys
import os
import functions

boardFolder	=	"/home/bbs/bbshome/boards/"

boardFilePath = "/home/bbs/bbshome/.BOARDS"
#boardFilePath = os.getcwd()+"/BOARDS"
BOARDSstruct =	["76s",		"i",		"20s",		"56s",	"3s",		"c",		"80s",		"I",		"12s"		]
BOARDSorder =	["filename",	"group",	"owner",	"BM",	"flag2",	"flag",		"title",	"level",	"accessed"	]

DIRstruct 	=	["80s",		"76s",		"I",	"80s",		"I",		"4s",		"I",	"I"		]
order		=	["filename",	"owner",	"pnum",	"title",	"level",	"accessed",	"id",	"reid"	]
def getBoards():
	boards = []
	for i in _getDetailedBoards():
		nm = i["filename"]
		for j in range(len(nm)):
			if nm[j] == '\0':
				nm = nm[:j]
				break
		len(nm) and boards.append(nm)
	return boards

def getBoardsByUser(user):
	aboards = getBoards()
	boards = []
	for i in aboards:
		if not isKBoard(i) or isInBoard(user,i):
			boards.append(i)
	return boards

def getBoardsDetailed():
	return _getDetailedBoards()

def getBoardsDict():
	l =  _getDetailedBoards()
	d = {}
	for i in l:
		d[i["filename"]] = i
	return d
	
def getBoardDetailed(boardName):
	for i in _getDetailedBoards():
		if i["filename"] == boardName:
			return i
	return False

def getBoardChineseName(boardName):
	c = getBoardDetailed(boardName)["title"]
	if(c[11] == " "):
		b = 12
	elif(c[12] == " "):
		b = 13
	elif(c[13] == " "):
		b = 14
	elif(c[14] == " "):
		b = 15
	else:
		b = 11
	return c[b:]

def isBoard(boardName):
	return boardName in getBoards()

def isKBoard(boardName):
	return _hasAllowFile(boardName)
	
def isInBoard(username, boardName):
	return username in _getAllowList(boardName)
	
def getPostsList(boardName):
	return _getFileHeaders(boardName)
	
def _getFileHeaders(boardName):
	f = open(boardFolder + boardName+ os.path.sep +".DIR","rb")
	#print boardFolder + boardName+ os.path.sep +".DIR"
	data = f.read()
	data = functions.parseStruct(DIRstruct,order,256,data)
	f.close()
	return data

def prettyPrintFileList(boardName):
	fl = []
	dfl = _getFileHeaders(boardName)
	for i in range(len(dfl)):
		owner = dfl[i]["owner"]
		title = dfl[i]["title"]
		filename = dfl[i]["filename"]
		
		info = str(i).ljust(6) + filename[0:18]  + owner.ljust(14) + title.ljust(10)
		fl.append(info)
	return fl
	
def _hasAllowFile(boardName):
	return os.path.exists( boardFolder + boardName +  os.path.sep + "board.allow" )

def _getAllowList(boardName):
	if not _hasAllowFile(boardName):
		return []
	f = open(boardFolder + boardName + os.path.sep +"board.allow","rb")
	ul = filter(None,f.read().split("\n"))
	return ul

def _getDetailedBoards():
	f = open(boardFilePath)
	data = f.read()
	dataout = functions.parseStruct(BOARDSstruct,BOARDSorder,256,data)
	f.close()
	return dataout

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "\t".join([len(i) > 7 and i or i + "\t" for i in getBoards()])
	elif len(sys.argv) == 2:
		b = getBoardDetailed(sys.argv[1])
		print "\n".join([ (len(i)> 7 and i + "\t:" or i + "\t\t:") + str(b[i]) for i in b ])
	elif len(sys.argv) == 3:
		l = prettyPrintFileList(sys.argv[1])
		l = [ l[i] for i in range( len(l) > int(sys.argv[2]) and len(l) - int( sys.argv[2]) or 0, len(l) )]
		print "\n".join(l)
