def main():
    province = create_list("provinces.txt")
    print(province)
    #remove 1st item from list            
    province.pop(0)
    #remove last item
    province.pop()

    for line in province:
        if line == "AB":
            i = province.index(line)
            province[i] = "Alberta"

    count = province.count("Alberta")

    print("\n", count)
def create_list(filename):
    with open(filename, "rt") as provinces:
        province = []
        for line in provinces:
            clean_line = line.strip()
            province.append(clean_line)
    
    return province

if __name__ == "__main__":
    main()
        

