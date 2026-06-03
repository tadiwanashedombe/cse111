# Value error occurs when the code calls a function, passes an argument with the corrcet data type but an invalid value
#ocuurs when the float / int functions ttris to comvert a string into a number  but the string contains characters that are not numbers
def main():
  try:
    number = float(input("Please enter a number: "))
    print(number)
  except ValueError as val_err:
    print(val_err)
if __name__ == "__main__":
  main()
