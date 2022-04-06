"""
1. python variables can only begin with alphabets or an _(underscore)
2. python variables are also called as identifiers

"""
plyrName = "Sachin"
print(f"plyrName :{plyrName}")
print("-" * 40)

player_count = 11
print(f"player_count :{player_count}")
print("-" * 40)

team = "India"
print(f"team :{team}")
print("-" * 40)

has_won_WC = True
print(f"Has won a World Cup :{has_won_WC}")
print("-" * 40)

team_rating = 8.3
print(f"team rating :{team_rating}")
print("-" * 40)

print(f"Module Name :{__name__}")
# __name__ = Double Underscore Name => dunder-name

print("-" * 40)
# invalid
# 3plyr = "Rahul"
# print(f"3rd Player :{3plyr}")
# @plyr = "Rahul"
# print(f"3rd Player :{@plyr}")

a, b, c = 10, "Hello", True
print(f"a :{a}")
print(f"b :{b}")
print(f"c :{c}")

print("-" * 40)
a = b = c = 256
print(f"a :{a}")
print(f"b :{b}")
print(f"c :{c}")

print("-" * 40)
first_name = "Sachin"
last_name = "Tendulkar"
print("Name of the player is " + first_name + " and he is more familiar as " + last_name)
print("Name of the player is", first_name , "and he is more familiar as" ,last_name)

# interpolation
print(f"Name of the player is {first_name} and he is more familiar as {last_name}")

print("-" * 40)
fruit = "apple"
print(f"the cost of {fruit} is {150 - (150 * 0.1)}")
print(f"the cost of {fruit} is {150 * 0.9}")

print("-" * 40)
print(f"The players belong to team :{team}")
print(f"The players belong to team '{team}'")
print(f'The players belong to team "{team}"')
print(f'The players belong to team :\'{team}\'')

