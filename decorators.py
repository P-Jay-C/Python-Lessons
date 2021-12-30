def decorator_function(original_function):
    
    def wrapper_function(*args,**kwargs):
        print("Our wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function
    
''''
class decorator_class:
    def __init__(self, original_funtion):
        self.original_function = original_funtion

    def __call__(self, *args, **kwds):
        print("Our class method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwds)
        
'''

@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print("display_info ran with arguments({}, {})".format(name,age))

display()

print()

display_info("Jerry", 22)




