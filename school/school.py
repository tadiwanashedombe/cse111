import csv
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
   # print(options)
  #  action = int(input("What Would You like do to:"))
    
    show_records(student_records)
    #save the dictionary to te file

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

#validate the the userinputs

if __name__ == "__main__":
    main()