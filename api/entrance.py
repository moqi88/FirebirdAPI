import web

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
