import itertools
from typing import Counter

letters = ['a', 'b', 'c', 'd']
numbers = [ 0,1,2,3]
names = ['Corey', 'Nicole']

# result = itertools.permutations(letters,2)
# result = itertools.combinations_with_replacement(numbers,4)

result =  itertools.islice(range(10),1, 5, 2   )

for item in result:
    print (1,item)

