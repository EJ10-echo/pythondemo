print("Saint Joseph International High School")
sections_count = int(input("Enter the number of sections in the school: "))
sections = []
class_name = input("Enter the name of the class: ")


for i in range(sections_count):
    section_name = input("Enter the name of section {}: ".format(i+1))
    sections.append(section_name)
        
class marvelous:
    def grade(self):
        if class_name == "Grade 1" or class_name == "Grade 2" or class_name == "Grade 3" or class_name == "Grade 4" or class_name == "Grade 5":
            section = input("Enter the section you want to view (A or B or C or D): ")
            if section in sections:
                student_count = int(input(f"Enter the number of students in {class_name}{section}: "))
                students = []
                for i in range(student_count):
                    student_name = input(f"Enter the name of a student in {class_name}{section}: ")
                    student_age = int(input("Enter the age of the student: "))
                    students.append((student_name, student_age))
                print("\n--- Student Details ---")
                for student in students:
                    print("Student Name:", student[0])
                    print("Student Age:", student[1])
                    print("-----------------------")
            else:
                print("Invalid section name")
        else:
            print("Invalid class name")
            

obj = marvelous()
obj.grade()
