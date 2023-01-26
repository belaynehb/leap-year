year = int(input("What year you would like to check if it is a leap year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is leap year")
else:
    print("It is not a leap year")

