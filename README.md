# Kiwigrapher

## An ASB Kiwisaver scheme grapher and analysis tool.

###### This tool is developed for educational and hobbyist purposes only. Not intended for commercial purposes. Use at your own risk.

---

## Installation

Clone the repository to your chosen directory:\
`git clone https://github.com/zerrissen/kiwigrapher`

CD into the repository:\
`cd \file\path\to\repo`

Install dependencies:\
`python3 -m pip install -r requirements.txt`

OR

`pip3 install -r requirements.txt`

Run program:\
`python3 main.py`

---

## Usage

When running the program, the user will be greeted with the main menu prompt.
This will ask the user to select a program function from the following options.

### Scrape Data

This will allow the user to scrape raw data from the ASB database. Note that this is considered "Unverified" data and will likely contain anomolies.

### Update Data

The user can update locally saved, unverified data using this option. This allows the user to keep up to date, without having to spend hours scraping the ASB database again.

### Verify Data

As of release 1.1.0, this function is unavailable. Users can expect this to be available by release 1.2.0.

### Sort Data

This function sorts the the data by splitting it into multiple files for each ASB Kiwisaver Scheme, allowing for analysis of seperate schemes.

### Graph Data

This function will plot either unverified or verified data as a line chart using matplotlib.Eventually further functionality will be available, such as the choice of charts and range of data to be displayed.

---

## License

This program is licensed under the GNU General Public License version 3.0.
Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.
