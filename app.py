from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Gayathri@123",
    database="school"
)

# Show form and student list
@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM student")  # ✅ Changed from 'students' to 'student'
    students = cursor.fetchall()
    return render_template('index.html', students=students)

# Add student (form submission)
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']

    cursor = db.cursor()
    cursor.execute("INSERT INTO student (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))  # ✅ Changed
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
