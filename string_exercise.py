
long_string = 'crapshoot is a freakin long string crap'

cap_string = long_string.capitalize()
print('cap string:', cap_string)

first_four = long_string[0:4]
print('first 4:', first_four)

last_four = long_string[-5:]
print('last 4:', last_four)

first_five = long_string[:5]
print('first 5:', first_five)

ss = first_five + last_four

demo = '%c - %s - %d' % ('X', 'SSSSSS', 1)
print(demo)