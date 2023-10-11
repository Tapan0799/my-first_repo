import MySQLdb
connection = MySQLdb.connect(host='localhost',database='pythonappdb',user='root',password='secret')
print(connection)
#cursor object is used for any query execution from python

cursor = connection.cursor()

insertquery = "insert into employee(emp_name,emp_id) values(%s,%s)"
values=("pradeep","102")
cursor.execute(insertquery,values)
connection.commit()
print("the record got inserted ",cursor.rowcount)
cursor.close()
