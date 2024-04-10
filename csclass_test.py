def things():
    while True:
        age = int(input("What is your age? "))
        date = input("What day of the week is it? ")
        if age < 1:
            print("You are too small. Try again. ")
            continue
        if date == "Monday" or date == "monday" or date == "mon" or date == "Mon" or date == "Tuesday" or date =="tuesday" or date == "Tues" or date == "tues" or date == "Wednesday" or date == "wednesday" or date == "Wed" or date == "wed" or date == "Thursday" or date == "thursday" or date == "Thurs" or date == "thurs" or date == "Friday" or date == "friday" or date == "Fri" or date == "fri":
            price = 1
        elif date == "Sunday" or date == "sunday" or date == "Sun" or date == "sun" or date == "Saturday" or date == "saturday" or date == "Sat" or date == "sat":
            price = 1.5
        else:
            print("I don't know what day of the week " + date + " is. Please write as Monday/monday/Mon/mon and try again. ")
            continue

        if age <= 13:
            final = price * 0.5
        elif age > 13 and age <=64:
            final = price * 1
        else:
            final = price * 0.7
        print("Your price is $" + str(round((final * 10),2)) + ". ")
        if input("Do you want to try again? (y/n) ") == "y":
            continue
        else:
            break

things()
    
