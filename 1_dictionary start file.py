import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

print(phonebook['Chris'])

my_dictionary = {} #this will create an empty dictionary

my_dictionary2 = dict(m=8, n=9) # m and n are keys and 8 and 9 are their corresponding values

print(my_dictionary2)

print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    print(f"Name: {name} Phone Number: {[name]}")
else:
    print(f"{name} is not in the phone book")





print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook['Joe'] = '555-0123'   #this will add a new ket value pair
phonebook['Chris'] = '555-4444'

print(phonebook)

print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)

del phonebook['Chris']

print(phonebook)


print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for x in phonebook:
    print(f"The key is {x} and the value is {phonebook[x]}") #iterates through the keys

for value in phonebook.values(): #iterates through the value
    print(value)



print()
print('*****  end section 5 ********')
print()


'''


print()
print('*****  start section 6 - using get and clear ********')
print()






print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()






print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()






print()
print('*****  end section 8 ********')
print()



print()
print('*****  start section 9 - using random and converting to list ********')
print()





print()
print('*****  end section 9 ********')
print()


'''





