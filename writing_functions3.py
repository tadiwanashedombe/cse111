def get_positive_value(prompt_text):
    """
    Prompt the user for a value and reprompts them if a value is negetive
    """
    #prompt for value
    value = float(input(prompt_text))
    
    #check if value is positive and reprompts if needed
    while value < 0:
        print("Sorry value cannot be negetive")

        #reprompt
        value = float(input(prompt_text))
        
    # return value
    return value

length = get_positive_value("What is the length of the rectangle : ")
width = get_positive_value("What is te width of the rectangle : ")

area = length * width

print(f"The area is {area}")