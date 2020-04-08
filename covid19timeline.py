#!/usr/bin/python3

# Date stuff
from datetime import datetime
from datetime import timedelta

# Graph stuff
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

# Data stuff
import json

# Starting date is '3/7/2020'
startingdate = datetime(2020, 3, 7)

# This data comes from the graph at the bottom of this page: https://coronavirus.health.ok.gov/

# That graph is the only *historical* data for Oklahoma that I can find.
# Everything else is only current.

# What that graph shows is only *cumulative* counts of cases.  I've done the
# subtraction on each successive day to find the counts of new cases per day.

with open('covid19counts.json') as f:
    cumulativeCount = json.load(f)

# Because I keep forgetting what these are called-- "List comprehensions"

# Get data
caseCountPerDay = [cumulativeCount[i] - cumulativeCount[i-1] for i in range(1, len(cumulativeCount))]
dates = [(startingdate + timedelta(days=i)).strftime('%m/%d') for i in range(0, len(caseCountPerDay))]

# Build figure
fig = plt.figure()

# Build actual plot.

plt.xticks(rotation=60)
updatedtime = 'Updated ' + datetime.now().strftime('%Y/%m/%d')
plt.figtext(0.99, 0.95, updatedtime, horizontalalignment='right')
plt.plot(dates, caseCountPerDay)

#plt.show()
fig.savefig('covid19oklahoma_test.png')
