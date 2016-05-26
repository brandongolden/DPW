'''
Brandon Golden
5/24/16
DPW
Dynamic Site
'''
import webapp2
from data import *
from page import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        if self.request.GET:

            if self.request.GET["id"] == "1":
                pass
            elif self.request.GET["id"] == "2":
                pass
            elif self.request.GET["id"] == "3":
                pass
            elif self.request.GET["id"] == "4":
                pass
            elif self.request.GET['id'] == "5":
                pass



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
