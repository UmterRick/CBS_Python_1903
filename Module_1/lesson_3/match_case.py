# switch - case

day = int(input("Week day: "))

if day == 1:
    print("Monday, start working")
elif day == 2:
    print("Tuesday, continue working")
elif day == 3:
    print("Wednesday, continue working")
elif day == 4:
    print("Thursday, continue working")
elif day == 5:
    print("Friday, continue working")
elif day == 6:
    print("Saturday, wow")
elif day == 7:
    print("Sunday, continue working")
else:
    print("Use numbers from 1 to 7")
    exit()


match day:
    case 1:
        print("Monday, start working")
    case 2:
        print("Tuesday, continue working")
    case 3:
        print("Wednesday, continue working")
    case 4:
        print("Thursday, continue working")
    case 5:
        print("Friday, continue working")
    case 6:
        print("Saturday, wow")
    case 7:
        print("Sunday, continue working")
    case _:
        print("Use numbers from 1 to 7")
        exit()

