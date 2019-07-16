course_list = []
class Course:

    def __init__(self, name, term, unit):
        self.name = name
        self.term = term
        self.unit = unit


    def __lt__(self, other):
        return self.unit < other.unit

    def search(course_name, lst):
        for i in range(0, len(lst)):
            if course_name == lst[i].name:
                return i

        return -1

    def addCourse(self):
        self.name = str(input("Enter course name: "))
        course_list.append(self.name)
        self.unit = int(input("Enter class units: "))
        course_list.append(self.unit)
        self.term = (input("Enter the term for this class: "))
        course_list.append(self.term)

    def removeCourse(self):
        remove = input("Enter that course that you would like to remove: ")
        index = search(remove, course_list)
        if index > -1:
            print("found, index = ", index)
            # change(course_list[index], "New name")
        else:
            print("Not found")

    def printList(self):
        print("Course", end="     ")
        print("Unit", end="     ")
        print("Term")
        for x in range(len(course_list)):
            print(course_list[x])

        #return str(self.name) + str(self.unit) + str(self.term)


def insertionSort(lst):
    for i in range(1, len(lst)):
            # insert lst[i] into a sorted sublist lst[0..i-1] so that
            #   lst[0..i] is sorted.
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

            # Insert the current element into lst[k + 1]
            lst[k + 1] = currentElement

    def courseSort(self):
        course_list.sort()
        print(course_list)


def menu():
    print("Please choose 1 of the following options:")
    print("  1. List all courses")
    print("  2. Add a course")
    print("  3. Drop a course")
    print("  4. Sort courses based on course name")
    print("  5. Sort courses based on number of units")
    print("  6. Exit")
    print(" ")
    return eval(input("Enter your option: "))

#program starts running
loop = 1

Course1 = Course("", "", 0)

while loop == 1:
    choice = menu()
    if choice == 1:
        if len(course_list) == 0:
            print("No classes have been inputted.")
        else:
            Course1.printList()
    elif choice == 2:
        Course1.addCourse()
    elif choice == 3:
        Course1.removeCourse()
    elif choice == 4:
        insertionSort()
    elif choice == 5:
        print("not ready yet")
    elif choice == 6:
        loop = 0
        print("Thank you for using the my bank application.")  # end the application
    elif choice <= 0:
        print("Invalid selection. Please try again.")  # error checking
    elif choice > 6:
        print("Invalid selection. Please try again.")  # error checking
