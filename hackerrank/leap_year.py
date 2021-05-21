"""
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
"""
import calendar
def is_leap(year) -> bool:
    """ This is 'stupid' be smart with returns
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    """
    # import the calendar dummy
    # return calendar.isleap(year)
    # single line
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

print(is_leap(2500))
