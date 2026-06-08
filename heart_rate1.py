
import math
age = int(input("Enter your age : "))

maximum = 220 - age

fastest = (85/100) * maximum

slowest = (65/100) * maximum

print(f"When you exercise to strengthen your heart, you should keep your heart rate between {math.floor(slowest)} and {math.ceil(fastest)} beats per minute.")