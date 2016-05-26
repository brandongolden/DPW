'''
Brandon Golden
5/24/16
DPW
Dynamic Site
'''

# superclass Page
class Page(object):
    def __init__(self):

        # header that will be used on every page
        self._header = '''
        <!DOCTYPE html>
        <head>
            <title>Web Hosting</title>
        </head>
        <body>
        '''

        # html body that will show when GET request does not exist
        self._body = '''
        <a href="?webhost=dreamhost">DreamHost</a>
        <a href="?webhost=hostgator">HostGator</a>
        <a href="?webhost=site5">Site5</a>
        <a href="?webhost=godaddy">GoDaddy</a>
        <a href="?webhost=siteground">SiteGround</a>
        '''

        # footer that will be used on every page
        self._footer = '''
        </body>
        </html>
        '''

    # merge header, body and footer to make front page that will show when there is no GET request
    def front_page(self):
        return self._header + self._body + self._footer


# subclass of Page
class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()  # make super class
        self.company = ""
        self.logo_img = ""
        self.plan = ""
        self.price = ""
        self.disk_space = ""
        self.bandwidth = ""
        self.control_panel = ""
        self.domains = ""
        self._webhost_body = ""

        # html body that will show when a GET request exists
        # local variables match chosen webhost
        self._webhost_body = '''
        {self.company}
        {self.plan}
        {self.price}
        {self.disk_space}
        {self.bandwidth}
        {self.control_panel}
        {self.domains}
        '''

    # merge header, webhost_body and footer to make webpage for webhost
    def make_page(self):
        a = self._header + self._webhost_body + self._footer
        a = a.format(**locals())  # Format all local variables
        return a





