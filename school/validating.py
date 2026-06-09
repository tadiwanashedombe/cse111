import re

def valid_email(dictionary):  
        valid = False
        while not valid:
            # get email
            email = input("Enter Email address : ")
            #format to lower
            email = email.lower()
            
            #common email pattern
            pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
            if re.fullmatch(pattern, email):
                #check if email already exits
                if email in dictionary:
                    print("Email Already Exists")
                else:
                    break
            else:
                print(f"Invalid email ('{email}')")
        return email
    
    #check for empty fields
def not_empty(prompt,error_msg):
    valid = False
    while not valid:
        user_input = input(prompt)
        if user_input == "":
            print(error_msg)
        else:
            break
    return user_input