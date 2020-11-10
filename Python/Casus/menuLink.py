import screenCompo

# this file contains an object that will be used in making the menu's for the client

class MenuLink(object):
    # default to the error screen
    def __init__(self, text, link=screenCompo.error_404):
        self.text = text
        self.link = link