import datetime as dt

"""
Expected output:
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
"""
def format_ft_time():
	start = dt.datetime(1970, 1, 1)
	end = dt.datetime.now()
	difference = (end - start).total_seconds()

	start_output = dt.datetime.strftime(start,"%B %-d, %Y")
	print("Seconds since {0:}: {1:,.4f} or {1:.2e} in scientific notation".format(start_output, difference))
	print("{0:}".format(end.strftime("%b %-d %Y")))

format_ft_time()
