import os
import unittest
from etools import Etools


class EmailListTestCase(unittest.TestCase):
    def setUp(self):
        test = Etools(os.path.abspath('tests/sample-input.data'))
        test.func_email_list()
        test.func_reg_html()
        self.email_out = os.path.abspath('email-addresses.txt')
        self.html_out = os.path.abspath('attendees-html-list.txt')

    def tearDown(self):
        os.remove(self.email_out)
        os.remove(self.html_out)

    def test_email_output(self):
        self.maxDiff = None
        with open(self.email_out) as f:
            self.assertEqual(
                f.readlines(),
                [
                    'augublair@fr.com\n',
                    'bob@a.com\n',
                    'editor@f.org\n',
                    'james@o.com\n',
                    'jane@g.com\n',
                    'jim@g.com\n',
                    'sarah@g.com\n',
                    'sas1234@gf.com\n'
                ]
            )

    def test_html_out(self):
        with open(self.html_out) as f:
            self.assertEqual(
                f.readlines(),
                [
                    '<ul>\n',
                    '  <li><strong>Dave Gowitz</strong> - <i>Maxcorp</i> - Software Engineer</li>\n',
                    '  <li><strong>James Dobbs</strong> - <i>Opencom</i> - Partner</li>\n',
                    '  <li><strong>Jane Silva</strong> - <i>Yupcorp</i> - Marketing</li>\n',
                    '  <li><strong>Jim Bat</strong> - <i>Curiosity Collider</i> - Member</li>\n',
                    '  <li><strong>Mel Dunno</strong> - <i>Dipcorp</i> - Event Coordinator</li>\n',
                    '  <li><strong>Michael Dexter</strong> - <i>Portcorp</i> - Volunteer</li>\n',
                    '  <li><strong>Roger Erbs</strong> - <i>Corp</i> - Engineer</li>\n',
                    '  <li><strong>Sarah Johnson</strong> - <i>Devcorp</i> - Inventor</li>\n',
                    '</ul>\n'
                ]
            )


if __name__ == '__main__':
    unittest.main()
