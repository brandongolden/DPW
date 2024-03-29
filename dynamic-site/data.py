'''
Brandon Golden
5/24/16
DPW
Dynamic Site
'''


class WebHost(object):
    def __init__(self):
        # Attributes
        self.company = ""
        self.plan = ""
        self.price = ""
        self.disk_space = ""
        self.bandwidth = ""
        self.control_panel = ""
        self.domains = ""

class Data(object):
    def __init__(self):
        dh = WebHost()  # Create instance of WebHost
        dh.company = "DreamHost"
        dh.plan = "Month-to-Month"
        dh.price = "$10.95/mo"
        dh.disk_space = "Unlimited"
        dh.bandwidth = "Unlimited"
        dh.control_panel = "DreamHost panel"
        dh.domains = "Unlimited"

        hg = WebHost()  # Create instance of WebHost
        hg.company = "HostGator"
        hg.plan = "Baby"
        hg.price = "$11.95/mo"
        hg.disk_space = "Unlimited"
        hg.bandwidth = "Unlimited"
        hg.control_panel = "cPanel"
        hg.domains = "Unlimited"

        s5 = WebHost()  # Create instance of WebHost
        s5.company = "Site5"
        s5.plan = "hostPro"
        s5.price = "$10.95/mo"
        s5.disk_space = "Unlimited"
        s5.bandwidth = "Unlimited"
        s5.control_panel = "cPanel"
        s5.domains = "Unlimited"

        gd = WebHost()  # Create instance of WebHost
        gd.company = "GoDaddy"
        gd.plan = "Deluxe"
        gd.price = "$9.99/mo"
        gd.disk_space = "Unlimited"
        gd.bandwidth = "Unlimited"
        gd.control_panel = "cPanel"
        gd.domains = "Unlimited"

        sg = WebHost()  # Create instance of WebHost
        sg.company = "SiteGround"
        sg.plan = "GrowBig"
        sg.price = "$14.95/mo"
        sg.disk_space = "20GB Web Space"
        sg.bandwidth = "Suitable for ~ 25,000 Visits Monthly"
        sg.control_panel = "cPanel"
        sg.domains = "Unlimited"

        # Store data objects in array to make them easily accessible
        self.webhosts_array = [dh, hg, s5, gd, sg]