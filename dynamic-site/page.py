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

class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()
