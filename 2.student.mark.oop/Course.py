class Course:
    __courses = []

    def __init__(self, courseId=None, courseName=None):
        self.__courseId = courseId
        self.__courseName = courseName
        if not self.isCourseDuplicate():
            Course.getAllCourses().append(self)

    def __setCourseId(self):
        newId = input("Enter course id: ")
        for course in Course.getAllCourses():
            if newId == course.getCourseId():
                print("Course Id already exists")
                return

        self.__courseId = newId
    
    def getCourseId(self):
        return self.__courseId
    
    def __setCourseName(self):
        newName = input("Enter course name: ")
        self.__courseName = newName

    def getCourseName(self):
        return self.__courseName
    
    def isCourseDuplicate(self):
        for c in Course.getAllCourses():
            if (self == c):
                return True
        return False
    
    def setCourse(self):
        self.__setCourseId()
        self.__setCourseName()
    
    @classmethod
    def getAllCourses(course):
        return course.__courses
    
    def __eq__(self, other):
        return (self.getCourseId() == other.getCourseId()
            and self.getCourseName() == other.getCourseName())
    
    def printAllCourses():
        if not Course.getAllCourses():
            print("No courses available.")
            return
        print("Course list:")
        print("ID----Name")
        for c in Course.getAllCourses():
            print("{}----{} ".format(
                c.getCourseId(), 
                c.getCourseName()
            ))