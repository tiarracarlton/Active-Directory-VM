def leap_year(year):
    year = int(year)
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return bool(leap_year)
    else:
        return False
        
print(leap_year)