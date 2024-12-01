weight = 41.5
premium = 125

# Ground shipping
if weight <= 2:
  cost = (1.5 * weight) + 20
elif weight <= 6:
  cost = (3 * weight) + 20
elif weight <= 10:
  cost = (4 * weight) + 20
elif weight > 10:
  cost = (4.75 * weight) + 20
else:
  print("Please enter a weight.")

# Drone Shipping
if weight <= 2:
  dcost = 4.5 * weight
elif weight <= 6:
  dcost = 9 * weight
elif weight <= 10:
  dcost = 12 * weight
elif weight > 10:
  dcost = 14.25 * weight
else:
  print("Please enter a weight.")

print(cost)
print(dcost)
print(premium)

