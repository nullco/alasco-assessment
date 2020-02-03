import json
import tornado

class ConvertViewHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('convert.html')