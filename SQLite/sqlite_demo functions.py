import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()


""" c.execute('''
            INSERT INTO employees 
            VALUES
                ('Mike', 'Smith',5000),
                ('Jane','Doe',7000)
        '''
) """

def insert_emp(emp):
        with conn:
                c.execute(
                        'INSERT INTO employees VALUES (:first, :last, :salary)',
                        {'first':emp_2.first, 'last':emp_2.last, 'salary': emp_1.salary}
                )

def get_emp_by_name(lastname):
        c.execute('SELECT * FROM employees WHERE last = :last', {'last':lastname})
        return c.fetchall()

def update_pay(emp,pay):
        c.execute('''
                        UPDATE employees 
                        SET pay = :pay 
                        WHERE first = :first AND last = :last ''',
                        {'first':emp.first, 'last':emp.last, 'pay':emp.pay})

def remove_emp(emp):
        with conn:
                c.execute('''
                        DELETE from employees 
                        WHERE first = :first AND last = :last''',
                        {'first':emp.first, 'last':emp.last}
                )

emp_1 = Employee('Sam','Smith', 10000)
emp_2 = Employee('Gloria', 'Obeng', 30000)

insert_emp(emp_1)
insert_emp(emp_2)

emp = get_emp_by_name('Smith')
print(emp)


conn.close()