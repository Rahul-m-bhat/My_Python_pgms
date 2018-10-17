#To check if the year is Leap year or not.
###In the Gregorian calendar three criteria must be taken into account to identify leap years:
               #   1) The year can be evenly divided by 4;
               #   2)If the year can be evenly divided by 100, it is NOT a leap year, unless;
               #   3)The year is also evenly divisible by 400. Then it is a leap year.
# there is a leap year every year divisible by four except for years which are both divisible by 100 and not divisible by 400


def leap_year(year):
	leap = True
	if year%4 == 0 and (year%400 == 0 or year%100 != 0):
		leap = True
	else:
		leap = False
	return("Year %s is a leap year: %s" % (year,leap))
		


year = int(input("Year to be checked:"))
check = leap_year(year)
print(check)





