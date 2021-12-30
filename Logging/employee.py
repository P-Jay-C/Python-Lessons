import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(asctime)s%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:
    ''' A sample Employee class'''

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self) -> str:
        return 'Employee({}, {}, {})'.format(self.first,self.last,self.salary)

emp_1= Employee('Jane', 'Smith', 22)
emp_2 = Employee('Corey', 'Schafer', 30)
emp_3 = Employee('Jerry', 'Jay', 30000)

