'''
Brandon Golden
'''
import webapp2

class MainHandler(webapp2.RequestHandler):
        def get(self):
            page_head = '''
            <DOCTYPE HTML>
            <html>
                <head>
                    <title>Simple Form</title>
                </head>
            <body>
            '''
            page_body = '''
            <form method="GET" action="">

            <label>Guitar Company: </label>
            <select name="guitar_company">
				<option value="Martin">Martin</option>
				<option value="Seagull">Seagull</option>
				<option value="Fender">Fender</option>
			</select>

			<label>Model: </label><input type="text" name="model" />

			<label>Strings: </label>
			<input type="radio" name="strings" value="6 String" checked>6 String<br>
			<input type="radio" name="strings" value="12 String"> 12 String

			<label>Condition: </label>
			<input type="radio" name="condition" value="New" checked> New<br>
			<input type="radio" name="condition" value="Used"> Used


			<label>Price: </label>
			<select name="price">
				<option value="<$500"><$500</option>
				<option value="$501-$899">$501-$899</option>
				<option value="$900>">$900></option>
			</select>

			<input type="submit" value="Submit" />
            </form>
            '''
            page_close = '''
            </body>
            </html>
            '''
            if self.request.GET:
                model = self.request.GET['model']
                guitar_company = self.request.GET['guitar_company']
                strings = self.request.GET['strings']
                condition = self.request.GET['condition']
                price = self.request.GET['price']
                self.response.write(page_head + model + ' ' + guitar_company + page_close)
            else:
                self.response.write(page_head + page_body + page_close)
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
