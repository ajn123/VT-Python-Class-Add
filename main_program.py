import re, os, sys, mechanize
from getpass import getpass
from BeautifulSoup import BeautifulSoup

class Navigator():

    br = mechanize.Browser()
    logged_in = False

    def clearConsole(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def checkVersion(self, major, minor, micro):
        major = int(major)
        minor = int(minor)
        micro = int(micro)

        if (major, minor, micro) <= (2, 7, 4):  # <= Python 2.7.4 Will Work
            return ""
        elif (major, minor, micro) <= (2, 9, 9):  # < Python 3.0.0 Will Probably Work
            return """
            Warning: This May Work, Python 2.7.x is Known to Work and {0}.{1}.{2} is Installed
            """.format(major, minor, micro)
        elif (major, minor, micro) >= (3, 0, 0):  # > Python 3.x.x Will Definitely Not Work
            return """
            Error: This Won't Work, Please Install The Latest Python Version 2.x.x
            Exit Status: 1 - Incompatible Python Version Installed (Python 3.x.x Detected)
            """

    def login(self, username, password):
        login_url = "https://auth.vt.edu/login?service=https://webapps.banner.vt.edu/banner-cas-prod/authorized/banner/SelfService"
        br = self.br
        br.open(login_url)
        br.select_form(nr=0)  # Select the 'Login' Form
        br.set_handle_robots(False)  # Ignore robots.txt file
        br.form["username"] = username
        br.form["password"] = password
        resp = br.submit()

        if ("Invalid username or password" in resp.read()):
            return False

        else:
            self.logged_in = True
            return True

    def validCourseInfo(self, crn="", term="09", year="2013", subj="", crse=""):
        # validity = [True, True, True, True, True]

        valid = True

        if (len(crn) != 5 and crn != ""):  # If a CRN is given, check if it's valid
            # validity[0] = False
            valid = "Please enter a CRN number that is 5 digits"

        return valid
