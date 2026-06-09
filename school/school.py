import csv
import re
from datetime import datetime

def main():
    """
    Purpose : Manage an online database with multiple records of different schools and countries
    """
    FILE = "records.csv"
    KEY_INDEX = 0
    print("Online School Database \n")
    
    options = """
    1.Show all student records
    2.Add student 
    3.Delete student record
    4.Edit student records 
    5.Find specific student
    """
    student_records = read_csv(FILE, KEY_INDEX)
    #print(student_records)
   # print(options)
  #  action = int(input("What Would You like do to:"))
    
    #1 show records
    #show_records(student_records)
    #save the dictionary to te file
    
    #2 add student
    #add_student(student_records,FILE)

    #3 delete student
    #del_student(student_records,FILE)

    # 4 Edit record
    #edit_record(student_records,FILE)

    # 5 Specific record
    find_record(student_records)

#read the csv file and create a dictionary
def read_csv(file, key_column):
    students = {}
    with open(file, "rt", encoding="utf-8-sig") as records:
        records = csv.reader(records)
        next(records)
        #lop through csv file det records
        for record in records:
            key = record[key_column]
            students[key] = record
    return students

def show_records(dictionary):
    #loop through dictionary
    print("format : Email    Fullname    D.O.B    Gender Nationality    Phone   Address     Emergency Contact   Emergency Phone     School  Form    Created at")
    
    for value in sorted(dictionary.items(), key=lambda x: x[1] ):
        #format the records remove commas, square brackets
        value = value[1]
        record = f"{value[0]} |{value[1]}  |{value[2]} |{value[3]} |{value[4]} |{value[5]} |{value[6]} |{value[7]} |{value[8]} |{value[9]} |{value[10]} |{value[11]} \n"
        print(record)

def add_student(dictionary, file):
    print("Please Enter the following records accordingly\n")
    #validate email
    def valid_email():  
        valid = False
        while not valid:
            # get email
            email = input("1/11\nEnter Email address : ")
            #format to lower
            email = email.lower()
            
            #common email pattern
            pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
            if re.fullmatch(pattern, email):
                #check if email already exits
                if email in dictionary:
                    print("Email Already Exists")
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

    email = valid_email()
    name = not_empty("2/11\nFull name : ", "Full name cannot be empty!")
    dob = not_empty("3/11\nEnter Date Of Birth (dd-mm-yyyy) : ", "Date of Birth cannot be empty!")
    gender = not_empty("4/11\nGender (F / M) : ", "Gender cannot be empty!") 
    nationality = not_empty("5/11\nNationality (Zimbabwean) : ", "Nationality cannot be empty!")  
    phone = not_empty("6/11\nYour Phone number (263 00 000 0000): ", "Phone Number cannot be empty!")  
    address = not_empty("7/11\nEnter you physical address : ", "Address cannot be empty! ")  
    emergency_contact = not_empty("8/11\nName of Emergency Contact : ", "Emergency contact name cannot be empty!") 
    emergency_phone = not_empty("9/11\nEmergency Contact Phone number : ", "Emergency Contact Phone number cannot be empty")  
    school  =  not_empty("10/11\nSchool Name: " , "School cannot be empty!")
    form = not_empty("11/11\nForm (Form 1 - 6) : ", "Form cannot be empty!") 
    now = datetime.now()
    created_at = now.strftime("%m/%d/%Y %I:%M %p")
    
    # Add users to file
    with open(file, "a", encoding="utf-8-sig") as records:
        records.write(f"{email},{name},{dob},{gender},{nationality},{phone},{address},{emergency_contact},{emergency_phone},{school},{form},{created_at} \n")
        print("Successfully added student")
        #show progress

def del_student(dictionary, File):
    delete = False
    
    while not delete:
        email = input("Enter the student email to delete :")
        if email in dictionary:
            del dictionary[email]
            
            #clear file 
            with open(File, "w") as newfile:
                newfile.write("email,full_name,dob,gender,nationality,phone,address,emergency_contact,emergency_phone,school,form,created_at\n")
                for value in dictionary.items():
                    value = value[1]
                    newfile.write(f"{value[0]}, {value[1]}, {value[2]}, {value[3]}, {value[4]}, {value[5]}, {value[6]}, {value[7]}, {value[8]}, {value[9]}, {value[10]}, {value[11]}\n")
            print("Record Deleted !")
            break
        else:
            print("Email not found") 
def edit_record(dictionary,File):
    edit = False
    while not edit:
        email = input("Enter the student email to edit :")
        if email in dictionary:

            value = dictionary[email]
            #show option
            print("Choose which field to edit using numbers")
            print(f"1.Email : {value[0]}\n 2.Name : {value[1]}\n 3.Date Of Birth: {value[2]}\n 4.Gender : {value[3]}\n 5.Nationality : {value[4]}\n 6.Phone : {value[5]}\n 7.Address : {value[6]}\n 8.Emergency Contact : {value[7]}\n 9.Emergency Contact Phone : {value[8]}\n 10.School : {value[9]}\n 11.Form : {value[10]}")
            field =(input("Which field  would you like to edit (1-11) : "))

            ###edit field
            if field == "1":
                new = input("New Email: ")
                value[0] = new
            elif field == "2":
                new = input("New Name: ")
                value[1] = new
            elif field == "3":
                new = input("New Date Of Birth: ")
                value[2] = new
            elif field == "4":
                new = input("New Gender: ")
                value[3] = new
            elif field == "5":
                new = input("New Nationality: ")
                value[4] = new
            elif field == "6":
                new = input("New Phone: ")
                value[5] = new
            elif field == "7":
                new = input("New Address: ")
                value[6] = new
            elif field == "8":
                new = input("New Emergency Contact: ")
                value[7] = new
            elif field == "9":
                new = input("New Emergency Contact Phone: ")
                value[8] = new
            elif field == "10":
                new = input("New School: ")
                value[9] = new
            elif field == "11":
                new = input("New Form: ")
                value[10] = new
            else:
                print("Invalid Option")
                
    
            #clear file 
            with open(File, "w") as newfile:
                #new header
                newfile.write("email,full_name,dob,gender,nationality,phone,address,emergency_contact,emergency_phone,school,form,created_at\n")
                #rewrite dictionary as newfile
                for value in dictionary.items():
                    value = value[1]
                    newfile.write(f"{value[0]}, {value[1]}, {value[2]}, {value[3]}, {value[4]}, {value[5]}, {value[6]}, {value[7]}, {value[8]}, {value[9]}, {value[10]}, {value[11]}\n")
            print("Record Edited !")
            break
        else:
            print("Email not found") 

def find_record(dictionary):
    fount = False
    while not fount:
        email = input("Enter the student email :")
        if email in dictionary:

            value = dictionary[email]
            #show option
            print(f"\n1.Email : {value[0]}\n 2.Name : {value[1]}\n 3.Date Of Birth: {value[2]}\n 4.Gender : {value[3]}\n 5.Nationality : {value[4]}\n 6.Phone : {value[5]}\n 7.Address : {value[6]}\n 8.Emergency Contact : {value[7]}\n 9.Emergency Contact Phone : {value[8]}\n 10.School : {value[9]}\n 11.Form : {value[10]}")
            break
        else:
            print("Email not found!")
            break

if __name__ == "__main__":
    main()