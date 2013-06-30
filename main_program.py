import re, os, sys, mechanize
from getpass import getpass
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
crn_filled = False
courses = []

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def checkVersion(major, minor, micro):

    if major == 2 and minor <= 7 and micro <= 4: # <= Python 2.7.4 Will Work
        pass
    elif major <= 2 and minor <= 9 and micro <= 9: # < Python 3.0.0 Will Probably Work
        return
        """
        Warning: This May Work, Python 2.7.x is Known to Work and {0}.{1}.{2} is Installed
        """.format(major, minor, micro)
    elif major >= 3 and minor >= 0 and micro >= 0: # > Python 3.x.x Will Definitely Not Work
        return
        """
        Error: This Won't Work, Please Install The Latest Python Version 2.x.x
        Exit Status: 1 - Incompatible Python Version Installed (Python 3.x.x Detected)
        """

def login(username, password):

    login_url = "https://auth.vt.edu/login?service=https://webapps.banner.vt.edu/banner-cas-prod/authorized/banner/SelfService"
    br.open(login_url)
    br.select_form(nr = 0) # Select the 'Login' Form
    br.set_all_readonly(False)
    br.set_handle_robots(False) # Ignore robots.txt file
    br.set_handle_refresh(False)
    br.form["username"] = username
    br.form["password"] = password
    resp = br.submit()

    if "Invalid username or password" in resp.read():
        return False

    else:
        return True

def checkCourseInfo(crn, term, year, subj, crse):

    if (crn != "" and len(crn) == 5): # If a CRN is given, check if it's valid
        global crn_filled
        crn_filled = True
        return True

    if (subj != "" or crse != ""): # If a SUBJ or CRSE is given..
        if (subj != "" and crse != ""): # .. then check to make sure Both are completed
            return True

    return False

def findByCRN(CRN, TERM, YEAR):

    url = "https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcComments?"
    url += "CRN=" + CRN + "&TERM=" + TERM + "&YEAR=" + YEAR

    browser = br.open(url)
    contents = browser.read()

    soup = BeautifulSoup(contents)
    classinfo = soup.findAll("td", {"class" : "mpdefault"})

    return clean(classinfo)

def findBySUBJ(SUBJ, CRSE, TERM, YEAR):

    url = "https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcRequest?"
    url += "CAMPUS=0" + "&TERMYEAR=" + YEAR + TERM + "&SUBJ_CODE=" + SUBJ + "&CRSE_NUMBER=" + CRSE

    br.open(url)
    br.select_form(nr = 0)

    browser = br.submit(label='FIND class sections')
    contents = browser.read()

    soup = BeautifulSoup(contents)
    data = soup.findAll("td", {"class" : re.compile(r'(deright|deleft|dedefault)')})
    data = clean(data)

    all_sections = []
    section_info = []

    current_element = data.pop(0) # Let's pop the first element since this is the first CRN
    section_info.append(current_element) # Add it to section info

    while len(data) > 0: # While we have at least one element
        current_element = data[0] # Let's look at the first element

        if (len(current_element) == 5 and current_element.isdigit()): # If the element's length is 5 and is a digit, then we have a CRN number
            all_sections.append(section_info)
            section_info = []

        current_element = data.pop(0) # Let's pop the first element
        section_info.append(current_element) # and add it to section info

    all_sections.append(section_info) # For the last section

    return all_sections

def pretty(subj=None, crn=None):

    if subj is not None:

        if "* Additional Times *" in subj:
            return """
            CRN:            {}
            Course:         {}
            Description:    {}
            Type:           {}
            Credit Hours:   {}
            Capacity:       {}
            Instructor:     {}
            Day(s):         {}
            Begin:          {}
            End:            {}
            Location:       {}
            Exam:           {}
            {}
            Day(s)          {}
            Begin:          {}
            End:            {}
            Location:       {}
            """.format(*subj)

        else:
            return """
            CRN:            {}
            Course:         {}
            Description:    {}
            Type:           {}
            Credit Hours:   {}
            Capacity:       {}
            Instructor:     {}
            Day(s):         {}
            Begin:          {}
            End:            {}
            Location:       {}
            Exam:           {}
            """.format(*subj)

    elif crn is not None:

        if "* Additional Times *" in crn:

            return """
            CRN:            {}
            Course:         {}
            Description:    {}
            Type:           {}
            Credit Hours:   {}
            Capacity:       {}
            Instructor:     {}
            Day(s):         {}
            Begin:          {}
            End:            {}
            Location:       {}
            Exam:           {}
            {}
            Day(s)          {}
            Begin:          {}
            End:            {}
            Location:       {}
            """.format(*crn)

        else:

            return """
            Day(s):         {}
            Begin:          {}
            End:            {}
            Location:       {}
            Exam:           {}
            Instructor:     {}
            Type:           {}
            Status:         {}
            Seats Avail:    {}
            Capacity:       {}
            """.format(*crn)


def clean(classinfo):

    classinfo = str(classinfo)

    classinfo = re.sub(r'(&nbsp;){0,}', '', classinfo)      # Remove &nbsp;
    classinfo = re.sub(r'(&amp;)', '&', classinfo)          # Replace &amp with &;
    classinfo = re.sub(r'[\[\]]', '', classinfo)            # Remove [ and ]
    classinfo = re.sub(r'<.+?>', ' ', classinfo)            # Remove html tags
    classinfo = classinfo.split(' , ')                      # Split the String Into a List
    classinfo = [string.strip() for string in classinfo]    # Remove White Space Characters from Each Element
    classinfo = filter(None, classinfo)                     # Remove Empty Entries

    return classinfo # Returns a List

def main():

    clearConsole();

    major, minor, micro = sys.version_info[:3]

    message = checkVersion(major, minor, micro)

    if message is not None:
        print message

    if "Error" in message:
        sys.exit(1)

    username = raw_input('PID: ')
    password = getpass()

    print "Logging In.. "; sys.stdout.flush()

    while (login(username, password) == False):
        print "Please Try Again"

        username = raw_input('PID: ')
        password = getpass()

    print "Logged In"
    print "Please Enter The Following Information:"

    CRN  = raw_input('CRN: ') # or "92083"
    TERM = raw_input('TERM (F, S, S1, or S2) (F - Default): ') or "09" # Default TERM if nothing is given
    YEAR = raw_input('YEAR (2013 - Default): ') or "2013" # Default YEAR if nothing is given
    SUBJ = raw_input('SUBJ: ')
    CRSE = raw_input('CRSE: ')

    while (checkCourseInfo(CRN, TERM, YEAR, SUBJ, CRSE) == False):
        clearConsole()
        print "TERM: " + TERM
        print "YEAR: " + YEAR
        print "Please Enter a CRN number that is 5 digits or enter a subject and course number"
        CRN = raw_input('CRN:  ')
        SUBJ = raw_input('SUBJ: ')
        CRSE = raw_input('CRSE: ')

    clearConsole()

    print "Fetching Course Information.. "

    if (crn_filled == True):
        classinfo = findByCRN(CRN, TERM, YEAR)
        print classinfo
        print pretty(crn = classinfo)

    else:
        print """
        Info For {} {}
        """.format(SUBJ, CRSE)
        sections = findBySUBJ(SUBJ, CRSE, TERM, YEAR)

        for section in sections:
            print pretty(subj = section)

        CRN = raw_input("Which CRN? ")
        classinfo = findByCRN(CRN, TERM, YEAR)
        print pretty(crn = classinfo)

    answer = raw_input("Do You Want to Add This Course? (Yes/Y or No/N) ")

    while (re.search(r'([Yy][Ee]*[Ss]*)|([Nn][Oo]*)', answer) == None):
        answer = raw_input("Please Enter a Valid Answer: ")

    if re.search(r'[Yy][Ee]*[Ss]*', answer):
        courses.append(CRN)

    answer = raw_input("Begin? (Yes/Y or CRN Number) ")

if __name__ == "__main__":
    main()
