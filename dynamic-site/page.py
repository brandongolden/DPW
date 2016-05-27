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
            <link rel="stylesheet" href="main.css">
            <link href='https://fonts.googleapis.com/css?family=Cuprum:400,700' rel='stylesheet' type='text/css'>
        </head>
        <body>
        '''

        # html body that will show when GET request does not exist
        self._body = '''
        <section>
            <h1>Web Hosting</h1>
            <article>
                <a href="?webhost=dreamhost"><h2>DreamHost</h2></a>
                <p>DreamHost is a Los Angeles-based web hosting provider and domain name registrar. It is the web hosting and cloud computing business owned by New Dream Network, LLC, founded in 1996 by Dallas Bethune, Josh Jones, Michael Rodriguez and Sage Weil, undergraduate students at Harvey Mudd College in Claremont, California, and registered in 1997 by Michael Rodriguez.[2][3] DreamHost began hosting customers' sites in 1997.[4] In May 2012, DreamHost spun off Inktank.[5] Inktank is a professional services and support company for the open source Ceph file system.[6] In November 2014, DreamHost spun off Akanda, an open source network virtualization solution.[7]</p>
                <a href="https://en.wikipedia.org/wiki/DreamHost">https://en.wikipedia.org/wiki/DreamHost</a>
            </article>
            <article>
                <a href="?webhost=hostgator"><h2>HostGator</h2></a>
                <p>HostGator is a Houston-based provider of shared, reseller, virtual private server, and dedicated web hosting with an additional presence in Austin, Texas.[3][4]</p>
                <a href="https://en.wikipedia.org/wiki/HostGator">https://en.wikipedia.org/wiki/HostGator</a>
            </article>
            <article>
                <a href="?webhost=site5"><h2>Site5</h2></a>
            </article>
            <article>
                <a href="?webhost=godaddy"><h2>GoDaddy</h2></a>
                <p>GoDaddy is a publicly traded Internet domain registrar and web hosting company.[4] As of January 2016, GoDaddy was said to have had more than 61 million domain names under management, making it the world's largest ICANN-accredited registrar. It serves more than 13 million customers and employs more than 4,000 people.[5] The company is known for its celebrity spokespeople, Super Bowl ads and as being an online provider for small businesses. In addition to a postseason college football bowl game, it previously sponsored NASCAR. It has been involved in several controversies related to security and privacy. In addition to domain registration and hosting, GoDaddy also sells e-business related software and services.</p>
                <a href="https://en.wikipedia.org/wiki/GoDaddy">https://en.wikipedia.org/wiki/GoDaddy</a>
            </article>
            <article>
                <a href="?webhost=siteground"><h2>SiteGround</h2></a>
                <p>SiteGround is a web hosting company founded in 2004 and servicing more than 450,000 domains world-wide. It provides shared hosting, cloud hosting and dedicated servers. Currently, the company employs over 315 people.[2]</p>
                <a href="https://en.wikipedia.org/wiki/SiteGround">https://en.wikipedia.org/wiki/SiteGround</a>
            </article>
        </section>
        '''

        # footer that will be used on every page
        self._footer = '''
        <footer>
            <a href="http://www.fatcow.com/free-icons">Free Icons</a> | Brandon Golden
        </footer>
        </body>
        </html>
        '''

    # merge header, body and footer to make front page that will show when there is no GET request
    def make_page(self):
        return self._header + self._body + self._footer


# subclass of Page
class ContentPage(Page):
    def __init__(self):
        super(ContentPage, self).__init__()  # make super class
        self.company = ""

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
        <section>
        <h1>{self.company}</h1>
        <img src="img/package.png">
        <b>Plan:</b> {self.plan}<br>

        <img src="img/total_plan_cost.png">
        <b>Price:</b> {self.price}<br>

        <img src="img/disk_space.png">
        <b>Disk Space:</b> {self.disk_space}<br>

        <img src="img/limit_bandwidth_usage.png">
        <b>Bandwidth:</b> {self.bandwidth}<br>

        <img src="img/control_panel_access.png">
        <b>Control Panel:</b> {self.control_panel}<br>

        <img src="img/domain_names_advanced.png">
        <b>Domains:</b> {self.domains}
        </section>
        '''

    # merge header, webhost_body and footer to make webpage for webhost
    # Polymorphism happening here
    def make_page(self):
        a = self._header + self._webhost_body + self._footer
        a = a.format(**locals())  # Format all local variables
        return a