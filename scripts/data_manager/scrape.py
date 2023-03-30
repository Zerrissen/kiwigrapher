# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Data scraper, scrapes raw ASB data to unverified data folder.
# ===========================================================================

from time import sleep

import requests
from fake_useragent import UserAgent

from .. import UNVERIFIED_DIR, DELTA, TODAY, URL, dt, os, pd


class Scrape:
    def __init__(self):
        scrape()


def scrape():
    print('Note that this will be raw data and may contain anomolies.')
    print('To remove the anomolies, run the "Verify" option in the menu.')

    data = {
        'currentDay': 1,
        'currentMonth': 10,
        'currentYear': 2007
    }
    startDate = dt.datetime(2007, 10, 1)

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
    print('Scrape compelte!')
