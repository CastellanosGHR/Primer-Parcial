# March the ninth, 2023. 3:11 p.m

def gregorian(day_, month_, year_, leap_):
    w31days = (1, 3, 5, 7, 8, 10, 12)
    w30days = (4, 6, 9, 11)
    if (day_ > 31 and month_ in w31days) or (day_ > 30 and month_ in w30days) or (day_ > 29 and month_ == 2):
        print("That day does not exist!")
        return -1
    if leap_:
        months = {1: 0, 2: 3, 3: 4, 4: 0, 5: 2, 6: 5, 7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6}
    else:
        months = {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}
    week = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    month_ = months[month_]
    result = (day_ + month_ + 5 * ((year_ - 1) % 4) + 4 * ((year_ - 1) % 100) + 6 * ((year_ - 1) % 400)) % 7
    print(f"The day is {week[result]}.")


while True:
    date = input("Type a date en the dd/mm/yyyy format: ")
    try:
        (day, month, year) = (int(number) for number in date.split("/"))
        if day < 0 or month not in range(0, 13) or year < -46:
            print("Your did not enter a valid input. Try again.")
            raise ValueError
        if (day >= 14 and month >= 10 and year == 1582) or (year > 1582):
            leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            gregorian(day, month, year, False)
            continue
    except ValueError:
        continue

# March the ninth, 2023. 5:50 p.m
