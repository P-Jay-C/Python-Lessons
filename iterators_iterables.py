import itertools
from typing import Counter

# counter = itertools.count(start=5,step=5)
# data = [100, 200, 300, 400]

# daily_data = list(itertools.zip_longest(range(10), data))

# print(daily_data)

# counter = itertools.cycle([1,2,3])
squares = map(pow,range(10),itertools.repeat(2))
squares = itertools.starmap(pow, [(0,2), (1,2), ( 3, 2)])

print(list(squares))

# counter = itertools.repeat(2, times=3)
# print(next(counter))
# print(next(counter))
# print(next(counter))

