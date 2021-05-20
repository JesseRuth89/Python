def is_leap(year) -> bool:
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = True
        elif year % 400 == 0:
            leap = True
    else:
        leap = False
    return leap


assert is_leap(2000) == True
assert is_leap(2400) == True
assert is_leap(2500) == False
