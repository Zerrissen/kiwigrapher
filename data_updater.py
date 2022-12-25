import requests
import pandas as pd
import datetime as dt
from os import path
from time import sleep
from fake_useragent import UserAgent

# Constant, never changes from this point. Accessed by multiple functions.
URL = "https://www.asb.co.nz/iFrames/investmentPerformance.asp"
TODAY = dt.datetime.today()
DELTA = dt.timedelta(days=1)
FIRST_ENTRY = dt.datetime(2007, 1, 10)
DAYS_SINCE_FIRST = (TODAY - FIRST_ENTRY).days # Number of days since the first known Kiwisaver Data entry from ASB

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
        if path.exists('Kiwisaver Data.csv'):
            print('Already exists!')
            print('Checking date..')
            df = pd.read_csv('Kiwisaver Data.csv')
            print(df['Date'].iloc[-1])
            lastDate = pd.to_datetime(df['Date'].iloc[-1], format='%Y-%m-%d')
            # If data is out of date, check if user wishes to update
            if lastDate < dt.datetime.today():
                checkUpdate(lastDate)
            else:
                print('Data is up to date. Closing updater.')
                exit(0)
        # If data does not exist, create csv and ask if user wants a full crawl
        else:
            with open('Kiwisaver Data.csv', 'w') as file:
                file.write('Scheme,Price,Date\n')
            checkUpdate(None)
    except IndexError:
        print('No date entered. Assuming no data.')
        pass
    except Exception as e:
        print("Oops an error happened")
        print(e)
        exit(0)
    checkUpdate(None) # full update if IndexError

# Check if the user wishes to update. Either second in callstack, or not called.
def checkUpdate(lastDate):
    if lastDate is not None:
        print('Data is out of date. Last known date is ' + str(lastDate))
        while True:
            try:
                doUpdate = input('Update list? (Y/N): ').lower()
                if doUpdate == 'y':
                    update(lastDate) # Call update function with data startdate
                elif doUpdate == 'n':
                    print('Not updating! Closing updater.')
                    exit(0)
                else:
                    print('Unknown option. Try again.')
                    continue
            except Exception as e:
                print('Uh oh, an error occurred! Closing program.')
                print(e)
                exit(99)
    else:
        print('Data does not exist. Do you wish to crawl the data from earliest known date?')
        print('Note: This will take ' + str((DAYS_SINCE_FIRST / 60 / 60)) + ' hours.')
        while True:
            try:
                doUpdate = input('Create full dataset? (Y/N): ').lower()
                if doUpdate == 'y':
                    update(None)  # Call update function with no startdate for full crawl
                elif doUpdate == 'n':
                    print('Not creating data. Closing updater.')
                    exit(0)
                else:
                    print('Unknown option. Try again.')
                    continue
            except Exception as e:
                print('Uh oh, an error occurred! Closing program.')
                print(e)
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
        df.to_csv('Kiwisaver Data.csv', index=False, mode='a', header=False)
        startDate += DELTA
        data['currentDay'], data['currentMonth'], data['currentYear'] = startDate.day, startDate.month, startDate.year
        print('Entry for ' + str(startDate) + ' added!')

if __name__ == '__main__':
    main()