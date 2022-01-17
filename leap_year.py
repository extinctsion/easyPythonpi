def check_leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return ("This is a leap year!!")
    else:
        return("This is not a leap year!!")


