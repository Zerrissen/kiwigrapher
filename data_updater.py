import requests
import pandas as pd
import datetime as dt
import sorter
from colorama import Fore, Style, just_fix_windows_console
from os import path
from time import sleep
from fake_useragent import UserAgent

# Constant, never changes from this point. Accessed by multiple functions.
URL = "https://www.asb.co.nz/iFrames/investmentPerformance.asp"
TODAY = dt.datetime.today()
DELTA = dt.timedelta(days=1)
FIRST_ENTRY = dt.datetime(2007, 1, 10)
DAYS_SINCE_FIRST = (TODAY - FIRST_ENTRY).days # Number of days since the first known Kiwisaver Data entry from ASB
BLUE = Fore.BLUE
RED = Fore.RED
YELLOW = Fore.YELLOW
DEFAULT = Style.RESET_ALL

# Not constant, accessed by multiple functions
data = {
    'currentDay' : 1,
    'currentMonth' : 10,
    'currentYear' : 2007
}

# Top of call stack
def main():
    # Check if data exists and is up to date
    try:
        if path.exists('Data\Kiwisaver Data.csv'):
            print(f'{BLUE}Data file already exists!')
            df = pd.read_csv('Data\Kiwisaver Data.csv')
            lastDate = pd.to_datetime(df['Date'].iloc[-1], format='%Y-%m-%d')
            printDate = df['Date'].iloc[-1]
            print(f'Last known date: {DEFAULT}{printDate}')
            # If data is out of date, check if user wishes to update
            if lastDate < dt.datetime.today():
                checkUpdate(lastDate, printDate)
            else:
                print(f'{BLUE}Data is up to date ({DEFAULT}{printDate}{BLUE}). Closing updater.{DEFAULT}')
                exit(0)
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
        exit(0)

# Check if the user wishes to update. Either second in callstack, or not called.
def checkUpdate(lastDate, printDate):
    if lastDate >= (lastDate - DELTA):
        print(f'{BLUE}Data is up to date. Closing program.{DEFAULT}')
        exit(0)
    if lastDate is not None:
        print(f'{YELLOW}Data is out of date. Last known date is {DEFAULT}{printDate}')
        while True:
            try:
                doUpdate = input(f'{BLUE}Update list? ({DEFAULT}Y/N{BLUE}): {DEFAULT}').lower().strip()
                if doUpdate == 'y' or doUpdate == 'n':
                    break
                else:
                    print(f'{RED}Unknown option. Try again.{DEFAULT}')
                    continue
            except Exception as e:
                print(f'{RED}Uh oh, an error occurred! Closing program.')
                print(f'{e}{DEFAULT}')
                exit(99)

        print(doUpdate)
        print(lastDate)
        if doUpdate == 'y': # Call update function with data startdate
            update(lastDate)
        else:
            print(f'{BLUE}Not updating! Closing updater.{DEFAULT}')
            exit(0)

    elif lastDate is None:
        print(f'{YELLOW}Data does not exist. Do you wish to crawl the data from earliest known date?')
        print(f'{BLUE}Note: This will take {DEFAULT}' + str((DAYS_SINCE_FIRST / 60 / 60)) + f' {BLUE}hours.')
        while True:
            try:
                doUpdate = input(f'Create full dataset? ({DEFAULT}Y/N{BLUE}):{DEFAULT} ').lower()
                if doUpdate == 'y':
                    update(None)  # Call update function with no startdate for full crawl
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

# Update data. Either second or last in callstack.
def update(lastDate):
    if lastDate is not None:
        startDate = lastDate + DELTA # start from the next day from data
    else:
        startDate = dt.datetime(2007,10,1) # full crawl, completely rebuild data from first known entry

    # update data with new data startdate
    while (startDate <= TODAY):
        sleep(1)
        header = {'User-Agent':str(UserAgent().random)}
        r = requests.post(URL, headers=header, data=data)
        df_list = pd.read_html(r.text)
        df = df_list[2]
        df['Date'] = startDate
        df.rename(columns={'ASB KiwiSaver Scheme fund':'Scheme', 'Sell price':'Price'}, inplace=True)
        startDate += DELTA
        data['currentDay'], data['currentMonth'], data['currentYear'] = startDate.day, startDate.month, startDate.year
        df.to_csv('Data\Kiwisaver Data.csv', index=False, mode='a', header=False)
        print(f'{BLUE}Entry for {DEFAULT}{(startDate-DELTA).strftime("%Y-%m-%d")}{BLUE} added!{DEFAULT}')

if __name__ == '__main__':
    just_fix_windows_console()
    try:
        main()
    except KeyboardInterrupt:
        print(f'\n{RED}Keyboard Interrupt ({DEFAULT}Ctrl+C{RED}) detected. Closing program.{DEFAULT}')
        exit(0)