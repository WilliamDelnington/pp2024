import math
import numpy as np
from curses.textpad import Textbox, rectangle
import curses
import time

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

            win = curses.newwin(3, 18, 3, 1)
            box = Textbox(win)
            rectangle(stdscr, 2, 0, 4, 19)
            stdscr.addstr(8, 0, "Press Ctrl + G to confirm the input.")

            stdscr.refresh()

            box.edit()
            newId = box.gather().replace("\n", "").replace(" ", "")

            #newId = int(input("Enter student id: "))
            if (newId == "") or (any(newId == student.getStudentId() for student in StudentBasicInfo.getAllStudentBasicInfos())):
                stdscr.clear()
                stdscr.addstr("Student ID already exists or can't be blanked.")
                stdscr.refresh()
                stdscr.getch()
                time.sleep(2)
            else:
                break

        stdscr.addstr(10, 0, f"The value you entered is: {newId}")
        stdscr.addstr(11, 0, "Press any key to continue...")

        self.__studentId = newId
        stdscr.getch()

    def getStudentId(self):
        return self.__studentId

    def __setStudentName(self, stdscr):
        # newName = input("Enter student name: ")
        stdscr.clear()
        stdscr.addstr(0, 0, "Add Student Name")
        stdscr.addstr(1, 0, "Enter student's name:")

        win = curses.newwin(3, 29, 3, 1)
        box = Textbox(win)
        rectangle(stdscr, 2, 0, 4, 30)
        stdscr.addstr(8, 0, "Press Ctrl + G to exit the input progress.")

        stdscr.refresh()

        box.edit()
        newName = box.gather().replace("\n", "")
        stdscr.addstr(10, 0, f"The value you entered is: {newName}")
        stdscr.addstr(11, 0, "Press any key to continue.")

        self.__studentName = newName
        stdscr.getch()

    def getStudentName(self):
        return self.__studentName
    
    def __setBirthDate(self, stdscr):
        # newBirthDate = input("Enter birth date: ")
        stdscr.clear()
        stdscr.addstr(0, 0, "Add Student Birthdate")
        stdscr.addstr(1, 0, "Enter student's birthdate:")

        win = curses.newwin(3, 18, 3, 1)
        box = Textbox(win)
        rectangle(stdscr, 2, 0, 4, 19)
        stdscr.addstr(8, 0, "Press Ctrl + G to exit the input progress.")

        stdscr.refresh()

        box.edit()
        newBirthDate = box.gather().replace("\n", "")
        stdscr.addstr(10, 0, f"The value you entered is: {newBirthDate}")
        stdscr.addstr(11, 0, "Press any key to continue.")

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
    
    # @classmethod
    # def printAllStudents(cls, stdscr):
    #     stdscr.clear()

    #     student_list = StudentBasicInfo.getAllStudentBasicInfos()

    #     if not student_list:
    #         # print("No students.")
    #         stdscr.addstr("No students.")
    #         stdscr.refresh()
    #         stdscr.getch()
    #         return
    #     # print("Student list:")
    #     # print("ID----Name----Birthdate")
    #     # for student_info in Student.getAllStudents():
    #     #     print("{}----{}----{}".format(
    #     #         student_info.getStudentId(),
    #     #         student_info.getStudentName(),
    #     #         student_info.getBirthDate()
    #     #     ))

    #     stdscr.addstr(1, 0, "Student list: ")
    #     stdscr.addstr(2, 2, "ID")
    #     stdscr.addstr(2, 16, "Name")
    #     stdscr.addstr(2, 42, "Birthdate")

    #     for s in student_list:
    #         stdscr.addstr(3 + student_list.index(s), 0, s.getStudentId())
    #         stdscr.addstr(3 + student_list.index(s), 13, s.getStudentName())
    #         stdscr.addstr(3 + student_list.index(s), 40, s.getBirthDate())

    #     stdscr.refresh()
    #     stdscr.getch()

# def main(stdscr):
#     sbi1 = StudentBasicInfo()
#     sbi1.setStudent(stdscr)

#     sbi2 = StudentBasicInfo()
#     sbi2.setStudent(stdscr)

#     sbi3 = StudentBasicInfo()
#     sbi3.setStudent(stdscr)

#     StudentBasicInfo.printAllStudents(stdscr)

# curses.wrapper(main)