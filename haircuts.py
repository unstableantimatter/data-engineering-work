hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_revenue = 0
total_price = 0
num_prices = len(prices)

for p in prices:
  total_price += p
  print(total_price)

average_price = total_price / num_prices
print("Average Haircut Price: " + str(average_price))

new_prices = [x - 5 for x in prices]
#print(new_prices)

s = len(hairstyles)
#print(s)

i = range(s)
#print(i)

for x in i:
  total_revenue += (prices[x] * last_week[x])
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("7 Day Average Daily Revenue: " + str(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print("Haircut Deals Under $30: " + str(cuts_under_30))
