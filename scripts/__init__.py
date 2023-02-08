import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import os

# ======== CONSTANTS =========
DELTA = dt.timedelta(days=1)
TODAY = dt.datetime.today()
FIRST_ENTRY = dt.datetime(2007, 1, 10)
DAYS_SINCE_FIRST = (TODAY - FIRST_ENTRY).days
URL = "https://www.asb.co.nz/iFrames/investmentPerformance.asp"
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), os.pardir, 'data', 'unverified'))
