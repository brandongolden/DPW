import webapp2
from lib import *
from page import FormPage
from page import ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage()  # Create instance of FormPage class
        r = ResultsPage()  # Create instance of ResultsPage class



        if self.request.GET:
            s = Simoleons(self.request.GET['simoleons'])
            sim = Sim(self.request.GET['simName'], self.request.GET['hairColor'], self.request.GET['eyeColor'])

            page = '''
            <b>Sim Name:</b> {sim.name}<br>
            <b>Simoleons:</b> &sect;{s.simoleons}<br>
            <b>Hair Color:</b> {sim.hair}<br>
            <img src="img/{sim.hair}.jpg"><br>
            <b>Eye Color:</b> {sim.eyes}<br>
            <img src="img/{sim.eyes}.png">
            '''

            page = page.format(**locals())
            self.response.write(r.header + page + r.footer)

        else:
            self.response.write(f.form)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
