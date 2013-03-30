import web,sys,mimerender

import passwd

try:
    import simplejson as json
except ImportError:
    import json

mimerender = mimerender.WebPyMimeRender()

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda **args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
render_html = render_json
render_txt = lambda message: message



errors = {
	"no_error"	:{"no":0,"error":""},

	"wrong_passwd"	:{"no":1001,"error":"invalid username or passwd"},
	"wrong_id"	:{"no":1002,"error":"invalid user"},

	"require_id":{"no":2001,"error":"id is required"},
}

def checkPasswd():
	web.header('content-type','text/html;charset=utf-8',unique=True)
	data=web.input()
	if "user" in data and "pw" in data:
		return passwd.checkPasswd(data.user,data.pw)
	else:
		return False
