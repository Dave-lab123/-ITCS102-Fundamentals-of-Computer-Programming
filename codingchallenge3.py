Sender_name = input("Enter sender's name: ")
Type_of_package = input("Enter package name: ")
weight = float(input("Enter package weight in kg: "))
distance = float(input("Enter distance to destination in km: "))
fragile = input("Is the package fragile? (yes/no): ")
is_express = input("Is the package express? (yes/no): ")
is_international = input("Is the package international? (yes/no): ")

Base_cost = (weight * 2.5) + (distance * 0.15)
if is_express == "no" and is_international == "no" and weight <= 2 and distance <= 100: #free shipping
 Total_cost = 0
 print("Free Shipping")
elif is_express == "yes" and is_international == "yes" : #express and international shipping
 Total_cost = (Base_cost * 1.4) + 50
 print("Express and International Shipping Cost: ", Total_cost)
elif is_express == "yes"  or is_international == "yes" and weight > 20 : #express or international shipping with heavy package
 Total_cost = (Base_cost * 1.2) + 25
 print("Express or Heavy International Shipping Cost : ", Total_cost)
elif weight > 30 or distance > 1000: #heavy or long distance shipping
 Total_cost = (Base_cost) + 30
 print("Heavy or Long Distance Shipping Cost: ", Total_cost)
else:  #standard shipping
 print("Standard Shipping Cost: ", Base_cost)