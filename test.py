from chemistry import make_periodic_table
from formula import parse_formula

formula = "C6H6"
periodic_table = make_periodic_table()

p = parse_formula(formula, periodic_table)
for i in p:
    e = i[0]

    for key, value in make_periodic_table().items():
        if key == e:
            mass = (value[0])
            print(mass)