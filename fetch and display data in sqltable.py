import mysql.connector
mydb = mysql.connector.connect(
    user='root',
    password='2204',
    host='localhost',
    database='myoffice'
)
cursor = mydb.cursor()

#SQL query
insert_query = "INSERT INTO persons (id,name,email) VALUES (%s, %s, %s)"
data = ('1608', 'Bhavya', 'parsibhavyasri234@gmailcom')
cursor.execute(insert_query, data)
mydb.commit()


select_query = "SELECT * FROM persons"
cursor.execute(select_query)

#fetches
result = cursor.fetchall()

# Displays retrieved data
for row in result:
    print(row)

cursor.close()
mydb.close()

