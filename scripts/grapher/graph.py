# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Graphing program for stored ASB Kiwisaver data using Matplotlib and Pandas
# ===========================================================================
from .. import UNVERIFIED_DIR, os, pd, plt


class Graph:
    def __init__(self):
        graph()

# ================================================
#  *                  graph
#  ? Graphs the data
#  @ param None
#  @ return None
#  todo: Allow the user to choose between unverified and verified
# ================================================


def graph():
    df = pd.read_csv(os.path.join(UNVERIFIED_DIR, 'Kiwisaver Data.csv'))
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.pivot_table(index='Date', columns='Scheme',
                        values='Price').resample('D').mean()
    df.plot(kind='line')
    plt.legend(loc='upper left')
    plt.title('Kiwisaver Fund Unit Prices Over Time')
    plt.ylabel('Unit Price (NZD$)')
    plt.show()
