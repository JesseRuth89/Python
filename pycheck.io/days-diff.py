#Importing date from datetime
#https://docs.python.org/2/library/datetime.html#
from datetime import date

#Import the passed vars as dates
def days_diff(a, b):
    """
    my orginal method but you can unpack tuples with *tuple
    a = date(a[0], a[1], a[2])
    b = date(b[0], b[1], b[2])
    c = a - b
    """
    """
    While this is still better, you can one liner it
    a = date(*a)
    b = date(*b)
    c = a - b
    #Returns absolute value
    return(abs(c.days))
    """
    #Single line return, most elegant
    return(abs((date(*a)- date(*b)).days))

if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
