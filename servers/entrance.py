#!/usr/bin/python

import web,sys

import mimerender

sys.path.append("parsers")
sys.path.append("apis")
sys.path.append("servers")

from mimerenderheader import *
from bbsuser import bbsuser
from bbsallusers import bbsallusers
from bbscheck import bbscheck


urls = (
	'/bbsuser.*','bbsuser',
	'/bbsallusers.*','bbsallusers',
	'/bbscheck.*','bbscheck',
	'/(.*)', 'greet'
)
app = web.application(urls, globals())

class greet:
    @mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self, name):
        if not name: 
            name = 'world'
        return {'message': 'Hello, ' + name + '!'}

if __name__ == "__main__":
    app.run()

