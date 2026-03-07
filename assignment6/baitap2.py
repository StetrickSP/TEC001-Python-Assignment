# Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.

seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month number (1-12): "))

if month == 12 or month == 1 or month == 2:
    season = seasons[0]
elif month >= 3 and month <= 5:
    season = seasons[1]
elif month >= 6 and month <= 8:
    season = seasons[2]
elif month >= 9 and month <= 11:
    season = seasons[3]

print("Season:", season)