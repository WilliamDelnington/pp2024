import time
from input import cursesInput
from output import print_message

class StudentBasicInfo:
    """This is a Student class that have attributes 
    all privated, and some specific methods."""
    __student_infos = []

    def __init__(self, studentId=None, studentName=None, birthdate=None):
        self.__studentId = studentId
        self.__studentName = studentName
        self.__birthdate = birthdate
        if not self.isStudentDuplicate():
            StudentBasicInfo.getAllStudentBasicInfos().append(self)

    def __setStudentId(self, stdscr):
        stdscr.clear()
        newId = None
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Add Student ID")
            stdscr.addstr(1, 0, "Enter student's id (Please do not space out):")

            input_val = cursesInput(stdscr, 18, 3, 3, 1)
            newId = input_val.replace("\n", "").replace(" ", "")

            if (newId == "") or (any(newId == student.getStudentId() for student in StudentBasicInfo.getAllStudentBasicInfos())):
                stdscr.clear()
                stdscr.addstr("Student ID already exists or can't be blanked.")
                stdscr.refresh()
                stdscr.getch()
                time.sleep(2)
            else:
                break

        print_message(stdscr, 10, 0, f"The value you entered is: {newId}")
        print_message(stdscr, 11, 0, "Press any key to continue...")

        self.__studentId = newId
        stdscr.getch()

    def getStudentId(self):
        return self.__studentId

    def __setStudentName(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Add Student Name")
        stdscr.addstr(1, 0, "Enter student's name:")

        newName = cursesInput(stdscr, 29, 3, 3, 1).replace("\n", "")
        print_message(stdscr, 10, 0, f"The value you entered is: {newName}")
        print_message(stdscr, 11, 0, "Press any key to continue.")

        self.__studentName = newName
        stdscr.getch()

    def getStudentName(self):
        return self.__studentName
    
    def __setBirthDate(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "Add Student Birthdate")
        stdscr.addstr(1, 0, "Enter student's birthdate:")

        newBirthDate = cursesInput(stdscr, 18, 3, 3, 1).replace("\n", "")
        print_message(stdscr, 10, 0, f"The value you entered is: {newBirthDate}")
        print_message(stdscr, 11, 0, "Press any key to continue.")

        self.__birthdate = newBirthDate
        stdscr.getch()
    
    def getBirthDate(self):
        return self.__birthdate
    
    def isStudentDuplicate(self):
        return any(self == student for student in StudentBasicInfo.getAllStudentBasicInfos())
    
    def setStudent(self, stdscr):
        self.__setStudentId(stdscr)
        self.__setStudentName(stdscr)
        self.__setBirthDate(stdscr)
    
    @classmethod
    def getAllStudentBasicInfos(student):
        return student.__student_infos
    
    def __eq__(self, other):
        return (self.getStudentId() == other.getStudentId())