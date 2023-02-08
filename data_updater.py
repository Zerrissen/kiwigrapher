# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Data updating program for Kiwigrapher. Scrapes ASB Kiwisaver data and sorts it.
#  todo            : Convert this to main file for controlling all function calls.
# ===========================================================================


# ===========================================================================
#                                Imports
# ===========================================================================
import datetime as dt
from os import path, getcwd
from time import sleep

import pandas as pd
import requests
from colorama import Fore, Style, just_fix_windows_console
from fake_useragent import UserAgent

from sorter import sort

# ===========================================================================
#                                CONSTANTS
# ===========================================================================
URL = "https://www.asb.co.nz/iFrames/investmentPerformance.asp"
TODAY = dt.datetime.today()
DELTA = dt.timedelta(days=1)
FIRST_ENTRY = dt.datetime(2007, 1, 10)
DAYS_SINCE_FIRST = (TODAY - FIRST_ENTRY).days  # Days since first entry
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.YELLOW
DEFAULT = Style.RESET_ALL

# ===========================================================================
#                            NON CONSTANT GLOBALS
# ===========================================================================
data = {
    'currentDay': 1,
    'currentMonth': 10,
    'currentYear': 2007
}


# ================================================
#  *                   main
#  ? Main function controls the execution of the program
#  @ return None
#  todo: implement import calls for each function to tidy up
# ================================================


def main():
    # ===========================================================================
    #  *                               INFO
    #  ? Check if the data file already exists, and if it is up to date.
    #  ? Also checks if the user would like to update and/or create the data file.
    #  todo: Move to same file as checkUpdate and call as import
    # ===========================================================================
    try:
        if path.exists('Data\Kiwisaver Data.csv'):
            print(f'{BLUE}Data file already exists!{DEFAULT}')
            df = pd.read_csv('Data\Kiwisaver Data.csv')
            lastDate = pd.to_datetime(df['Date'].iloc[-1], format='%Y-%m-%d')
            printDate = df['Date'].iloc[-1]
            print(f'{BLUE}Last known date: {DEFAULT}{printDate}')
            # If data is out of date, check if user wishes to update
            if lastDate < dt.datetime.today():
                checkUpdate(lastDate, printDate)
            else:
                print(
                    f'{BLUE}Data is up to date ({DEFAULT}{printDate}{BLUE}).')
        # If data does not exist, create csv and ask if user wants a full crawl
        else:
            with open('Data\Kiwisaver Data.csv', 'w') as file:
                file.write('Scheme,Price,Date\n')
            checkUpdate(None, printDate)
    except IndexError:
        print(f'{RED}No date entered. Assuming no data.{DEFAULT}')
        flag = True
    except Exception as e:
        print(f'{RED}Oops an error happened')
        print(f'{e}{DEFAULT}')
        exit(99)

    # ===========================================================================
    #  *                               INFO
    #  ? Check if the data has been sorted, and whether the user wants to sort it.
    #  todo: Move to sorter.py and call from sorter.
    # ===========================================================================
    try:
        count = 0
        df = pd.read_csv('Data\Kiwisaver Data.csv')
        for i, x in df.groupby('Scheme'):
            p = path.join(getcwd(), 'Data\{} Data.csv'.format(i))
            if path.exists(p):
                pass
            else:
                count += 1
    except Exception as e:
        print(f'{RED}Oops an error happened')
        print(f'{e}{DEFAULT}')
        exit(99)

    if count > 0:
        try:
            do_sort = input(
                f'{YELLOW}Data is not sorted. Would you like to sort? ({DEFAULT}Y/N{YELLOW}):{DEFAULT} ').lower().strip()
        except Exception as e:
            print(f'{RED}Oops an error happened')
            print(f'{e}{DEFAULT}')
            exit(99)

        if do_sort == 'y':
            print(f'{BLUE}Sorting data...{DEFAULT}')
            sort()
            print(f'{BLUE}Data is sorted.{DEFAULT}')
        else:
            print(f'{BLUE}Data will not be sorted.{DEFAULT}')


# ================================================
#  *                checkUpdate
#  ? Checks if user wants to update the data and acts accordingly.
#  @ return None
#  todo: Move to seperate file and call as import
# ================================================


def checkUpdate(lastDate, printDate):
    if lastDate >= (lastDate - DELTA):
        print(f'{BLUE}Data is up to date.{DEFAULT}')
    if lastDate is not None:
        print(f'{YELLOW}Data is out of date. Last known date is {DEFAULT}{printDate}')
        while True:
            try:
                doUpdate = input(
                    f'{BLUE}Update list? ({DEFAULT}Y/N{BLUE}): {DEFAULT}').lower().strip()
                if doUpdate == 'y' or doUpdate == 'n':
                    break
                else:
                    print(f'{RED}Unknown option. Try again.{DEFAULT}')
                    continue
            except Exception as e:
                print(f'{RED}Uh oh, an error occurred! Closing program.')
                print(f'{e}{DEFAULT}')
                exit(99)

        if doUpdate == 'y':  # Call update function with data startdate
            update(lastDate)
        else:
            print(f'{BLUE}Not updating!{DEFAULT}')

    elif lastDate is None:
        print(
            f'{YELLOW}Data does not exist. Do you wish to crawl the data from earliest known date?')
        print(f'{BLUE}Note: This will take {DEFAULT}' +
              str((DAYS_SINCE_FIRST / 60 / 60)) + f' {BLUE}hours.')
        while True:
            try:
                doUpdate = input(
                    f'Create full dataset? ({DEFAULT}Y/N{BLUE}):{DEFAULT} ').lower()
                if doUpdate == 'y':
                    # Call update function with no startdate for full crawl
                    update(None)
                elif doUpdate == 'n':
                    print(f'{BLUE}Not creating data. Closing updater.{DEFAULT}')
                    exit(0)
                else:
                    print(f'{RED}Unknown option. Try again.{DEFAULT}')
                    continue
            except Exception as e:
                print(f'{RED}Uh oh, an error occurred! Closing program.')
                print(f'{e}{DEFAULT}')
                exit(99)


# ================================================
#  *                  update
#  ? Updates the data
#  @ param lastDate datetime
#  @ return None
#  todo: Move to seperate file and call as import
# ================================================


def update(lastDate):
    if lastDate is not None:
        startDate = lastDate + DELTA  # start from the next day from data
    else:
        # full crawl, completely rebuild data from first known entry
        startDate = dt.datetime(2007, 10, 1)

    # update data with new data startdate
    while (startDate <= TODAY):
        sleep(1)
        header = {'User-Agent': str(UserAgent().random)}
        r = requests.post(URL, headers=header, data=data)
        df_list = pd.read_html(r.text)
        df = df_list[2]
        df['Date'] = startDate
        df.rename(columns={'ASB KiwiSaver Scheme fund': 'Scheme',
                  'Sell price': 'Price'}, inplace=True)
        startDate += DELTA
        data['currentDay'], data['currentMonth'], data['currentYear'] = startDate.day, startDate.month, startDate.year
        df.to_csv('Data\Kiwisaver Data.csv',
                  index=False, mode='a', header=False)
        print(
            f'{BLUE}Entry for {DEFAULT}{(startDate-DELTA).strftime("%Y-%m-%d")}{BLUE} added!{DEFAULT}')


if __name__ == '__main__':
    just_fix_windows_console()
    try:
        main()
    except KeyboardInterrupt:
        print(
            f'\n{RED}Keyboard Interrupt ({DEFAULT}Ctrl+C{RED}) detected. Closing program.{DEFAULT}')
        exit(0)  # Use code 0 here as this is not an error but user input.

    exit(0)  # Exit program smoothly
