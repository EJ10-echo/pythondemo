
from tkinter import END, UNDERLINE

UNDERLINE = '\033[4m'
END = '\033[0m'

cls = int(input("Enter the name of the class(1,2,3,4): "))
section = input("Enter the section of the class(A,B,C,D): ").upper()

stud_name1 = "Ebin Joe"
stud_name2 = "John"
stud_name3 = "Mary"

stud_name4 = "Augustus"
stud_name5 = "Rutherford"
stud_name6 = "Marie"

stud_name7 = "Rachel"
stud_name8 = "Marcus"
stud_name9 = "Austin"


# Gender verification part
male_names = [stud_name1, stud_name2, stud_name4, stud_name5, stud_name8, stud_name9]
female_names = [stud_name3, stud_name6, stud_name7]


section_students = {
    "A": [(stud_name1, 1001, "M", "01/01/2010"), (stud_name2, 1002, "M", "05/02/2010"), (stud_name3, 1003, "F", "10/03/2010")],
    "B": [(stud_name4, 1004, "M", "12/04/2010"), (stud_name5, 1005, "M", "22/05/2010"), (stud_name6, 1006, "F", "15/06/2010")],
    "C": [(stud_name7, 1007, "F", "20/07/2010"), (stud_name8, 1008, "M", "30/08/2010"), (stud_name9, 1009, "M", "25/09/2010")]
}

subject_names = [
    "EVS",
    "Maths",
    "Tamil",
    "Music",
    "Arts",
    "Physical Education"
]


def print_student_list(student_info):
    print(f"{UNDERLINE}Saint Joseph International High School{END}")
    print("Grade", cls, "Section", section)
    print(
        f"{UNDERLINE}{'Serial No.':<12}{END} | "
        f"{UNDERLINE}{'Roll No.':<8}{END} | "
        f"{UNDERLINE}{'Name':<20}{END} | "
        f"{UNDERLINE}{'Date of Birth':<18}{END} | "
        f"{UNDERLINE}{'Gender':<10}{END}"
    )
    for index, (name, roll, stud_gender, stud_dob) in enumerate(student_info, start=1):
        print(f"{index:<12} | {roll:<8} | {name:<20} | {stud_dob:<18} | {stud_gender:<10}")


def print_marks_table(student_name, marks):
    print(
        f"\n{UNDERLINE}{'Subject':<25}{END} "
        f"{UNDERLINE}{'Marks':<6}{END}"
    )
    for subject, mark in zip(subject_names, marks):
        print(f"{subject:<25}{mark:<6}")


def get_student_marks(student_name):
    print(f"\nEnter marks for {student_name} in each subject:")
    marks = []
    for subject in subject_names:
        while True:
            try:
                mark = int(input(f"{subject}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Please enter a numeric value.")
    return marks


if cls == 1 and section in section_students:
    selected_students = section_students[section]
    print_student_list(selected_students)

    selected = int(input("\nSelect a student serial number to enter marks (1-3): "))
    if 1 <= selected <= len(selected_students):
        chosen_name, chosen_roll, chosen_gender, chosen_dob = selected_students[selected - 1]
        marks = get_student_marks(chosen_name)
        print(f"\nMarks for {chosen_name} (Roll {chosen_roll}):")
        print_marks_table(chosen_name, marks)
    else:
        print("Invalid student selection.")
else:
    print("No students found for the selected class and section.")