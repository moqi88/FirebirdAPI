import sys
import passwd,functions
import web

def checkPasswd():
	data=web.input()
	if "user" in data and "pw" in data:
		return passwd.checkPasswd(data.user,data.pw)
	else:
		return False

class bbsCheck:
	def GET(self):
		return str(checkPasswd())	
	def POST(self):
		return self.GET()

class bbsShowUsers:
	def GET(self):
		if not checkPasswd():
			return "Not Logged in"
		users = passwd.getUsers()
		return str(users)
	def POST(self):
		return self.GET()


