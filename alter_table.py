import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gayathri@123",     # Change this
    database="school"
)

cursor = db.cursor()

# Add 'age' column
cursor.execute("ALTER TABLE student ADD COLUMN age INT")
db.commit()

print("Column 'age' added successfully!")
