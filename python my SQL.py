
import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    user='root',
    password='2204',
    host='localhost',
    database='myoffice'
)

# Create a cursor object
cursor = cnx.cursor()

# Write the SQL query
insert_query = "INSERT INTO persons (id,name,email) VALUES (%s, %s, %s)"
data = ('1608', 'Bhavya', 'parsibhavyasri234@gmailcom')

# Execute the SQL query
cursor.execute(insert_query, data)

# Commit the changes
cnx.commit()


select_query = "SELECT * FROM persons"
cursor.execute(select_query)

# Fetch all rows of the result
result = cursor.fetchall()

# Display the retrieved data
for row in result:
    print(row)


# Close the cursor and connection
cursor.close()
cnx.close()

