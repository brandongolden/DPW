'''
Brandon Golden
5/24/16
DPW
Dynamic Site
'''

class Page(object):
    def __init__(self):
        self.header = '''
        <!DOCTYPE html>
        <head>
            <title>Dynamic Site</title>
        </head>
        <body>
        '''

        self.body = ""

        self.footer = '''
        </body>
        </html>
        '''