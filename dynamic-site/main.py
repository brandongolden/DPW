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
        p = Page()

        if self.request.GET:

            if self.request.GET["id"] == "1":
                webhost = d.webhosts_array[0]

            elif self.request.GET["id"] == "2":
                webhost = d.webhosts_array[1]

            elif self.request.GET["id"] == "3":
                webhost = d.webhosts_array[2]

            elif self.request.GET["id"] == "4":
                webhost = d.webhosts_array[3]

            elif self.request.GET['id'] == "5":
                webhost = d.webhosts_array[4]

            c.company = webhost.company
            c.logo_img = webhost.logo_img
            c.plan = webhost.plan
            c.price = webhost.price
            c.disk_space = webhost.disk_space
            c.bandwidth = webhost.bandwidth
            c.control_panel = webhost.control_panel
            c.domains = webhost.domains

            # Show custom page using info above
            self.response.write(c.make_page())

        else:
            # Show front page if GET does not exist
            self.response.write(p.front_page())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
