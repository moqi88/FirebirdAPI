import sys,web,mimerender
import passwd,functions,PERM

from mimerenderheader import *

class bbsallusers:
    @mimerender(default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self):
        if checkPasswd() != True:
            return {"message":errors["wrong_passwd"]}
        else:
            users = []
            userList = passwd.getUsers()
            for u in userList:
                users.append({
                    "userid":passwd.getAttr(u,"userid"),
                    "username":passwd.getAttr(u,"username"),
                    "userid":passwd.getAttr(u,"userid"),
                    "lastlogin":passwd.getAttr(u,"lastlogin"),
                    "lastlogout":passwd.getAttr(u,"lastlogout")
                })
        return {"message":users}
