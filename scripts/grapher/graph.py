# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Graphing program for stored ASB Kiwisaver data using Matplotlib and Pandas
# ===========================================================================
from .. import UNVERIFIED_DIR, VERIFIED_DIR, os, pd, plt


class Graph:
    def __init__(self, verifType):
        graph(verifType)

# ================================================
#  *                  graph
#  ? Graphs either verified or unverified data
#  @ param verifType string
#  @ return None
# ================================================


def graph(verifType):
    try:
        if verifType == 'verified':
            df = pd.read_csv(os.path.join(VERIFIED_DIR, 'Kiwisaver Data.csv'))
        elif verifType == 'unverified':
            df = pd.read_csv(os.path.join(
                UNVERIFIED_DIR, 'Kiwisaver Data.csv'))
        else:
            raise Exception()
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.pivot_table(index='Date', columns='Scheme',
                            values='Price').resample('D').mean()
        df.plot(kind='line')
        plt.legend(loc='upper left')
        plt.title('Kiwisaver Fund Unit Prices Over Time')
        plt.ylabel('Unit Price (NZD$)')
        plt.show()
    except Exception as e:
        pass
