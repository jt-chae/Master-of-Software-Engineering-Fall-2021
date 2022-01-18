import mysql.connector

class StudentManagementSystem:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1989Imagination;",
            database = "jt-chae"
        )

        self.mycursor = self.mydb.cursor() #method to read lines from user
        self.mycursor.execute(
            "CREATE TABLE IF NOT EXISTS students (student_id INT AUTO_INCREMENT PRIMARY KEY, student_name VARCHAR(50) NOT NULL, student_email VARCHAR(255) NOT NULL)")
        self.mycursor.execute(
            "CREATE TABLE IF NOT EXISTS courses (course_id INT AUTO_INCREMENT PRIMARY KEY, course_name VARCHAR(50) NOT NULL, course_description VARCHAR(255) NOT NULL, course_schedule VARCHAR(255) NOT NULL)")
        self.mycursor.execute(
            "CREATE TABLE IF NOT EXISTS students_courses (student_id INT NOT NULL, course_id INT NOT NULL,CONSTRAINT students_courses_fk_students FOREIGN KEY (student_id) REFERENCES students (student_id),  CONSTRAINT students_courses_fk_courses FOREIGN KEY (course_id) REFERENCES courses (course_id))")

    def addStudent(self, student_name, student_email):
        sql = "INSERT INTO students VALUES (DEFAULT, %s, %s)"
        self.mycursor.execute(sql, (student_name, student_email))
        self.mydb.commit() #after finish method, we have to commit it 

    def addCourse(self, course_name, course_description, days):
        course_day = ','.join(days)
        sql = "INSERT INTO courses VALUES (DEFAULT,%s, %s, %s)"
        self.mycursor.execute(
            sql, (course_name, course_description, course_day))
        self.mydb.commit()

    def enrollToCourse(self, student_id, course_id):
        if self.alreadyEnroll(student_id, course_id):
            return 1
        elif len(self.getStudentByID(student_id)) == 0:
            return 2
        elif len(self.getCourseByID(course_id)) == 0:
            return 3
        sql = "INSERT INTO students_courses VALUES (%s, %s)"
        self.mycursor.execute(sql, (student_id, course_id))
        self.mydb.commit()
        return 0

    def getStudentByID(self, student_id):
        sql = "SELECT * FROM students WHERE student_id = %s"
        self.mycursor.execute(sql, (student_id,))
        res = self.mycursor.fetchall()
        return res

    def getCourseByID(self, course_id):
        sql = "SELECT * FROM courses WHERE course_id = %s"
        self.mycursor.execute(sql, (course_id,))
        res = self.mycursor.fetchall()
        return res

    def alreadyEnroll(self, student_id, course_id):
        sql = "SELECT * FROM students_courses s WHERE s.student_id = %s and s.course_id = %s"
        self.mycursor.execute(sql, (student_id, course_id))
        res = self.mycursor.fetchall()
        return len(res) > 0

    def getAllStudentsByCourseID(self, course_id):
        if len(self.getCourseByID(course_id)) == 0:
            return []
        sql = "SELECT s.student_name FROM courses c JOIN students_courses sc ON c.course_id = sc.course_id JOIN students s ON sc.student_id = s.student_id WHERE c.course_id = %s ORDER BY s.student_name"
        self.mycursor.execute(sql, (course_id,))
        res = self.mycursor.fetchall()
        return [r[0] for r in res]

    def getAllCoursesByStudentID(self, student_id):
        if len(self.getStudentByID(student_id)) == 0:
            return []
        sql = "SELECT c.course_name FROM courses c JOIN students_courses sc ON c.course_id = sc.course_id JOIN students s ON sc.student_id = s.student_id WHERE s.student_id = %s ORDER BY c.course_name"
        self.mycursor.execute(sql, (student_id,))
        res = self.mycursor.fetchall()
        return [r[0] for r in res]

    def getAllCoursesByStudentIDOnOneDay(self, student_id, day):
        if len(self.getStudentByID(student_id)) == 0:
            return []
        sql = "SELECT c.course_name FROM courses c JOIN students_courses sc ON c.course_id = sc.course_id JOIN students s ON sc.student_id = s.student_id WHERE s.student_id = %s and c.course_schedule LIKE %s ORDER BY c.course_name"
        self.mycursor.execute(sql, (student_id, '%'+day+'%'))
        res = self.mycursor.fetchall()
        return [r[0] for r in res]

    def close(self):
        self.mycursor.close()
        self.mydb.close()

def main():
    sms = StudentManagementSystem()
    while True:
        print("----------------------\n" +
              "Welcome to student enrollment system:\n" +
              "1. Add a new student \n" +
              "2. Add a new course\n" +
              "3. Enroll a student to a course\n"
              "4. Find a student's courses\n" +
              "5. Find all students in a course\n" +
              "6. Find all courses of a student on a day\n" +
              "7. Exit")

        command = input()
        if command == '1':
            name = input('Please enter the Student name: ')
            email = input('Please enter the Student email address: ')
            sms.addStudent(name, email)
            print('Student added successfully!\n')
        elif command == '2':
            name = input('Please enter the Course Name: ')
            description = input('Please enter the Course Description: ')
            schedule = input('Please enter the Course Schedule separated by commas: ')
            sms.addCourse(name, description, schedule.split(' '))
            print('Course added successfully!\n')
        elif command == '3':
            student_id = input('Please Enter the Student ID: ')
            course_id = input('Please Enter the Course ID: ')
            res = sms.enrollToCourse(student_id, course_id)
            if res == 0:
                print('Enrolled Successfully!\n')
            elif res == 1:
                print('Already Enrolled.\n')
            elif res == 2:
                print('Student Not Found.\n')
            elif res == 3:
                print('Course Not Found.\n')

        elif command == '4':
            student_id = input('Please Input the Student ID: ')
            res = sms.getAllCoursesByStudentID(student_id)
            if res:
                print('Search Done!\n')
                print(res)
                print('\n')
            else:
                print('Student Not Found.\n')
        elif command == '5':
            course_id = input('Please Enter the Course ID: ')
            res = sms.getAllStudentsByCourseID(course_id)
            if res:
                print('Search Done!\n')
                print(res)
                print('\n')
            else:
                print('Course Not Found.\n')
        elif command == '6':
            course_id = input('Please Enter the Student ID: ')
            day = input('Please Enter the Day You Want to Check: ')
            res = sms.getAllCoursesByStudentIDOnOneDay(student_id, day)
            if res:
                print('Search Done!\n')
                print(res)
                print('\n')
            else:
                print('No Data')
        elif command == '7':
            print('Exited')
            return
        else:
            print('Invalid Input\n')


if __name__ == "__main__":
    main()