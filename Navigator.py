import re, mechanize
from BeautifulSoup import BeautifulSoup

class Navigator():

    br = mechanize.Browser()
    logged_in = False

    def clearBrowser(self):
        self.br = mechanize.Browser()

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

    def find(self, subj="", crse="", crn="", term="", year=""):
        url = "https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcRequest?"
        # CAMPUS=0 is Blacksburg
        # AR%25 is All Areas of Classes

        url += "CAMPUS=" + str(0) + "&TERMYEAR=" + year + term
        url += "&CORE_CODE=" + "AR%25" + "&SUBJ_CODE=" + subj
        url += "&CRSE_NUMBER=" + crse + "&crn=" + crn + "&open_only=" + ""
        url += "&PRINT_FRIEND=" + "Y"  # + "&BTN_PRESSED=" + "FIND+class+sections"

        browser = self.br.open(url)
        contents = browser.read()

        if ("NO SECTIONS FOUND FOR THIS INQUIRY." in contents):
            return None

        return contents
