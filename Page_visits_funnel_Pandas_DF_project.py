## page visits funnel project

import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])


visits_cart = pd.merge(visits, cart, how='left')
print(len(visits_cart))

count_cart = visits_cart['cart_time'].notna().sum()
count_visit = visits_cart['visit_time'].notna().sum()

visit_cart_per = (count_cart / count_visit) * 100
print(visit_cart_per)

cart_checkout = pd.merge(cart, checkout, how='left')
print(len(cart_checkout))

count_cart_checkout = len(cart_checkout) - sum(cart_checkout['checkout_time'].notna())

print(count_cart_checkout)

cart_checkout_per = (count_cart_checkout / len(cart_checkout)) * 100
print(cart_checkout_per)

all_data = visits.merge(cart, how='left')\
  .merge(checkout, how='left')\
  .merge(purchase, how='left')

print(all_data.head())


# Count non-null values in each column
count_A = all_data['visit_time'].count()
count_B = all_data['cart_time'].count()
count_C = all_data['checkout_time'].count()
count_D = all_data['purchase_time'].count()

# Calculate percentage of non-null values in column_A relative to column_B
percent_checkout_nopurchase = (count_D / count_C) * 100 if count_C != 0 else 0
print(percent_checkout_nopurchase)

percent_visit_nocart = (count_B / count_A) * 100 if count_B != 0 else 0
print(percent_visit_nocart)

percent_cart_nocheckout = (count_C / count_B) * 100 if count_C != 0 else 0
print(percent_cart_nocheckout)

all_data['shopping_time'] = all_data.purchase_time - all_data.visit_time

print(all_data.shopping_time)

print(all_data.shopping_time.mean())


