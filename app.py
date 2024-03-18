import psycopg2
from psycopg2 import sql

db_params = {
    'dbname': 'example',
    'user': 'example',
    'password': 'example',
    'host': 'localhost'
}

def get_db():
  connect = psycopg2.connect(**db_params)
  return connect

def getAllStudents():
  connect = get_db()
  query = connect.cursor()
  query.execute("SELECT * FROM students;")
  students = query.fetchall()
  for student in students:
    print(student)
  query.close()
  connect.close()

def addStudent(first_name, last_name, email, enrollment_date):
  connect = get_db()
  query = connect.cursor()
  query.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", (first_name, last_name, email, enrollment_date))
  connect.commit()
  query.close()
  connect.close()

def updateStudentEmail(student_id, new_email):
  connect = get_db()
  query = connect.cursor()
  query.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
  connect.commit()
  query.close()
  connect.close()

def deleteStudent(student_id):
  connect = get_db()
  query = connect.cursor()
  query.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
  connect.commit()
  query.close()
  connect.close()

if __name__ == '__main__':
  # addStudent('Add', 'Student', 'add.student@example.com', '2023-09-03')
  # getAllStudents()
  # updateStudentEmail(1, 'update.email@example.com')
  # deleteStudent(1)