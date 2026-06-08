import csv
import re
def main():
    FILE = "records.csv"
    KEY_INDEX = 0
    print("Alheit High School Database \n")
    
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
    add_student(student_records)

#read the csv file and create a dictionary
def read_csv(file, key_column):
    students = {}
    with open(file, "r+", encoding="utf-8-sig") as records:
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
def add_student(dictionary):
    print("Please Enter the following records accordingly\n")
    #validate email
    def valid_email():  
        valid = False
        while valid == False:
            # get email
            email = input("Enter Email address :")
            #common email pattern
            pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if re.fullmatch(pattern, email):
                #check if email already exits
                if email in dictionary:
                    print("Email Already Exists")
                #break
            else:
                print(f"Invalid email ('{email}')")
    
    
    valid_email()
    
        

        #show progress
        #check if email has @
        #check if email doesn't already exist
       

if __name__ == "__main__":
    main()