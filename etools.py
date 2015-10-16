"""Parse input file to extract and output data to files."""

__author__ = 'jono@jonobacon.org (Jono Bacon)'
__author__ = 'vanriper@google.com (Van Riper)'

import sys
import re
import string

class Etools():
    def __init__(self, argv):
        self.args = sys.argv

        for a in self.args:
            if a == "-r":
                self.func_reg_html()

            if a == "-e":
                self.func_email_list()


    def get_data_col(self, s):
        """Return the column number for a given data type in the source file"""

        num = 0

        for i in self.data:
            if i.rstrip() == s:
                return num

            num = num + 1

    def func_reg_html(self):
        """Create a HTML list of registered attendees, including first name,
        last name, organization, and role."""

        print "Generating list of registered attendees..."

        self.load_source_file()

        names = []
        out_html = open("attendees-html-list.txt", 'w')

        print self.in_file

        for line in self.in_file:
          cells = line.split('\t')
          first_name = cells[self.get_data_col("First Name")].strip().lower().title()
          last_name = cells[self.get_data_col("Last Name")].strip().lower().title()
          organization = cells[self.get_data_col("Company / Organization")].strip().lower().title()
          role = cells[self.get_data_col("Job Title")].strip().lower().title()

          if (first_name != last_name):
            if not organization == "":
                names.append('<strong>%s %s</strong> - <i>%s</i> - %s' % (first_name, last_name,
                                            organization, role))
            else:
                names.append('<strong>%s %s</strong>' % (first_name, last_name))


        prev_name = ''
        names.sort()
        out_html.write('<ul>\n')
        for name in names:
          if prev_name != name:
            out_html.write('  <li>%s</li>\n' % name)
          prev_name = name
        out_html.write('</ul>\n')

        self.close_source_file()

        print "...done."

    def func_email_list(self):
        """Generate a list of email addresses (useful for emailing registered
        attendees)."""

        print "Generating list of emails..."

        self.load_source_file()

        emails = []
        out_emails = open("email-addresses.txt", 'w')

        print self.in_file

        for line in self.in_file:
            cells = line.split('\t')
            email = cells[self.get_data_col("Email Address")].strip().lower()
            if re.match('.+@.+\..+', email):
                emails.append(email.lower())

        prev_email = ''
        emails.sort()
        for email in emails:
          if prev_email != email:
            out_emails.write(email + '\n')
          prev_email = email

        self.close_source_file()
        print "...done."

    def load_source_file(self):
        input_file = sys.argv[1]

        self.in_file = open(input_file, 'r')

        self.data = self.in_file.readline().split('\t')

    def close_source_file(self):
        self.in_file.close()


if __name__ == '__main__':
  e = Etools(sys.argv)
