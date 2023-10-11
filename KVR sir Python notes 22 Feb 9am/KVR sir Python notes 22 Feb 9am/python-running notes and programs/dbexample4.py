#program for selectin the records
import MySQLdb
connection = MySQLdb.connect(host='localhost',database='pythonappdb',user='root',password='secret')
print(connection)
#cursor object is used for any query execution from python

cursor = connection.cursor()

cursor.execute("select * from employee")

rows=cursor.fetchall()

print("the total number of rows ", cursor.rowcount)

for row in rows:
   print(row) #display each row

for row in rows:
   employeename = row[0]
   employeeId = row[1]
   print("employeeName", employeename)
   print("employeeId", employeeId)


cursor.close() #close the cursor

print("****getting data by using order by")
cursor = connection.cursor()

cursor.execute("select * from employee order by emp_id desc")

rows=cursor.fetchall()


for row in rows:
   employeename = row[0]
   employeeId = row[1]
   print("employeeName", employeename)
   print("employeeId", employeeId)

cursor.close() #close the cursor
print("****getting data by using limit clause")
cursor = connection.cursor()

cursor.execute("select * from employee limit 3 offset 2")

rows=cursor.fetchall()


for row in rows:
   employeename = row[0]
   employeeId = row[1]
   print("employeeName", employeename)
   print("employeeId", employeeId)

print("****getting data by using like operator")

cursor = connection.cursor()

cursor.execute("select * from employee where emp_name like 'r%'")

rows=cursor.fetchall()

for row in rows:
   employeename = row[0]
   employeeId = row[1]
   print("employeeName", employeename)
   print("employeeId", employeeId)

connection.close() #close the connection