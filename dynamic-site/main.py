'''
Brandon Golden
5/24/16
DPW
Dynamic Site
'''

import webapp2
from data import *  # Import all classes from data.py
from page import *  # Import all classes from page.py

class MainHandler(webapp2.RequestHandler):
    def get(self):

        # Make instances of Data, ContentPage and Page classes
        d = Data()
        c = ContentPage()
        p = Page()

        if self.request.GET:  # If there is a GET request run this code
            webhost = self.request.GET['webhost']  # Set webhost to the value of the GET request

            if webhost == "dreamhost":  # If the value of the GET request is dreamhost run this code
                w = d.webhosts_array[0]  # Select dreamhost from the webhosts_array

                # Retrieve attributes that match webhost chosen in GET request
                c.company = w.company
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains

            elif webhost == "hostgator":  # If the value of the GET request is hostgator run this code
                w = d.webhosts_array[1]  # Select hostgator from the webhosts_array

                # Retrieve attributes that match webhost chosen in GET request
                c.company = w.company
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains

            elif webhost == "site5":  # If the value of the GET request is site5 run this code
                w = d.webhosts_array[2]  # Select site5 from the webhosts_array

                # Retrieve attributes that match webhost chosen in GET request
                c.company = w.company
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains

            elif webhost == "godaddy":  # If the value of the GET request is godaddy run this code
                w = d.webhosts_array[3]  # Select godaddy from the webhosts_array

                # Retrieve attributes that match webhost chosen in GET request
                c.company = w.company
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains

            elif webhost == "siteground":  # If the value of the GET request is siteground run this code
                w = d.webhosts_array[4]  # Select siteground from the webhosts_array

                # Retrieve attributes that match webhost chosen in GET request
                c.company = w.company
                c.plan = w.plan
                c.price = w.price
                c.disk_space = w.disk_space
                c.bandwidth = w.bandwidth
                c.control_panel = w.control_panel
                c.domains = w.domains


            # Show custom page using selected info above
            self.response.write(c.make_page())

        else:
            # Show front page if GET does not exist
            self.response.write(p.make_page())
            # self.response.write("No GET found")

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
