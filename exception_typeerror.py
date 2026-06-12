#type error occurs when a function is passed with wrong data-types
def main():
    try:
        text = input("Please enter a number : ")
        integer = round(text)
        print(integer)
    except TypeError as type_error:
        print(type_error)
if __name__ == "__main__":
    main()