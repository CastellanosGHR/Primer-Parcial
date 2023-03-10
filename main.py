# Programación de computadores - Grupo II
# Nicolás Andrés Castellanos Rico    1094245550
# Juan David Buitrago Salazar        1011096514
# Juan David Castañeda Cárdenas      1014976113
# Santiago Pinilla Ruiz              1077225805
# Juan Diego Mendoza                 1029720696


def gregorian(day_, month_, year_, leap_):
    days = [31, 29 if leap_ else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day_ > days[month_ - 1]:
        return "\033[31m" + "That day does not exist!" + "\033[0m"
    
    months = [0, 3, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6] if leap_ else [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    month_ = months[month_ - 1]
    result = (day_ + month_ + 5 * ((year_ - 1) % 4) + 4 * ((year_ - 1) % 100) + 6 * ((year_ - 1) % 400)) % 7

    return "\033[32m" + f"The day is {week[result]} according to the gregorian calendar." + "\033[0m"


def julian(day_, month_, year_, leap_):
    days = [31, 29 if leap_ else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day_ > days[month_ - 1]:
        return "\033[31m" + "That day does not exist!" + "\033[0m"
    
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    result = (day_ + (153 * (month_ + 12 * ((14 - month_) // 12) - 3) + 2) // 5 + 365 *
              (year_ + 4800 - (14 - month_) // 12) + (year_ + 4800 - (14 - month_) // 12)
              // 4 - (year_ + 4800 - (14 - month_) // 12) // 100 +
              (year_ + 4800 - (14 - month_) // 12) // 400 - 32045) % 7
    
    return "\033[32m" + f"The day is {week[result]} according to the julian calendar." + "\033[0m"


while True:
    date = input("\033[0m" + ">>> " + "\033[35m" + "Type a date in the " + "\033[33m" + "dd/mm/yyyy" +
                "\033[35m" + " format or press" + "\033[33m" + " (ENTER or ctrl + c)" + "\033[35m" +
                " to quit: " + "\033[36m")
    
    if date == "":
        exit()

    day = month = year = None

    try:
        (day, month, year) = (int(number) for number in date.split("/"))
    except ValueError:
        print("\033[31m" + "Your did not enter a valid input. Try again." + "\033[0m")
        continue

    if day < 0 or month not in range(0, 13):
        print("\033[31m" + "This date is not valid! Try again." + "\033[0m")
        continue

    if (year == 1582 and month == 10 and day in range(5, 15)) or (year < -45):
        print("\033[31m" + "This date does not exist! Try again." + "\033[0m")
        continue

    if (day >= 15 and month >= 10 and year == 1582) or (year > 1582):
        leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        print(gregorian(day, month, year, leap))
        continue

    elif (day <= 4 and month <= 10 and year == 1582) or (year < 1582):
        leap = year % 4 == 0
        print(julian(day, month, year, leap))
        continue
