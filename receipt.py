#added a "return by" date that is 9:00 PM 30 days in the future at the bottom of the receipt.
import csv
from datetime import datetime, timedelta

def main():
    FILE = "products.csv"
    try:
        products_dict = read_dictionary(FILE, 0)
        #the time now to display at the end of the receipt
        now = datetime.now()
        now = now.strftime("%a %b %e %H:%M:%S %Y")
        #return by 30dys
        today = datetime.today()

        future_date = today + timedelta(days=30)
        future = future_date.replace(hour=21, minute=0, second=0, microsecond=0)
        return_by = future.strftime("%b %d %Y %H:%M")

        print("TM PicknPay\n")

        with open("request.csv", "rt") as request:
            total_items = 0 
            subtotal = 0
            tax_rate = 6/100
            requests = csv.reader(request)
            next(requests)
            for line in requests:
                item = line[0] 
                quanity = int(line[1])
                
                name = products_dict[item][1]
                price = products_dict[item][2]
                print(f"{name} : {quanity} @ {price}")

                total_items += quanity
                price_per_product = (float(price) * quanity)
                subtotal += price_per_product

            sales_tax = subtotal*tax_rate

            print(f"Number of items : {total_items}")

            #print subtotal before tax
            print(f"Subtotal : {round(subtotal, 2)}")

            print(f"Sales Tax : {round(sales_tax, 2)}")
            subtotal = subtotal + sales_tax
            #total after sales tax
            print(f"Total : {round(subtotal, 2)}")

            print("Thank you for  shopping at TM PicknPay.")        
            print(now)
            print(f"\nReturn by {return_by}")
    except FileNotFoundError as filenotfound:
        print(FILE, " deos not to exist")
        print(filenotfound)
    except PermissionError:
        print("You do not have the permission  to access", FILE)
    except KeyError as key_err:
        print("There is on corresponding key in dictionary")
        print(key_err)


def read_dictionary(filename, key_column_index):
    products = {}
    #open file
    with open(filename, "rt") as file:
        #implement .reader() and assign variable
        product = csv.reader(file, delimiter=",")
        #skip the first line
        next(product)
        #loop through ecah i tem in the csv file
        for item in product:
            #set the key index from the .csv file
            key = item[key_column_index]
            #add items to the csv file
            products[key] = item
    #return the dictionary
    return products
if __name__ == "__main__":
    main()