
LOWER = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
DIGITS = ["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","|",";",":","'","\"",",",".",
           "<",">","?","/","\\","`","~"]

def main():
    print("Password Strength Checker (enter 'q' to quit)")
    while True:
        password = input("\nEnter a password to check: ")
        if password in ("q", "Q"):
            print("Goodbye!")
            break

        strength = password_strength(password)

        # Enhancement: visual strength meter
        filled = "#" * strength
        empty = " " * (5 - strength)
        print(f"Strength: [{filled}{empty}] {strength}/5")

def word_in_file(word, filename, case_sensitive=False):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            file_word = line.strip()
            if case_sensitive:
                if word == file_word:
                    return True
            else:
                if word.lower() == file_word.lower():
                    return True
    return False


def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity


def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    if len(password) > 15:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    strength = 1 + word_complexity(password)
    return strength





if __name__ == "__main__":
    main()