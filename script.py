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

#1
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

#2
visits_cart = visits.merge(cart, how= "left")

#3
lenght = len(visits_cart)
print(lenght)

#4
null_timestamps = visits_cart[visits_cart.cart_time.isnull()].count()
print(null_timestamps)

#5
percent_visitor_without_order = null_timestamps / float(lenght)
print(percent_visitor_without_order)

#6
checkout_cart = cart.merge(checkout, how= "left")

lenght_checkout_cart = len(checkout_cart)
print(lenght_checkout_cart)

null_timestamps_checkout_cart = checkout_cart[checkout_cart.checkout_time.isnull()].count()
print(null_timestamps_checkout_cart)

percent_cart_without_checkout = null_timestamps_checkout_cart / float(lenght_checkout_cart)
print(percent_cart_without_checkout)

#7
all_data = visits.merge(cart, how = "left").merge(checkout, how = "left").merge(purchase, how = "left")
print(all_data.head())

#8
all_data["count_num"]= all_data.checkout_time.isnull()
checkout_no_purchase = all_data[all_data.count_num == False].count()
print(checkout_no_purchase)
purchase_overall = all_data.purchase_time.count()
percent_checkout_purchase = purchase_overall / checkout_no_purchase
print(percent_checkout_purchase)

#10
all_data["diff_time"] = all_data.purchase_time - all_data.visit_time

#11
print(all_data)

#12 0 days 00:43:53.360160
avg_time = all_data["diff_time"].mean()
print(avg_time)

