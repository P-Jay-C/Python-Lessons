#First Class Functions
'''
def square(x):
    return x * x

def my_map(func, arg_lists):
    result = []
    for i in arg_lists:
        result.append(func(i))

    return result

squares = my_map(square, [1,2,3,4,5,6])

print(squares)
'''

'''
def logger(msg):
    
    def log_message():
        print("Log: ", msg)

    return log_message

log_hi = logger("Hi")

log_hi()
'''

#Closures
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

my_func = outer_func("Hi")

print(my_func()) 