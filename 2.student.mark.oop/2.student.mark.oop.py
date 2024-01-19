# student_infos = []
# courses = []
from StudentMark import StudentMark
from Course import Course

class StudentMarkManagement:
    def __setStudents(self):
        try:
            n = int(input("Number of students: "))
            for _ in range(n):
                s = StudentMark()
                s.setStudent()
        except ValueError:
            print("Invalid input.")

    def __setCourses(self):
        try:
            n = int(input("Number of courses: "))
            for _ in range(n):
                c = Course()
                c.setCourse()
        except ValueError:
            print("Invalid input.")

    def setSpecificMark(self):
        Course.printAllCourses()
        courseId = self.coursePicking()
        for s in StudentMark.getAllStudents():
            s.setMark(courseId)

    def coursePicking(self):
        courseId = input("Write course id: ")
        while True:
            for c in Course.getAllCourses():
                if c.getCourseId().lower() == courseId.lower():
                    return courseId
            print("Course not found.")
            courseId = input("Write course id: ")

    def printCourseMark(self):
        Course.printAllCourses()
        courseId = self.coursePicking()
        print("Student Marks: ")
        print("Student ID----Student Name----Course Id----Mark")
        for s in StudentMark.getAllStudents():
            print("{}----{}----{}----{}".format(
                s.getStudentId(),
                s.getStudentName(),
                courseId,
                s.getMarks()[courseId.upper()]
            ))

    def main(self):
        ""
        while True:
            print("""
                1. Input students information
                2. Input courses information
                3. Input marks based on course
                4. Display students information
                5. Display courses information
                6. Display student marks based on course
                7. Exit
            """)
            m = input("Your choice (enter number only): ")
            match m:
                case "1":
                    self.__setStudents()
                case "2":
                    self.__setCourses()
                case "3":
                    self.setSpecificMark()
                case "4":
                    StudentMark.printAllStudents()
                case "5":
                    Course.printAllCourses()
                case "6":
                    self.printCourseMark()
                case "7":
                    break
                case _:
                    print("Invalid input.")

smm = StudentMarkManagement()
smm.main()