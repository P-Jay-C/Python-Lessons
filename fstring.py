'''
first_name = 'Corey'
last_name = 'Schafer'

#sentence = 'My name is {} {}'.format(first_name,last_name)
sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)
'''

person = {
    'name': 'Jenn',
    'age': 23
}

'''
sentence = 'My name is {} and I am {} years old'.format(person['name'],person['age'])
sentence = f'My name is {person["name"]} and I am {person["age"]} years old'
print(sentence)
'''

'''
for n in range(1,11):
    sentence = f'The value is {n:02}'
    print(sentence)
'''

pi = 3.14159265

sentence = f'pi is equal to {pi:.4f}'
print(sentence)

