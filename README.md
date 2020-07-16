# UVic Schedule

A Python Script for Creating an `.ics` File for your UVic Schedule. 

The UVic Schedule Script uses [BeautifulSoup4](http://www.crummy.com/software/BeautifulSoup/),  [Mechanize](https://pypi.python.org/pypi/mechanize/), and [icalendar](https://pypi.org/project/icalendar/).

## Setup

### Install Requirements

```sh
pip3 install -r requirements.txt
```

## Usage

The first time you run the following command and once `.cookies` expires, you will be prompted to login with your NETLINK ID and PASSWORD.

### Create `.ics` File

Replace `[TERM]` with the term for your `.ics` file. **Note** This is only for readability, and ease of use. You may use any naming convention for `.ics` file.

```sh
python3 getSchedule.py calendar-TERM.ics
```

### Change Selected Term

To change the selected term run the following command. You will be prompted to select a term. If you aren't logged in, you will be prompted to login with your NETLINK ID and PASSWORD.

```sh
python3 changeTerm.py
```

## Importing Calendar

The above command `python3 getSchedule.py calendar-TERM.ics` creates a file named `calendar-TERM.ics` located in the root directory of this git repository. You can import this file into your desired Calendar Application to import your UVic Schedule for that TERM. You will need to do this with every `.ics` file you create.  

Below is a list of links to resources if you need help, or want to read more about how to import an `.ics` file into your Calendar App.

* [Import to Google Calendar](https://support.google.com/calendar/answer/37118)
* [Import to Apple Calendar](https://support.apple.com/en-ca/guide/calendar/icl1023/mac)
* [Import to Outlook Calendar](https://support.microsoft.com/en-us/office/import-or-subscribe-to-a-calendar-in-outlook-on-the-web-503ffaf6-7b86-44fe-8dd6-8099d95f38df)

## Credits

* [Brynn Hawker](https://github.com/hwkr) for the original UVicSchedule.
* [Denis Kisselev](https://github.com/dkisselev) for the original UVic Auth Script.
