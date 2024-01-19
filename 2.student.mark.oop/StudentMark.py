from Student import Student

class StudentMark(Student):
    def __init__(self, studentId=None, studentName=None, birthdate=None):
        super().__init__(studentId, studentName, birthdate)
        self.__marks = {}

    def setMark(self, courseId):
        mark = float(input("Enter mark:"))
        self.__marks[courseId.upper()] = mark

    def getMarks(self):
        return self.__marks
