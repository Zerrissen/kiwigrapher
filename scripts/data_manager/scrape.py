from time import sleep

import requests
from fake_useragent import UserAgent

from .. import (DATA_DIR, DAYS_SINCE_FIRST, DELTA, FIRST_ENTRY, TODAY, URL, dt,
                os, pd)


class Scrape:
    def __init__(self):
        scrape()


def scrape():
    data = {
        'currentDay': 1,
        'currentMonth': 10,
        'currentYear': 2007
    }
    startDate = dt.datetime(2007, 10, 1)

    while startDate < TODAY:
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
        df.to_csv(os.path.join(DATA_DIR, 'Kiwisaver Data.csv'),
                  index=False, mode='a', header=False)
        print(
            f'Entry for {(startDate-DELTA).strftime("%Y-%m-%d")} added!')
    print('Scrape compelte!')
