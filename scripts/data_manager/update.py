from time import sleep

import requests
from fake_useragent import UserAgent

from .. import UNVERIFIED_DIR, DELTA, TODAY, URL, os, pd


class Update:
    def __init__(self):
        if os.path.exists(os.path.join(UNVERIFIED_DIR, 'Kiwisaver Data.csv')):
            update()
        else:
            print('Data file not found. Please scrape first.')

# ================================================
#  *                  update
#  ? Updates already-scraped, unverified data
#  @ param None
#  @ return None
# ================================================


def update():
    # Variable definitions for update loop.
    df = pd.read_csv(os.path.join(UNVERIFIED_DIR, 'Kiwisaver Data.csv'))
    lastDate = pd.to_datetime(df['Date'].iloc[-1], format='%Y-%m-%d')
    startDate = lastDate + DELTA
    data = {
        'currentDay': startDate.day,
        'currentMonth': startDate.month,
        'currentYear': startDate.year
    }

    # Loop to continue scraping from the last saved date until the current date.
    print(f'Scraping {startDate} to {TODAY}')
    while startDate < TODAY:
        print("Estimated time remaining: ",
              str(((((TODAY - startDate).days) * 1.5)/60)) + " minutes")
        sleep(0.5)
        header = {'User-Agent': str(UserAgent().random)}
        r = requests.post(URL, headers=header, data=data)
        df_list = pd.read_html(r.text)
        df = df_list[2]
        df['Date'] = startDate
        df.rename(columns={'ASB KiwiSaver Scheme fund': 'Scheme',
                  'Sell price': 'Price'}, inplace=True)
        startDate += DELTA
        data['currentDay'], data['currentMonth'], data['currentYear'] = startDate.day, startDate.month, startDate.year
        df.to_csv(os.path.join(UNVERIFIED_DIR, 'Kiwisaver Data.csv'),
                  index=False, mode='a', header=False)
        print(
            f'Entry for {(startDate-DELTA).strftime("%Y-%m-%d")} added!')
    print('Update complete! Please run the Verify option to remove anomolies.')
