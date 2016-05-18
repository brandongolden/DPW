"""
Brandon Golden
DPW
Reusable Library
5/18/16
"""
import webapp2
from lib import *  # Import all classes from lib.py
from page import FormPage  # Import FormPage class from page.py
from page import ResultsPage  # Import ResultsPage class from page.py

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage()  # Create instance of FormPage class
        r = ResultsPage()  # Create instance of ResultsPage class
        #  If form has been submitted then run this code
        if self.request.GET:

            # Create instances of Simoleons and Sim classes
            # Submit form input to classes
            s = Simoleons(self.request.GET['simoleons'])
            sim = Sim(self.request.GET['simName'], self.request.GET['hairColor'], self.request.GET['eyeColor'])

            # html body of results
            page = '''
            <div class="box">
            <b>Sim Name:</b> {sim.name}<br>
            </div>
            <div class="box">
            <b>Simoleons:</b> &sect;{s.simoleons}<br>
            </div>

            <div class="box">
            <b>Hair Color:</b> {sim.hair}<br>
            <img src="img/{sim.hair}.jpg"><br>
            </div>
            <div class="box">
            <b>Eye Color:</b> {sim.eyes}<br>
            <img src="img/{sim.eyes}.png">
            </div>
            '''

            page = page.format(**locals())  # Format { } local variables
            self.response.write(r.header + page + r.footer)  # Combine header page and footer html

        else:  # If form has not been submitted then display form
            self.response.write(f.form)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
