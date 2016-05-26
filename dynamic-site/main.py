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

        d = Data()
        c = ContentPage()


        if self.request.GET:

            if self.request.GET["id"] == "1":
                webhost = d.dh
                c.title = webhost.company
                self.response.write(c.make_page())

            elif self.request.GET["id"] == "2":
                webhost = d.hg
                c.title = webhost.company
                self.response.write(c.make_page())

            elif self.request.GET["id"] == "3":
                webhost = d.s5
                c.title = webhost.company
                self.response.write(c.make_page())

            elif self.request.GET["id"] == "4":
                webhost = d.gd
                c.title = webhost.company
                self.response.write(c.make_page())

            elif self.request.GET['id'] == "5":
                webhost = d.sg
                c.title = webhost.company
                self.response.write(c.make_page())

        else:
            self.response.write(c.front_page())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
