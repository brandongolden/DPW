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
            webhost = self.request.GET['webhost']

            if webhost == "dreamhost":
                w = d.webhosts_array[0]
                c.company = w.company
                c.logo_img = w.logo_img
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains

            elif webhost == "hostgator":
                w = d.webhosts_array[1]
                c.company = w.company
                c.logo_img = w.logo_img
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains

            elif webhost == "site5":
                w = d.webhosts_array[2]
                c.company = w.company
                c.logo_img = w.logo_img
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains

            elif webhost == "godaddy":
                w = d.webhosts_array[3]
                c.company = w.company
                c.logo_img = w.logo_img
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains

            elif webhost == "siteground":
                w = d.webhosts_array[4]
                c.company = w.company
                c.logo_img = w.logo_img
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains


            # Show custom page using info above
            self.response.write(c.make_page())

        else:
            # Show front page if GET does not exist
            self.response.write(p.front_page())
            # self.response.write("No GET found")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
