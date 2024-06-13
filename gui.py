import random
from tkinter import *
import json

# Create text file to store student records if it doesn't exist
#students_file = open("students_records.txt", "x",  encoding='utf-8')

# Create GUI
window = Tk()

# getting screen width and height of display to set full screen
# width = window.winfo_screenwidth()
# height = window.winfo_screenheight()
# window.geometry("%dx%d" % (width, height))


# setting tkinter window size
window.geometry("500x500")
window.title("Student Managing System")


# Global GUI widgets
student_name = None
student_name_label = None
student_age = None
student_age_label = None
student_grade = None
student_grade_label = None
student_subjects = None
student_subjects_label = None
student_id = None
student_id_label = None
delete_button = None
add_button = None
update_button = None
search_button = None
TIME = 5000
WIDGET_WIDTH = 40


def remove_widgets(*args, **kwargs):
    """Remove widgets from screen but not delete them"""
    for widget in args:
        widget.pack_forget()

    for key, value in kwargs.items():
        value.pack_forget()


def destroy_labels(*args):
    """Delete labels from screen after certain time"""
    for widget in args:
        widget.destroy()


def disable_buttons():
    """Disable main buttons until entry fields details are submitted"""
    add_students.config(text="Add Student", width=WIDGET_WIDTH, state=DISABLED)
    update_student.config(text="Update Student Details", width=WIDGET_WIDTH, state=DISABLED)
    delete_student.config(text="Delete Student", width=WIDGET_WIDTH, state=DISABLED)
    search_for_student.config(text="Search for Student by Name and Id", width=WIDGET_WIDTH, state=DISABLED)
    all_students.config(text="Get All Students", width=WIDGET_WIDTH, state=DISABLED)


def enable_buttons():
    """Enable main buttons when entry fields details are submitted"""
    add_students.config(text="Add Student", width=WIDGET_WIDTH, state=NORMAL)
    update_student.config(text="Update Student Details", width=WIDGET_WIDTH, state=NORMAL)
    delete_student.config(text="Delete Student", width=WIDGET_WIDTH, state=NORMAL)
    search_for_student.config(text="Search for Student by Name and Id", width=WIDGET_WIDTH, state=NORMAL)
    all_students.config(text="Get All Students", width=WIDGET_WIDTH, state=NORMAL)


def add_student():
    """Create entry fields to add student detail"""
    global add_button, student_name, student_name_label, student_age, student_age_label, student_grade, student_grade_label, student_subjects, student_subjects_label,WIDGET_WIDTH

    student_name_label = Label(window, text="Student Name:")
    student_name_label.pack()
    student_name = Entry(window, width=WIDGET_WIDTH)
    student_name.pack()

    student_age_label = Label(window, text="Student Age:")
    student_age_label.pack()
    student_age = Entry(window, width=WIDGET_WIDTH)
    student_age.pack()

    student_grade_label = Label(window, text="Student Grade:")
    student_grade_label.pack()
    student_grade = Entry(window, width=WIDGET_WIDTH)
    student_grade.pack()

    student_subjects_label = Label(window, text="Subjects (comma separated):")
    student_subjects_label.pack()
    student_subjects = Entry(window, width=WIDGET_WIDTH)
    student_subjects.pack()

    add_button = Button(text="Submit", width=WIDGET_WIDTH, command=add_values)
    add_button.pack()

    disable_buttons()


def add_values():
    """Get student details to text file"""
    global student_name, student_age, student_grade, student_subjects, student_id, add_button, TIME
    students_from_text_file = []
    # generate unique student id
    unique_id = random.randint(1000, 9999)

    name = student_name.get()
    age = student_age.get()
    grade = student_grade.get()
    subjects = student_subjects.get().split(",")

    new_student = {unique_id: {
        "name": name,
        "age": age,
        "grade": grade,
        "subjects": subjects
    }
    }
    # Check if student id is already exist
    with open("students_records.txt", "r") as file:
        for line in file:
            data = json.loads(line.strip())
            students_from_text_file.append(data)

        for student in students_from_text_file:
            first_key = next(iter(student))
            while first_key == unique_id:
                unique_id = random.randint(1000, 9999)

    with open("students_records.txt", "a+", encoding='utf-8') as file:
        file.write(json.dumps(new_student))
        file.write('\n')

    student_id = Label(window, text=f"Student Unique Id: {unique_id}", background="green", font="bolt")
    student_id.pack()
    window.update()
    window.after(TIME, destroy_labels(student_id))

    remove_widgets(add_button, student_name, student_name_label, student_age, student_age_label, student_grade,
                   student_grade_label, student_subjects, student_subjects_label)

    enable_buttons()


def update_student_details():
    """Create entry fields for updating student details """
    global update_button, student_id, student_id_label, student_name, student_name_label, student_age, student_age_label, student_grade, student_grade_label, student_subjects, student_subjects_label,WIDGET_WIDTH

    student_id_label = Label(window, text="Student Unique Id:")
    student_id_label.pack()
    student_id = Entry(window, width=WIDGET_WIDTH)
    student_id.pack()

    student_name_label = Label(window, text="Student Name:")
    student_name_label.pack()
    student_name = Entry(window, width=WIDGET_WIDTH)
    student_name.pack()

    student_age_label = Label(window, text="Student Age:")
    student_age_label.pack()
    student_age = Entry(window, width=WIDGET_WIDTH)
    student_age.pack()

    student_grade_label = Label(window, text="Student Grade:")
    student_grade_label.pack()
    student_grade = Entry(window, width=WIDGET_WIDTH)
    student_grade.pack()

    student_subjects_label = Label(window, text="Subjects (comma separated):")
    student_subjects_label.pack()
    student_subjects = Entry(window, width=WIDGET_WIDTH)
    student_subjects.pack()

    update_button = Button(text="Update", width=WIDGET_WIDTH, command=update_details)
    update_button.pack()

    disable_buttons()


def update_details():
    """Update student details in text file"""
    global student_name, student_name_label, student_age, student_age_label, student_grade, student_grade_label, student_subjects, student_subjects_label, student_id, update_button,TIME
    students_from_text_file = []

    name = student_name.get()
    age = student_age.get()
    grade = student_grade.get()
    subjects = student_subjects.get()
    unique_id = student_id.get()

    with open("students_records.txt", "r") as file:
        message = ""
        for line in file:
            data = json.loads(line.strip())
            students_from_text_file.append(data)
        if len(students_from_text_file) > 0:

            for student in students_from_text_file:
                first_key = next(iter(student))
                # check for new details, if the field is left blank the details not going to be changed
                if first_key == unique_id:
                    if name != "":
                        student[first_key]["name"] = name
                    if age != "":
                        student[first_key]["age"] = age
                    if grade != "":
                        student[first_key]["grade"] = grade
                    if subjects != "":
                        student[first_key]["subjects"] = subjects.split(",")
                    message = f"Student with ID: {unique_id} details are updated"
                    break
            else:
                message = "No student found"

    update_message = Label(window, text=message)
    update_message.pack()

    window.update()
    window.after(TIME, destroy_labels(update_message))

    with open("students_records.txt", "w") as file:
        for student in students_from_text_file:
            file.write(json.dumps(student))
            file.write('\n')

    remove_widgets(update_button, student_id, student_id_label, student_name, student_name_label, student_age,
                   student_age_label, student_grade,
                   student_grade_label, student_subjects, student_subjects_label)

    enable_buttons()


def delete_student_details():
    """Create entry fields for deleting student"""
    global student_name, student_name_label, student_id, student_id_label, delete_button, WIDGET_WIDTH

    student_name_label = Label(window, text="Student Name:")
    student_name_label.pack()
    student_name = Entry(window, width=WIDGET_WIDTH)
    student_name.pack()

    student_id_label = Label(window, text="Student Unique Id:")
    student_id_label.pack()
    student_id = Entry(window, width=WIDGET_WIDTH)
    student_id.pack()

    delete_button = Button(text="Delete", width=WIDGET_WIDTH, command=delete)
    delete_button.pack()

    disable_buttons()


def delete():
    """Delete student from the text file"""
    global student_name, student_name_label, student_id, student_id_label, delete_button,TIME
    students_from_text_file = []

    student_unique_id = student_id.get()
    name = student_name.get()
    message = ""
    # Check if  student is in text file and delete it
    with open("students_records.txt", "r") as file:

        for line in file:
            data = json.loads(line.strip())
            students_from_text_file.append(data)

        for student in students_from_text_file:
            first_key = next(iter(student))

            if first_key == student_unique_id and name == student[first_key]["name"]:
                message = f"{name} with student id {student_unique_id} was deleted "
                students_from_text_file.remove(student)
                break

        else:
            message = "No student found"

    with open("students_records.txt", "w") as file:
        for student in students_from_text_file:
            file.write(json.dumps(student))
            file.write('\n')

    remove_widgets(student_name, student_name_label, student_id, student_id_label, delete_button)
    deleted_student = Label(window, text=message, background="red")
    deleted_student.pack()
    window.update()
    window.after(TIME, destroy_labels(deleted_student))

    enable_buttons()


def search_student():
    """Create entry fields for student search"""
    global student_name, student_name_label, student_id, student_id_label, search_button, WIDGET_WIDTH

    student_name_label = Label(window, text="Student Name:")
    student_name_label.pack()
    student_name = Entry(window, width=WIDGET_WIDTH)
    student_name.pack()

    student_id_label = Label(window, text="Student Unique Id:")
    student_id_label.pack()
    student_id = Entry(window, width=WIDGET_WIDTH)
    student_id.pack()

    search_button = Button(text="Search", width=WIDGET_WIDTH, command=search)
    search_button.pack()

    disable_buttons()

def search():
    """Search for student in text file"""
    global student_name, student_name_label, student_id, student_id_label, search_button, TIME
    students_from_text_file = []
    student_unique_id = student_id.get()
    name = student_name.get()
    message = ""

    with open("students_records.txt", "r") as file:
        for line in file:
            data = json.loads(line.strip())
            students_from_text_file.append(data)

        for student in students_from_text_file:
            first_key = next(iter(student))

            if first_key == student_unique_id and name == student[first_key]["name"]:
                age = student[first_key]["age"]
                grade = student[first_key]["grade"]
                subjects = student[first_key]["subjects"]
                message = f"Student Name: {name}\nStudent age: {age}\nStudent grade: {grade}\nSubjects: {' ,'.join(subjects)}"
                break
        else:
            message = "No students in database"
        searched_student = Label(window, text=message, background="yellow")
        searched_student.pack()

    window.update()
    window.after(TIME, destroy_labels(searched_student))
    print(message)
    remove_widgets(student_name, student_name_label, student_id, student_id_label, search_button)
    enable_buttons()


def list_of_students():
    """Get all students from the text file"""

    # Create a scrollbar and Text box to display all available students
    scroll_bar = Scrollbar(window)
    scroll_bar.pack(side=RIGHT, fill=Y)
    all_students_ = Text(window, yscrollcommand=scroll_bar.set)
    all_students_.pack(expand=True)
    scroll_bar.config(command=all_students_.yview)

    students_from_text_file = []
    message = ""
    with open("students_records.txt", "r") as file:

        for line in file:
            data = json.loads(line.strip())
            students_from_text_file.append(data)
        if len(students_from_text_file) > 0 :

            for student in students_from_text_file:
                first_key = next(iter(student))
                name = student[first_key]["name"]
                age = student[first_key]["age"]
                grade = student[first_key]["grade"]
                subjects = student[first_key]["subjects"]
                message += f"Student unique ID: {first_key}\nStudent Name: {name}\nStudent age: {age}\nStudent grade: {grade}\nSubjects: {' ,'.join(subjects)}"
                message += f"\n{'#' * 20}\n{'#' * 20}\n"


        else:
            message = "No students in database"
    all_students_.insert(END, message)
    all_students_.config(state=DISABLED)

    window.update()
    window.after(20000, lambda: destroy_labels(all_students_, scroll_bar))


add_students = Button(text="Add Student", width=WIDGET_WIDTH, command=add_student)
add_students.pack()

update_student = Button(text="Update Student Details", width=WIDGET_WIDTH, command=update_student_details)
update_student.pack()

delete_student = Button(text="Delete Student", width=WIDGET_WIDTH, command=delete_student_details)
delete_student.pack()

search_for_student = Button(text="Search for Student by Name and Id", width=WIDGET_WIDTH, command=search_student)
search_for_student.pack()

all_students = Button(text="Get All Students", width=WIDGET_WIDTH, command=list_of_students)
all_students.pack()

window.mainloop()
