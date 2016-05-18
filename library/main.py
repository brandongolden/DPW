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
            sim = Sim(self.request.GET['simName'], self.request.GET['hairColor'])

            page = '''
            {sim.name}<br>
            {sim.hair}<br>
            {s.simoleons}
            '''

            page = page.format(**locals())
            self.response.write(r.header + page + r.footer)

        else:
            self.response.write(f.form)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
