# Student-Management-System
Simple Student Management System implemented using Python's Tkinter library. It allows users to add, view, delete, search and update student records. The student records are stored in a text file, and the user interface provides functionality to interact with these records.

Features
Add Student: Add a new student record with a name, age, grade, and subjects, then you will get Unique Student ID returned on the screen for 5 seconds.Take a note because you will need it

Update Students: Type student unique ID, then simply change details you want to change.If you want to keep old information just leave the entry box empty.

Delete Student: Delete a student record by specifying the student's unique ID and name.

Search Student: Search for a student record with a unique ID, name, age, grade, and subjects.

View Students: View all student records with a scrollbar for easy navigation. The information will be on the screen for certian time then will disapear.

Usage

Adding a Student

1.Click the "Add Student" button.
2.Fill in the student's name, age, grade, and subjects (comma separated).
3.Click the "Submit" button. The student will be added to the records and saved in students_records.txt.
4.On screen will be displayed unique studen id for 5 sec.

Update Student

1.Click the "Update Student Details" button.
2.Make sure the studen id match your student
3.Fill the student's name, age, grade, and subjects (comma separated).If you want to keep the old details just leave the field empty.

Deleting a Student

1.Click the "Delete Student" button.
2.Enter the student's name and unique ID.
3.Click the "Submit" button. If the student exists, their record will be deleted from the records.

Searching for Student

1.Click the "Search for Student by Name and Id" button.
2.Enter the student's name and unique ID.
3.If they are match to student in students_records.txt the student will be displayed on the screen for 5 sec.


Viewing Students

1.Click the "Get All Students" button.
2.A text box will display all students with a scrollbar for navigation.
3.The list of students will automatically disappear after a set time.


