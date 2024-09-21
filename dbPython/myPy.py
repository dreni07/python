import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
create table if not exists employee(
    id integer primary key autoincrement,
    name text not null,
    email text not null,
    position text not null,
    salary text not null);
''')

cursor.execute('''
insert into employee (name,email,position,salary) values (?,?,?,?);
''',('Dren Llazani','drenllazani10@gmail.com','SWE',2300))

conn.commit()

cursor.execute('Select * from employee')
row = cursor.fetchall()
for the_row in row:
    print(the_row)

cursor.close()
conn.close()