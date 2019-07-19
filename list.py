 import os.path
if os.path.exists('Course List (4)/Courses1.txt'):
    print("Courses1.txt exists")
else:
    print("Courses1.txt does not exist.")

course_dict = {}
class Course:
    def __init__(self, name, unit, term):
        self.name = name

        self.unit = unit

        self.term = term

    def __str__(self):
        return "name: " + self.name + " unit: " + str(self.unit) + "term: " + str(self.term)

    def __lt__(self, other):
        return self.unit < other.unit

    def addCourse(self, course_dict):
        global name, unit, term
        name = str(input("Enter course name: "))
        course_dict[name] = self.name

        unit = str(input("Enter course units: "))
        course_dict[unit] = self.unit

        term = str(input("Enter course term: "))
        course_dict[term] = self.term


    def removeCourse(self, course_dict):
        removedname = input("Enter that course that you would like to remove: ")
        if removedname in course_dict:

            removedunit = input("Enter the units that you would like to remove: ")

            removedterm = input("Enter the term that you would like to remove: ")

            course_dict.pop(removedname)

            course_dict.pop(removedunit)

            course_dict.pop(removedterm)
        else:
            print("The course", removedname, "does not exist.")

    def printList(self, course_dict):
        print("Course", end="         ")
        print("Unit", end="         ")
        print("Term")

        if len(course_dict) == 0:
            print("No courses exist.")

        else:
            for key in course_dict:
                value = course_dict[key]
                print(key)
    def sortKeys(self, course_dict):
        for key in sorted(course_dict.keys()):
            print(key, course_dict[key])
# this is where i need help so basically im trying to sort and print the course based on their keys which are the names of the courses

def menu():
    print(" ")
    print("Please choose 1 of the following options:")
    print("  1. List all courses")
    print("  2. Add a course")
    print("  3. Drop a course")
    print("  4. Sort courses based on course name")
    print("  5. Exit")
    print(" ")
    return eval(input("Enter your option: "))


# program starts running
loop = 1

Course1 = Course("", "", 0)

while loop == 1:
    choice = menu()
    if choice == 1:  # option 1 is displayed
        if len(course_dict) == 0:
            print("No classes have been inputted.")
        else:
            Course1.printList(course_dict)

    elif choice == 2:  # option 2 is displayed
        Course1.addCourse(course_dict)

    elif choice == 3:  # option 3 is displayed
        Course1.removeCourse(course_dict)

    elif choice == 4:  # option 4 is displayed
        Course1.sortKeys(course_dict)

    elif choice == 5:  # option 5 is displayed
        loop = 0
        print("Thank you for using the course list application!!")
        file1 = open("Courses1.txt", "w")
        file1.write("Course")
        file1.close
        # end the application

    elif choice <= 0:
        print("Invalid selection. Please try again.")  # error checking

    elif choice > 5:
        print("Invalid selection. Please try again.")  # error checking
