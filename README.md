# oklahomacovid19
Just a small matplotlib chart of new Oklahoma covid-19 cases.

![New Cases of Covid-19 in Oklahoma]('./covid19oklahoma.png')


This data comes from the graph at the bottom of this page: https://coronavirus.health.ok.gov/

That graph is the only *historical* data for Oklahoma that I can find.
Everything else is only current.

What that graph shows is only *cumulative* counts of cases.  I've done the
subtraction on each successive day to find the counts of new cases per day.

If you want to check my work, take a look at the covid19timeline.py.
