import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message



date = dt.date.today()
time = f"The current time is " + str(dt.datetime.now().time())
cost = 1000
current_year = int(date.strftime("%Y"))
target_year = randint(1900, 2200)
time_differential = abs(current_year - target_year)
print(time_differential)
poss_destinations = ["Moon", "Sun", "Rio", "Portugal", "North Korea"]

destination = choice(poss_destinations)
print(f"You chose to travel to " + destination)

base_cost = Decimal(1000.000)
cost_multiplier = 1.0 + (abs(time_differential * 0.01))
print(cost_multiplier)

final_cost = cost * cost_multiplier
print(f"Final Cost: " + f"{final_cost:.2f}")

print(date)
print(time)


print(generate_time_travel_message(target_year, destination, final_cost))
