class Employee:
    ''' A sample Employee class'''

    def __init__(self, first, last, salary):
        self.first =first
        self.last = last
        self.salary = salary

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self) -> str:
        return 'Employee({}, {}, {})'.format(self.first,self.last,self.salary)
