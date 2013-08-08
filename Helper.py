# Helper Classes

import re, os, sys, mechanize
from getpass import getpass
from BeautifulSoup import BeautifulSoup

def YesNo(answer):

    while (re.search(r'([Yy][Ee]*[Ss]*)|([Nn][Oo]*)', answer) == None):
        answer = raw_input("Please Enter a Valid Answer: ")

    if re.search(r'[Yy][Ee]*[Ss]*', answer):
        return "Yes"
    else:
        return "No"

class ErrorCheck():

    def obviousChecks(self, crn="", term="09", year="2013", subj="", crse=""):
        errors = []

        if crn:  # If a CRN is given
            if (len(crn) == 5 and crn.isdigit() is True):
                pass
            else:
                errors.append("Please enter a valid CRN")

        if subj:  # If a Subject is given
            if (subj.isalpha() is True):
                pass
            else:
                errors.append("Please enter a valid Subject")

        if crse:  # If a Course Number is given
            if (len(crse) == 4 and crse.isdigit() is True):
                pass
            else:
                errors.append("Please enter a valid Course Number")

        return errors

    def harderChecks(self, crn="", term="09", year="2013", subj="", crse=""):
        errors = []

class Cleaner():

    data = ""

    def __init__(self, contents):
        soup = BeautifulSoup(contents)

        self.data = soup.findAll("td", {"class" : "pldefault"})
        self.data = self.toList(self.data)
        self.data = self.parseList(self.data)
        self.data = self.pretty(self.data)

        return None

    def __str__(self):
        return self.data

    def toList(self, classinfo):
        classinfo = str(classinfo)

        classinfo = re.sub(r'(&nbsp;){0,}', '', classinfo)      # Replace &nbsp; with ''
        classinfo = re.sub(r'(&amp;)', '&', classinfo)          # Replace &amp with &
        classinfo = re.sub(r'[\[\]]', '', classinfo)            # Replace [ and ] with ''
        classinfo = re.sub(r'<.+?>', ' ', classinfo)            # Replace html tags with ''
        classinfo = classinfo.split(' , ')                      # Split the String Into a List
        classinfo = [string.strip() for string in classinfo]    # Remove White Space Characters from Each Element
        classinfo = filter(None, classinfo)                     # Remove Empty Entries

        return classinfo # Returns a List

    def parseList(self, data):
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

    def pretty(self, course_info):
        string = ""

        for course in course_info:
            info = """
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
                """

            if "* Additional Times *" in course_info:
                info += """
                {}
                Day(s)          {}
                Begin:          {}
                End:            {}
                Location:       {}
                """

            string += info.format(*course)

        return string

class CourseWatch():
    pass

