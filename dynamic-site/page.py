'''
Brandon Golden
5/24/16
DPW
Dynamic Site
'''

class Page(object):
    def __init__(self):
        self.__title = "Dynamic Site"
        self.__header = '''
        <!DOCTYPE html>
        <head>
            <title>{self.title}</title>
        </head>
        <body>
        '''

        self.__body = ""

        self.__footer = '''
        </body>
        </html>
        '''


        @property
        def title(self):
            return self.__title
        @title.setter
        def title(self, change_title):
            self.__title = change_title

        @property
        def header(self):
            return self.__header

        @property
        def body(self):
            return self._body
        @body.setter
        def body(self, change_body):
            self.__body = change_body


        def make_page(self):
            self.html = self.header + self.body + self.footer
            self.html = self.html.format(**locals())
            return self.html

class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()


