person = {
    'name':'Jess',
    'age': 23,
    'job': 'Programmer'
}

'''
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print('Missing some keys')
'''

'''
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print('Missing {}'.format(e))
'''

import os

my_file = 'text.txt'

try: 
    f = open(my_file)
except IOError as e:
    print("File can not be accessed")
else:
    with f:
        print(f.read())
        