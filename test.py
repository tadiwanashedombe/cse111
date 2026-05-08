city_name = "Accra"
# Open a text file named cities.txt in append mode.
with open("volume.txt", "at") as cities_file:
  # Print a city's name and information to the file.
  print(city_name, file=cities_file)