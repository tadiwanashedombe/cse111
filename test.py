from chemistry import make_periodic_table
from formula import parse_formula

formula = "C6H6"
periodic_table = make_periodic_table()

p = parse_formula(formula, periodic_table)
total_mass = 0 
for i in p:
    e = i[0]
    m = i[1]
    print (m)

    for key, value in make_periodic_table().items():
        if key == e:
            mass = (value[1] * m)
            total_mass += mass
print(total_mass)