# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Graphing program for stored ASB Kiwisaver data using Matplotlib and Pandas,
# ===========================================================================
import matplotlib.pyplot as plt
import pandas as pd


def main():
    df = pd.read_csv('Data\Kiwisaver Data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.pivot_table(index='Date', columns='Scheme',
                        values='Price').resample('D').mean()
    df.plot(kind='line')
    plt.legend(loc='upper left')
    plt.style.use('ggplot')
    plt.title('Kiwisaver Fund Unit Prices Over Time')
    plt.ylabel('Unit Price (NZD$)')
    plt.show()


if __name__ == '__main__':
    main()
