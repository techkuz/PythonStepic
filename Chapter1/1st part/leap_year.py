x = int(input())


year_common = "Обычный"
year_leap = "Високосный"

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print (year_leap)
else:
    print (year_common)

