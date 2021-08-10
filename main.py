# if __name__ == '__main__':

# library imports
from calendar import monthrange

# Taking_in_User Input:
dateOfBirth = input("What is your date of birth? (Enter in mm/dd/yyyy format):\n")
dateOfBirthSplit = dateOfBirth.split("/");

month = int(dateOfBirthSplit[0])
day = int(dateOfBirthSplit[1])
year = int(dateOfBirthSplit[2])
shortYear = int(year % 10)
century = int(year / 100)
dayOfBirth = str("")
list = []
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def is_leap_year(userYear):
    if userYear % 400 == 0:
        return True
    elif userYear % 100 == 0:
        return False
    elif userYear % 4 == 0:
        return True
    else:
        return False


def get_month_code(userMonth, userYear):
    number: int = 0
    if userMonth == 1:
        return 0
    for i in range(1, userMonth):
        if not is_leap_year(userYear):
            number = ((number + (monthrange(userYear, i)[1])) % 7)
        else:
            number = ((number + (monthrange(userYear - 1, i)[1])) % 7)
    return number


def get_century_code(userYear):
    return int(6 - (2 * (int((userYear / 100)) % 4)))


def get_birthday_week_value(userMonth, userDay, userYear):
    CalenderCalc = int(
        (userYear % 100) + ((userYear % 100) / 4) + userDay + get_month_code(userMonth, userYear) + get_century_code(
            userYear))
    if is_leap_year(userYear) and userMonth <= 2:
        return (CalenderCalc % 7) - 1
    else:
        return CalenderCalc % 7


def get_birthday_week_day(userMonth, userDay, userYear):
    week = weekdays[get_birthday_week_value(userMonth, userDay, userYear)]
    return week


def get_consecitive_same_day_birthday(userMonth, userDay, userYear):
    listOfSameDayBirthday = []
    for i in range(userYear, userYear + 100):
        if userDay <= monthrange(i, userMonth)[1]:
            if get_birthday_week_value(userMonth, userDay, i) == get_birthday_week_value(userMonth, userDay, userYear):
                listOfSameDayBirthday.append(str(i))
    return listOfSameDayBirthday



print("You were born on a:" + " " +get_birthday_week_day(month, day, year))
print()
print("These years you will have birthday on a " + "" + get_birthday_week_day(month, day, year) + ":")
print(*get_consecitive_same_day_birthday(month, day, year), sep="\n")
