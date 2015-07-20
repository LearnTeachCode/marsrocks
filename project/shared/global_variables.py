import datetime

def get_current_year():
    #Flora, do your code here and set your end result to year.
    # year = {% now "Y" %}

	now = datetime.datetime.now()
	year = now.year

	return dict(current_year=year)
