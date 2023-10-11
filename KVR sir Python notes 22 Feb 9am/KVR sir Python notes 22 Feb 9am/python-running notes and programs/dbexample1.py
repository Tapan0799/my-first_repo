import MySQLdb
connection = MySQLdb.connect(host='localhost',database='pythonappdb',user='root',password='secret')
print(connection)
#cursor object is used for any query execution from python

cursor = connection.cursor()

cursor.execute("select curdate();")

#This will fetch the record
datevalue = cursor.fetchone()

#get the datevlaue from the result object

print("today's date is ",datevalue[0])

connection.close()
