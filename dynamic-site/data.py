'''
Brandon Golden
5/24/16
DPW
Dynamic Site
'''


class WebHost(object):
    def __init__(self):
        self.company = ""
        self.logo_img = ""
        self.plan = ""
        self.price = ""
        self.disk_space = ""
        self.bandwidth = ""
        self.control_panel = ""
        self.domains = ""
        self.id = 0

class Data(object):
    def __init__(self):
        self.dh = WebHost()
        self.dh.company = "DreamHost"
        self.dh.logo_img = ""
        self.dh.plan = "Month-to-Month"
        self.dh.price = "$10.95/mo"
        self.dh.disk_space = "Unlimited"
        self.dh.bandwidth = "Unlimited"
        self.dh.control_panel = "DreamHost panel"
        self.dh.domains = "Unlimited"
        self.dh.id = 1

        self.hg = WebHost()
        self.hg.company = "HostGator"
        self.hg.logo_img = ""
        self.hg.plan = "Baby"
        self.hg.price = "$11.95/mo"
        self.hg.disk_space = "Unlimited"
        self.hg.bandwidth = "Unlimited"
        self.hg.control_panel = "cPanel"
        self.hg.domains = "Unlimited"
        self.hg.id = 2

        self.s5 = WebHost()
        self.s5.company = "Site5"
        self.s5.logo_img = ""
        self.s5.plan = "hostPro"
        self.s5.price = "$10.95/mo"
        self.s5.disk_space = "Unlimited"
        self.s5.bandwidth = "Unlimited"
        self.s5.control_panel = "cPanel"
        self.s5.domains = "Unlimited"
        self.s5.id = 3

        self.gd = WebHost()
        self.gd.company = "GoDaddy"
        self.gd.logo_img = ""
        self.gd.plan = "Deluxe"
        self.gd.price = "$9.99/mo"
        self.gd.disk_space = "Unlimited"
        self.gd.bandwidth = "Unlimited"
        self.gd.control_panel = "cPanel"
        self.gd.domains = "Unlimited"
        self.gd.id = 4

        self.sg = WebHost()
        self.sg.company = "SiteGround"
        self.sg.logo_img = ""
        self.sg.plan = "GrowBig"
        self.sg.price = "$14.95/mo"
        self.sg.disk_space = "20GB Web Space"
        self.sg.bandwidth = "Suitable for ~ 25,000 Visits Monthly"
        self.sg.control_panel = "cPanel"
        self.sg.domains = "Unlimited"
        self.sg.id = 5