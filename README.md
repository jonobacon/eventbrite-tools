# eventbrite-tools

This is a simple script for making use of attendee data from the Eventbrite event
organization website.

The first cut of this code was written by Van Riper and then I (Jono Bacon)
rewrote it.

## Usage

Firstly, download the attendee list in plain text format. To do this:

 1. Go to http://www.eventbrite.com
 2. Click your name in the top-right corner of the page. Select *My Events*.
 3. Select your event from the list and in the Event Dashboard, select *Orders* from the *Manage Attendees* section.
 4. Use the Export combo box to select *Export to Text* and then save the page to your computer.

You can now use this saved file as the *input file* in the commands below.

### Generate a HTML list of attendees

This is useful for embedding the list on your website.

```
python etools.py inputfile.txt -r
```

### Generate a list of email addresses for attendees

This provides a list of email addresses, useful for reaching out to all attendees.

```
python etools.py inputfile.txt -e
```
