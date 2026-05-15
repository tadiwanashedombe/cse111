#when user creates the password it is added to known passwords so that it cannot be used again
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensetive=False):
    #c
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            #password from file
            line = line.strip()
            if case_sensetive:
                if word == line:
                    return True
            else:
                if word.lower() == line.lower():
                    return True
    return False
                
def word_has_character(word, character_list):
    #read through the chars list
    for character in word:
        #if the character in word is in the character list
        if character in character_list:
            return True
    return False

def word_complexity(word):
    #initialize ratings counter
    complexity_rating = 0
    
    #check for character in uppercase list
    if word_has_character(word, UPPER):
        complexity_rating += 1
    #check for character in lowercase list
    if word_has_character(word, LOWER):
        complexity_rating += 1
    
    #check for character in special chars list
    if word_has_character(word, SPECIAL):
        complexity_rating += 1
    
    #check for character in digits list
    if word_has_character(word, DIGITS):
        complexity_rating += 1
    #return the rating
    return complexity_rating

def password_strength(password, min_length=10 , strong_length=16):
    #check dictionary
    #if the password is exactly the same as in wordlist.txt
    if word_in_file(password, "wordlist.txt", case_sensetive=False):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    #check Known passwords
    #if password is in the toppassword.txt
    if word_in_file(password, "toppasswords.txt", case_sensetive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    #short password
    if len(password) < min_length:
        print("Password os too short and is not secure.")
        return 1
    
    #if password len > 15
    if len(password) > strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    #call word_complexity to determine the password strength
    password_strength = 1 + word_complexity(password)

    return password_strength


def main():
    print("Welcome to password checker press (q) to exit. \n")
    password = " "
    #check password until they quit
    while password != "q" and password != "Q":
        password = input("Enter password : ")

        strength = password_strength(password)
        print(f"Password Strength : {strength}")

        with open("toppasswords.txt", "at") as passwords:
            print(password, file=passwords)

if __name__ == "__main__":
    main()