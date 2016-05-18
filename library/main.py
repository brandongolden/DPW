import webapp2
from lib import *
from page import FormPage
from page import ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):
        f = FormPage() #Create instance of FormPage class
        r = ResultsPage() #Create instance of ResultsPage class



        if self.request.GET:
            self.response.write('Form sent')
        else:
            self.response.write(f.form)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
