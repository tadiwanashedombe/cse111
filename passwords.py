LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]
#main function
def main():
    
    password = " "
    #check password until they quit
    while password != "q" and password != "Q":
        password = input("Enter password : ")

def password_strength(password, min_length=10 , strong_length=16):
    pass


def word_in_file(word, filename, case_sensetive):
    #check password against toppaswords list
    with open("topppasswords.txt", "r") as file:
        for line in file:
            line = line.strip()
            if word.lower() == line:
                if
                return True
                break
            else:
                return False
                
def word_has_character(word, character_list):
    pass

def word_complexity(word):
    pass



main()
#start a loop
#check password against dictionary
#craete password strength checker
"""
If the password is in the dictionary file. (this should be a case insensitive match)
Print the message. "'Password is a dictionary word and is not secure."
Return a strength value of 0.
If the password is in the toppassword list. (this should be a case sensitive match)
Print the message "Password is a commonly used password and is not secure."
Return a strength value of 0
If the password is shorter than the minimum password length of 10
Print the message "Password is too short and is not secure."
Return a strength value of 1
If the password is longer than 15 characters, the password is strong
Print the message "Password is long, length trumps complexity this is a good password."
Return the strength value of 5
"""
#
