#added code to calculate the diferrence between the sub total and 50 on a tuesday or wednesady
from datetime import date

today = date.today()

day_name = today.strftime("%A")

sub_total = float(input("Enter sub total amount : "))

if day_name == "Tuesday" or day_name == "Wednesday":
    if sub_total >= 50:
        #discount
        discount = (10/100) * sub_total
        
        new_sub_total = sub_total - discount
        
        sales_tax = (6/100) * new_sub_total

        total_amount = new_sub_total + sales_tax
    else:
        #difference
        diferrence = 50 - sub_total
        discount = 0

        sales_tax = (6/100) * sub_total
        
        total_amount = sub_total + sales_tax
        print(f"Add ${diferrence:.2f} to your sub total to apply 10% discount")
else:
    discount = 0

    sales_tax = (6/100) * sub_total
    
    total_amount = sub_total + sales_tax

print(f"Discount : ${discount:.2f}")
print(f"Sales Tax Amount : ${sales_tax:.2f}")
print(f"total Amount Due : ${total_amount:.2f}")

