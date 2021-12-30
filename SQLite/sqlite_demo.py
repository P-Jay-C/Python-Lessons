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

emp_1 = Employee('Sam','Smith', 10000)
emp_2 = Employee('Gloria', 'Obeng', 30000)

# c.execute('INSERT INTO employees VALUES (?,?,?)',(emp_1.first, emp_1.last, emp_1.salary))
# conn.commit()

# c.execute(
#                 'INSERT INTO employees VALUES (:first, :last, :salary)',
#                 {'first':emp_2.first, 'last':emp_2.last, 'salary': emp_1.salary}
#         )
# conn.commit()



c.execute('SELECT * FROM employees WHERE last = ?', ('Smith',))
print(c.fetchall())

c.execute('SELECT * FROM employees WHERE last = :last', {'last': 'Doe'})
print(c.fetchall())

conn.commit()
conn.close()