"""
Pseudocode
input num_items == -1
While num_items < 0:
if number
convert it to an integer
else
display an error message

total_price == 0.0
for i in range(num_items)
Initialize price == -1.
While price < 0
input the price of the 'i+1' item
if valid number
convert
else
display an error message
if total_price > 100
reduce total_price by 10%
Display final total price
"""
num_items = -1
while num_items < 0:
    num_items = input("Number of items: ")
    if num_items.isdigit():
        num_items = int(num_items)
    else:
        print("Invalid number of items.")

total_price = 0.0

for i in range(num_items):
    price = -1
    while price < 0:
        item_price = input(f"Price of item {i + 1}: $")
        if item_price.replace('.', '', 1).isdigit():
            price = float(item_price)
        else:
            print("Invalid price.")

    total_price += price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {num_items} items is ${total_price:.2f}")

