# ===========================================================================
#  ?                                ABOUT
#  @author         : Nathan Hines
#  @email          : nathan@hines.net.nz
#  @repo           : https://github.com/zerrissen/kiwigrapher
#  @description    : Verifier program to remove anomolous data.
# ===========================================================================

import math

from .. import UNVERIFIED_DIR, VERIFIED_DIR, os, pd


class Verify:
    def __init__(self):
        verify()


def verify():
    print("Not working yet.")
    # df = pd.read_csv(os.path.join(DATA_DIR, "Kiwisaver Data.csv"))
    # iterate through data and check for anomalies.
    # correct anomalies using the mean of the data from 3 days either side of the point.
    # if the days either side of the point can also be anomalous, skip and continue to the next valid point.
