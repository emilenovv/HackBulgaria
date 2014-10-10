def what_is_my_sign(day, month):
    if month == 3 and day in range(21, 32) or month == 4 and day in range(1, 21):
        return "Ariel"
    if month == 4 and day in range(21, 31) or month == 5 and day in range(1, 22):
        return "Taurus"
    if month == 5 and day in range(22, 32) or month == 6 and day in range(1, 22):
        return "Gemini"
    if month == 6 and day in range(2, 31) or month == 7 and day in range(1, 23):
        return "Cancer"
    if month == 7 and day in range(22, 32) or month == 8 and day in range(1, 23):
        return "Leo"
    if month == 8 and day in range(23, 32) or month == 9 and day in range(1, 24):
        return "Virgo"
    if month == 9 and day in range(24, 31) or month == 10 and day in range(1, 24):
        return "Libra"
    if month == 10 and day in range(24, 32) or month == 11 and day in range(1, 23):
        return "Scorpio"
    if month == 11 and day in range(23, 31) or month == 12 and day in range(1, 22):
        return "Sagittarius"
    if month == 12 and day in range(22, 32) or month == 1 and day in range(1, 21):
        return "Capricorn"
    if month == 1 and day in range(21, 32) or month == 2 and day in range(1, 20):
        return "Aquarius"
    if month == 2 and day in range(20, 28) or month == 3 and day in range(1, 21):
        return "Ariel"


print(what_is_my_sign(30, 6))
