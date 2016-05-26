'''
Brandon Golden
5/24/16
DPW
Dynamic Site
'''

class Page(object):
    def __init__(self):
        self._header = '''
        <!DOCTYPE html>
        <head>
            <title>Web Hosting</title>
        </head>
        <body>
        '''

        self._body = '''
        <a href="?webhost=dreamhost">DreamHost</a>
        <a href="?webhost=hostgator">HostGator</a>
        <a href="?webhost=site5">Site5</a>
        <a href="?webhost=godaddy">GoDaddy</a>
        <a href="?webhost=siteground">SiteGround</a>
        '''

        self._footer = '''
        <br>
        &copy;2016 Brandon Golden
        </body>
        </html>
        '''

    def front_page(self):
        return self._header + self._body + self._footer



class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()
        self.company = ""
        self.logo_img = ""
        self.plan = ""
        self.price = ""
        self.disk_space = ""
        self.bandwidth = ""
        self.control_panel = ""
        self.domains = ""
        self._webhost_body = ""

        self._webhost_body = '''
        <h1>{self.plan}</h1>
        Test
        '''

    def make_page(self):
        a = self._header + self._webhost_body + self._footer
        a = a.format(**locals())
        return a





