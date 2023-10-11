import MySQLdb
connection = MySQLdb.connect(host='localhost',database='pythonappdb',user='root',password='secret')
print(connection)
#cursor object is used for any query execution from python

cursor = connection.cursor()

table="create table employee(emp_name varchar(50), emp_id int primary key)"

cursor.execute(table)
print("employee table got created")