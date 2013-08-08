import sys
import os
from getpass import getpass
from Navigator import Navigator


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


def checkVersion(major, minor, micro):
    major = int(major)
    minor = int(minor)
    micro = int(micro)

    if [major, minor, micro] <= [2, 7, 4]:  # <= Python 2.7.4 Will Work
        return ""
    elif [major, minor, micro] <= [2, 9, 9]:  # < Python 3.0.0 Will Probably Work
        return "Warning: This Program May Work, Python 2.7.4 is Known to Work and {0}.{1}.{2} is Installed".format(major, minor, micro)
    elif [major, minor, micro] >= [3, 0, 0]:  # >= Python 3.x.x Will Definitely Not Work
        return "Error: This Won't Work, Please Install The Latest Python Version 2.x.x \n \
        Exit Status: 1 - Incompatible Python Version Installed (Python 3.x.x Detected) "


def main():
    clearConsole()

    nav = Navigator()
    courses = []

    major, minor, micro = sys.version_info[:3]
    message = checkVersion(major, minor, micro)

    if message != "":
        print message

    if "Error" in message:
        sys.exit(1)

    username = getpass('PID: ')
    password = getpass()

    print "Logging In.. "
    sys.stdout.flush()

    while (nav.login(username, password) is False):
        print "Please Try Again"

        username = raw_input('PID: ')
        password = getpass()

    clearConsole()

    automate = raw_input("Automate?: ")

    if automate:
        errors = ""
        CRN = "92074"
        TERM = "09"
        YEAR = "2013"
        SUBJ = "CS"
        CRSE = "2114"
    else:
        errors = 1

    print "Logged In"

    print "Please Enter The Following Information:"

    error_checker = ErrorCheck()

    while (errors):

        CRN = raw_input('CRN: ') or ""  # or "92083"
        TERM = raw_input('TERM (F, S, S1, or S2) (F - Default): ') or "09"  # Default TERM if nothing is given
        YEAR = raw_input('YEAR (2013 - Default): ') or "2013"  # Default YEAR if nothing is given
        SUBJ = raw_input('SUBJ: ') or ""
        CRSE = raw_input('CRSE: ') or ""

        print "\nChecking for Errors in Course Information..\n"

        errors = error_checker.obviousChecks(crn=CRN, subj=SUBJ, crse=CRSE)

        if (errors):
            print "Sorry, There Were Some Errors: \n"
            print "Error(s): "
            for error in errors:
                print error
            print "Please Try Again"

    clearConsole()
    print "Everything Looks Good.."
    print "Searching for Class Information.."

    if ((SUBJ and CRSE) or CRN):
        course_info = nav.find(subj=SUBJ, crse=CRSE, term=TERM, year=YEAR, crn=CRN)
    else:
        print "Sorry.. You Didn't Enter Enough Information"
        sys.exit(0)

    if course_info is None:
        print "Sorry.. No Sections were Found"
        answer = raw_input("Try Again..? ")
        sys.exit(0)
    else:
        course_info = Cleaner(course_info)

    print "Here's What I Found.."

    print course_info

    answer = YesNo(raw_input("Do You Wish to Add a Course? Enter (y)es or (n)o: "))

    if answer == "Yes":
        CRN = raw_input("Please Enter the CRN: ")
        courses.append(CRN)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
