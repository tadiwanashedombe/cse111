password = "password"
with open("toppasswords.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == password:
            found = 1
            break
        else:
            found = 0
if found == 1:
    print("foundit")
else:
    print("damnmit")