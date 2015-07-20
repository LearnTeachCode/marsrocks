import datetime

def get_current_year():

	now = datetime.datetime.now()
	year = now.year

	return dict(current_year=year)
