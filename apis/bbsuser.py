import sys,web,mimerender
import passwd,functions,PERM

from mimerenderheader import *

class bbsuser:
    @mimerender(default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        if checkPasswd() != True:
            return {"message":errors["wrong_passwd"]}
        elif "id" not in web.input():
            return {"message":errors["require_id"]}
        elif web.input()["id"] not in passwd.getUsers():
            return {"message":errors["wrong_id"]}
        else:
            userid = web.input()["id"]
            return {"message":{
		"userid":userid,
		"username":passwd.getAttr(userid,"username"),
		"gender":passwd.getAttr(userid,"gender"),
		"birthmonth":passwd.getAttr(userid,"birthmonth"),
		"birthday":passwd.getAttr(userid,"birthday"),
		"firstlogin":passwd.getAttr(userid,"firstlogin"),
		"lasthost":passwd.getAttr(userid,"lasthost"),
		"numlogins":passwd.getAttr(userid,"numlogins"),
		"money":passwd.getAttr(userid,"money"),
		"lastlogin":passwd.getAttr(userid,"lastlogin"),
		"lastlogout":passwd.getAttr(userid,"lastlogout"),
		"stay":passwd.getAttr(userid,"stay"),
		"level":PERM.levels(passwd.getAttr(userid,"userlevel"))

}}
