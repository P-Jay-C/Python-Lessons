def leap_year(num):
    if (num % 4) == 0:
        if (num % 100) == 0:
            if (num % 400) == 0:
                print(num, " is a leap year")
            else:
                print(num, " is not a leap year")
        else:
            print(num, " is a leap year")
    else:
         print(num, " is not a leap year")


leap_year(2000)
