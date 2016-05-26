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
        dh = WebHost()
        dh.company = "DreamHost"
        dh.logo_img = ""
        dh.plan = "Month-to-Month"
        dh.price = "$10.95/mo"
        dh.disk_space = "Unlimited"
        dh.bandwidth = "Unlimited"
        dh.control_panel = "DreamHost panel"
        dh.domains = "Unlimited"
        dh.id = 1

        hg = WebHost()
        hg.company = "HostGator"
        hg.logo_img = ""
        hg.plan = "Baby"
        hg.price = "$11.95/mo"
        hg.disk_space = "Unlimited"
        hg.bandwidth = "Unlimited"
        hg.control_panel = "cPanel"
        hg.domains = "Unlimited"
        hg.id = 2

        s5 = WebHost()
        s5.company = "Site5"
        s5.logo_img = ""
        s5.plan = "hostPro"
        s5.price = "$10.95/mo"
        s5.disk_space = "Unlimited"
        s5.bandwidth = "Unlimited"
        s5.control_panel = "cPanel"
        s5.domains = "Unlimited"
        s5.id = 3

        gd = WebHost()
        gd.company = "GoDaddy"
        gd.logo_img = ""
        gd.plan = "Deluxe"
        gd.price = "$9.99/mo"
        gd.disk_space = "Unlimited"
        gd.bandwidth = "Unlimited"
        gd.control_panel = "cPanel"
        gd.domains = "Unlimited"
        gd.id = 4

        sg = WebHost()
        sg.company = "SiteGround"
        sg.logo_img = ""
        sg.plan = "GrowBig"
        sg.price = "$14.95/mo"
        sg.disk_space = "20GB Web Space"
        sg.bandwidth = "Suitable for ~ 25,000 Visits Monthly"
        sg.control_panel = "cPanel"
        sg.domains = "Unlimited"
        sg.id = 5