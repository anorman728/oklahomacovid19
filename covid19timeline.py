#!/usr/bin/python3

from datetime import datetime
from datetime import timedelta

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

# Starting date is '3/7/2020'
startingdate = datetime(2020, 3, 7)

# This data comes from the graph at the bottom of this page: https://coronavirus.health.ok.gov/

# That graph is the only *historical* data for Oklahoma that I can find.
# Everything else is only current.

# What that graph shows is only *cumulative* counts of cases.  I've done the
# subtraction on each successive day to find the counts of new cases per day.

cumulativeCount = [
    0, # Presumably starting with zero cases.
    1,
    1,
    1,
    2,
    2,
    2,
    3,
    4,
    7,
    10,
    17,
    29,
    44,
    49,
    53,
    67,
    81,
    106,
    164,
    248,
    322,
    377,
    429,
    481,
    565,
    719,
    879,
    988,
    1159,
    1252,
    1327,
    1472,
]

# Because I keep forgetting what these are called-- "List comprehensions"

caseCountPerDay = [cumulativeCount[i] - cumulativeCount[i-1] for i in range(1, len(cumulativeCount))]

dates = [(startingdate + timedelta(days=i)).strftime('%m/%d') for i in range(0, len(caseCountPerDay))]

fig = plt.figure()

plt.xticks(rotation=60)

plt.plot(dates, caseCountPerDay)
#plt.show()
fig.savefig('covid19oklahoma.png')
