import csv
def read_dictionary(filename, key_column_index):
    s_dictionary = {}
    #open file
    with open(filename, "rt") as csvfile:

        reader = csv.reader(csvfile, delimiter = ",")
        next(csvfile)
        for row in reader:
            key_value = row[key_column_index]

            s_dictionary[key_value] = row
    return s_dictionary
def main():
    KEY_INDEX = 0
    NAME_INDEX = 1

    students = read_dictionary("students.csv", KEY_INDEX)

    i_number = input("Enter I number : ")

    i_number = i_number.replace("-", "")

    if not i_number.isdigit():
        print("Invalid i number")
        
    if i_number in students:
        student = students[i_number]

        name = student[NAME_INDEX]

        print(f"The student's name is {name}")
    else:
        print("No such student !")

if __name__ == "__main__":
    main()