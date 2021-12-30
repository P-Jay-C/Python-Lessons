
try:
    f = open("test.txt")

except FileNotFoundError as e:
    print(e)

except NameError as e: 
    print(e)

