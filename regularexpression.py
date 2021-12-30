import re

text_to_search = '''
abcdefghijklmnopqrstuvyxyz
ABCDEFGHIJKLMNOPQRSTUVYXYZ
1234567890

321-555-4321
123.555.1234
222*333*3345
300-333-3345
400-333-3345

mat 
bat
pat 
cat

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''
sentence = 'Start a sentence then bring it to an end'
email = ''
'''
CoreyMSchafer@gmail.com
corey.scha
'''

#pattern  = re.compile(r'[^b]at')
#pattern  = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern  = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

