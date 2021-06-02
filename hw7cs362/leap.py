def leapyr(num):
    if num % 400 == 0:
        return(num, "is a leap year!!")
    elif num % 100 == 0:
        return(num, "is not a leap year")
    elif num % 4 == 0:
        return(num, "is a leap year!!")
    else:
        return(num, "is not a leap year")


