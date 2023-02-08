import math

from .. import DATA_DIR, os, pd


class Verify:
    def __init__(self):
        verify()


def verify():
    df = pd.read_csv(os.path.join(DATA_DIR, "Kiwisaver Data.csv"))
    # iterate through data and check for anomalies.
    # correct anomalies using the mean of the data from 3 days either side of the point.
    # if the days either side of the point can also be anomalous, skip and continue to the next valid point.
