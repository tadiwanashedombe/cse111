#added option to add phone number to the volume.txt file
#

import math
from datetime import date

#get user width
width = float(input("Enter the width of the tire in mm (e.g 405) : "))

#get user aspect ratio
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60) : "))

#get user diameter
diameter = float(input("Enter the diameter of the wheel in inches (ex 15) : "))

#declare the pi
pi = math.pi

#prepare the date
day = date.today()
#initialize date format
day_name = day.strftime("%Y-%m-%d")



##calculate
volume_part1 = pi * (width**2) * aspect_ratio

volume_part2 = width * aspect_ratio + 2540 * diameter

tire_volume = (float(volume_part1) * float(volume_part2)) / 10000000000

tire_volume = round(tire_volume, 2)

#get user phone number
phone_number = input("Would you like to purchase the tire with these dimensions (yes/no) : ")

if phone_number.lower() == "yes":
    phone_number = input("Enter your phone number : ")

    phone_number = ", "+ phone_number
else:
    phone_number = " "

#Write to volumes.txt
with open("volumes.txt", "at") as volume:
    print(f"{day_name}, {width}, {diameter}, {aspect_ratio}, {tire_volume}{phone_number}", file=volume)

#display the volume
print(f"The approximate volume is {tire_volume} liters")

