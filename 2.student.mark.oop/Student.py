class Student:
    """This is a Student class that have attributes 
    all privated, and some specific methods."""
    __student_infos = []

    def __init__(self, studentId=None, studentName=None, birthdate=None):
        self.__studentId = studentId
        self.__studentName = studentName
        self.__birthdate = birthdate
        if not self.isStudentDuplicate():
            Student.getAllStudents().append(self)

    def __setStudentId(self):
        newId = int(input("Enter student id: "))
        for student in Student.getAllStudents():
            if newId == student.getStudentId():
                print("Student Id already exists.")
                return

        self.__studentId = newId

    def getStudentId(self):
        return self.__studentId

    def __setStudentName(self):
        newName = input("Enter student name: ")
        self.__studentName = newName

    def getStudentName(self):
        return self.__studentName
    
    def __setBirthDate(self):
        newBirthDate = input("Enter birth date: ")
        self.__birthdate = newBirthDate
    
    def getBirthDate(self):
        return self.__birthdate
    
    def isStudentDuplicate(self):
        for s in Student.getAllStudents():
            if (self == s):
                return True
        return False
    
    def setStudent(self):
        self.__setStudentId()
        self.__setStudentName()
        self.__setBirthDate()
    
    @classmethod
    def getAllStudents(student):
        return student.__student_infos
    
    def __eq__(self, other):
        return (self.getStudentId() == other.getStudentId())
    
    def printAllStudents():
        if not Student.getAllStudents():
            print("No students.")
            return
        print("Student list:")
        print("ID----Name----Birthdate")
        for student_info in Student.getAllStudents():
            print("{}----{}----{}".format(
                student_info.getStudentId(),
                student_info.getStudentName(),
                student_info.getBirthDate()
            ))

