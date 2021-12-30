import logging

#DEBUG: Detailed information, typically of interest only when diagnosing problems.
#INFO: Confirmation that 

logging.basicConfig(filename='test.log',level= logging.DEBUG, 
                    format= '%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x * y
 
def divide(x,y):
    return x / y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.warning('Div: {} / {} = {}'.format(num_1, num_2, div_result))

