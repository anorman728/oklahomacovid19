# oklahomacovid19
Just a small matplotlib chart of new Oklahoma covid-19 cases.

UPDATE, 4/13/2020:  I just noticed that Oklahoma has finally decided to add this information to their page (except as a bar chart instead of a line chart for some odd reason).  I'll go ahead and keep this running for the time being, but I'll probably stop the regular updates in the near-ish future.

![New Cases of Covid-19 in Oklahoma](/covid19oklahoma.png)


This data comes from the graph at the bottom of this page: https://coronavirus.health.ok.gov/

That graph is the only *historical* data for Oklahoma that I can find.
Everything else is only current.

What that graph shows is only *cumulative* counts of cases.  I've done the
subtraction on each successive day to find the counts of new cases per day.

If you want to check my work, take a look at the covid19timeline.py.
