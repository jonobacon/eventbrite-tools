#!/usr/bin/python2.4

"""Parse input file to extract and output data to files."""

__author__ = 'jono@jonobacon.org (Jono Bacon)'
__author__ = 'vanriper@google.com (Van Riper)'

import sys
import re

def main(argv):
  """Parse input file to extract and output data to files.

  argv must consist of three values: an input filename with the raw
  tab delimited registration data, an output filename for a comma
  separated list of email addresses, and an output filename for an
  HTML list of just names and affiliations for attendees.

  Args:
    argv: Index 1 is the input file, e.g. cls-reg.txt.  Index 2 is the
        output file for the email addresses, e.g. emails.txt. Index 3
        is the output file for HTML unordered list, e.g. list.html.
  """

  if len(argv) < 4:
    print 'Usage: etools.py [input-file] [output-emails] [output-html]'
    print '       etools.py reg.txt emails.txt list.html'
    sys.exit()

  input_file = argv[1]
  output_email_addresses = argv[2]
  output_html_list = argv[3]

  print 'Parsing %s to create %s and %s' % (input_file,
                                       output_email_addresses,
                                       output_html_list)
  in_file = open(input_file, 'r')
  print in_file
  out_emails = open(output_email_addresses, 'w')
  out_html = open(output_html_list, 'w')

  names = []
  emails = []

  for line in in_file:
    cells = line.split('\t')
    print cells[12]
    first_name = cells[12].strip().lower().title()
    last_name = cells[13].strip().lower().title()
    organization = cells[16].strip().lower().title()
    role = cells[15].strip()
    email = cells[14].strip()
    if (first_name != last_name
        and email != 'Email'
        and re.match('.+@.+\..+', email)):
      if not organization == "":
          names.append('<strong>%s %s</strong> - <i>%s</i> - %s' % (first_name, last_name,
                                      organization, role))
      else:
          names.append('<strong>%s %s</strong>' % (first_name, last_name))
		  
      emails.append(email.lower())


  prev_name = ''
  names.sort()
  out_html.write('<ul>\n')
  for name in names:
    if prev_name != name:
      out_html.write('  <li>%s</li>\n' % name)
    prev_name = name
  out_html.write('</ul>\n')

  prev_email = ''
  emails.sort()
  for email in emails:
    if prev_email != email:
      out_emails.write(email + '\n')
    prev_email = email

if __name__ == '__main__':
  main(sys.argv)
