#!/usr/bin/env python2.7

import sys
import os
from getpass import getpass
from Navigator import Navigator
from Helper import ErrorCheck, YesNo, Cleaner

"""
Clears the command window.
"""
def clearConsole():
    # 'cls' is used with Windows based operating systems
    # 'clear' is used with POSIX based operating systems
    os.system('cls' if os.name == 'nt' else 'clear')

"""
Checks the python version and displays a warning or error if the incorrect
version is used.

@param major - An integer indicating the major version number.
@param minor - An integer indicating the minor version number.
@param micro - An integer indicating the micro version number.

@return string message - Returns a string message.
"""
def checkVersion(major, minor, micro):
    major = int(major)
    minor = int(minor)
    micro = int(micro)

    # Don't return a message if Python 2.7.4 or below is being used.
    if [major, minor, micro] <= [2, 7, 4]:
        return ""
    # Return a warning message if Python 2.9.9 or below is being used.
    elif [major, minor, micro] <= [2, 9, 9]:
        return "Warning: This Program May Work, Python 2.7.4 is Known to Work and {0}.{1}.{2} is Installed".format(major, minor, micro)
    # Return an error message if Python 3.0.0 or above is being used.
    elif [major, minor, micro] >= [3, 0, 0]:
        return "Error: This Won't Work, Please Install The Latest Python Version 2.x.x"

"""
This program uses the mechanize library in order to log users in, search through
available courses, add courses to a list, and tries to add a user to a course.
"""
def main():

    # Clear the console before the program begins.
    clearConsole()

    # Create a navigator object which will browse through online courses.
    nav = Navigator()

    # The courses list will be used to store course information.
    courses = []

    major, minor, micro = sys.version_info[:3]
    message = checkVersion(major, minor, micro)

    if "Error" in message:
        print "Exit Status: 1 - Incompatible Python Version Installed (Python 3.x.x Detected)"
        sys.exit(1)
    elif "Warning" in message:
        print message

    print "Please Enter Your.."
    print ""
    username = getpass('PID: ')
    password = getpass()

    # If login returns false, then we are not logged in and we need to try again
    while (nav.login(username, password) is False):
        clearConsole()
        print "I was Unable to Login. Please Try Again."

        print ""
        print "Please Enter Your.."
        print ""
        username = getpass('PID: ')
        password = getpass()

    clearConsole()
    print "Logged In."
    print "Please Enter The Following Information:"
    print ""

    error_checker = ErrorCheck()
    errors = True

    while (errors):

        CRN = raw_input('CRN: ') or "92074"
        # The default term is '09' which is Fall Semester if nothing is entered.
        TERM = raw_input('TERM (F, S, S1, or S2) (F - Default): ') or "09"
        YEAR = raw_input('YEAR (2013 - Default): ') or "2013"
        SUBJ = raw_input('SUBJ: ')  or "CS"
        CRSE = raw_input('CRSE: ') or "2114"

        clearConsole()
        print "Checking for Errors in Course Information."

        errors = error_checker.obviousChecks(crn=CRN, subj=SUBJ, crse=CRSE)

        if (errors):
            print "Sorry, There Were Some Errors."
            print "Error(s): "
            for error in errors:
                print error
            print "Please Try Again"

    print "Everything Looks Good."
    print "Searching for Class Information."

    # The user must enter a subject and a course number or just a crn
    if ((SUBJ and CRSE) or CRN):
        # The navigator will try to find any course information
        course_info = nav.find(subj=SUBJ, crse=CRSE, term=TERM, year=YEAR, crn=CRN)
    else:
        print "Sorry. You Didn't Enter Enough Information."
        print "Exiting."
        sys.exit(0)

    # If the navigator was unable to find course information, we will just exit.
    if course_info is None:
        print "Sorry. No Sections were Found."
        print "Exiting."
        sys.exit(0)
    else:
        # If the course information was found, we should present the information
        # in a human readable format.
        course_info = Cleaner(course_info)

    print "Here's What I Found.."

    print course_info

    answer = True

    while (answer):

        answer = YesNo(raw_input("Do You Wish to Add a Course? Enter (Y)es or (N)o: "))

        if answer == "Yes":
            CRN = raw_input("Please Enter the CRN: ")
            courses.append(CRN)
            print "CRN(s) Added So Far: " + str(courses)
        else:
            answer = False

    print "I Will Try to Add Your Courses."





if __name__ == "__main__":
    main()
