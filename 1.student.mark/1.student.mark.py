student_infos = []
courses = []

def main():
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
        try:
            m = int(input("Your choice (enter number only): "))
            match m:
                case 1:
                    input_students()
                case 2:
                    input_courses()
                case 3:
                    input_mark()
                case 4:
                    display_students()
                case 5:
                    display_courses()
                case 6:
                    display_mark()
                case 7:
                    break
                case _:
                    print("Invalid input. Try again.")
        except:
            print("Invalid input. Try again.")

def input_students():
    n = int(input("Enter numbers of students: "))
    for i in range(n):
        student_info = {}
        s_id = input("Student ID: ")
        s_name = input("Student Name: ")
        s_birthdate = input("Student Birth Date: ")
        student_info["id"] = s_id
        student_info["name"] = s_name
        student_info["birthdate"] = s_birthdate
        student_infos.append(student_info)

def input_courses():
    n_c = int(input("Enter number of courses: "))
    for _ in range(n_c):
        course = {}
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        course["course_id"] = c_id
        course["course_name"] = c_name
        courses.append(course)

def input_mark():
    if not courses:
        print("No courses available.")
        return
    display_courses()
    course_pick = input("Choose course: ")
    while True:
        for course in courses:
            if course_pick.lower() == course["course_name"].lower():
                for student_info in student_infos:
                    mark = float(input("Enter {}'s {} mark: ".format(student_info["name"], course_pick.lower())))
                    student_info[course_pick.upper()] = mark
                break
        print("Course doesn't match.")
        course_pick = input("Choose course: ")

def display_courses():
    if not courses:
        print("No courses available.")
        return
    print("Course list:")
    print("ID------------------Name")
    for course in courses:
        print("{}      {} ".format(course['course_id'], course['course_name']))

def display_students():
    if not student_infos:
        print("No students.")
        return
    print("Student list:")
    print("ID-------------Name-----------------Birthdate")
    for student_info in student_infos:
        print("{}   {}    {}".format(student_info['id'], student_info['name'], student_info['birthdate']))

def display_mark():
    def course_picking():
        course_pick = input("Choose course: ")
        while True:
            for course in courses:
                if course_pick.lower() == course["course_name"].lower():
                    return course_pick
            print("Course doesn't match.")
            course_pick = input("Choose course: ")

    if not courses:
        print("No courses available.")
        return
    display_courses()
    course_pick = course_picking()    

    print("Student marks:")
    print(f"Student ID ------------ Student name ------------ {course_pick.upper()}")
    for student_info in student_infos:
        print('{}     {}      {}'.format(student_info["id"], student_info["name"], student_info[course_pick.upper()]))

if __name__ == '__main__':
    main()