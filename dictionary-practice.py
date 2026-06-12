bad_guys = {
    'daredevil':'kingpin',
    'x-men':'apocalypse',
    'batman':'bane'
}
# adding an entry to the dictionary
bad_guys['deadpool'] = 'deadpool'

# edit the value
bad_guys['x-men'] = 'juggernaut'

# deletinf items:
del bad_guys['x-men']

print(bad_guys)
