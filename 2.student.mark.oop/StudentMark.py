from Student import Student
from Course import Course

class StudentMark(Student):
    def __init__(self, studentId=None, studentName=None, birthdate=None):
        super().__init__(studentId, studentName, birthdate)
        self.__marks = {}

    def setMark(self, courseId):
        mark = float(input("Enter mark:"))
        self.__marks[courseId.upper()] = mark

    def getMarks(self):
        return self.__marks

    def coursePicking(self):
        courseId = input("Write course id: ")
        while True:
            for c in Course.getAllCourses():
                if c.getCourseId().lower() == courseId.lower():
                    return courseId
            print("Course not found.")
            courseId = input("Write course id: ")

    def setSpecificMark(self):
        Course.printAllCourses()
        courseId = self.coursePicking()
        for s in Student.getAllStudents():
            s.setMark(courseId)

    def printCourseMark(self):
        Course.printAllCourses()
        courseId = self.coursePicking()
        print("Student Marks: ")
        print("Student ID----Student Name----Course Id----Mark")
        for s in Student.getAllStudents():
            print("{}----{}----{}----{}".format(
                s.getStudentId(),
                s.getStudentName(),
                courseId,
                s.getMarks[courseId.upper()]
            ))