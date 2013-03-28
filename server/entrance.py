#!/usr/bin/python

import web,sys
sys.path.append("server")
sys.path.append("api")
sys.path.append("parser")

from hello import *
from bbsuser import *
from bbsboard import *
#from bbspost import *

urls = (
	'/bbsCheck', 'bbsCheck',
	'/bbsShowUsers', 'bbsShowUsers',
	'/bbsShowBoards', 'bbsShowBoards',
	'/bbsShowBoard', 'bbsShowBoard',
	'/', 'hello'
)
app = web.application(urls,globals())

if __name__ == "__main__":
	app.run()
