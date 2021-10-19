# #formatting literal strings
# print('I love css2021'.upper())
# print('I love css2021'.rjust(20))
# print('I love css2021'.capitalize())


# # cocatenation
# print('hello'+ 'world')
# print('I like ' + str('cs_class_code') + '\talot!')
# print(f'{type(229)}')


# #lists
# list_1 = ['one','two','three']
# # list_1.append('four')

# list_2 = [1,2,3]
# list_1.extend(list_2)
# print(list_1)


# dictionaries
homies = {'Name': 'Gorret', 'Cousin': 'Maggie', 'Brother': 'Kevin', }

# mapping a dictionary

print(list(homies.keys()))
print(list(homies.values()))

# update
homies.update({'Sister': 'Leticia'})

# iteration
for x in homies:
    print(homies[x])
