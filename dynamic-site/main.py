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
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
