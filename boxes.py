import math

number_of_items = int(input("Enter number of items : "))
items_per_box = int(input("Enter number of items per box : "))

boxes_needed = number_of_items / items_per_box

print(f"For {number_of_items} items, packing {items_per_box} items in each box, you will need {math.ceil(boxes_needed)} boxes.")