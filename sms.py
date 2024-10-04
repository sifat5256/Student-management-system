from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
import csv
import os

# Path to the CSV file
csv_file_path = 'students.csv'

# List to store student data
students = []

def delete_student():
    selected_item = studentTable.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'Please select a student to delete')
        return

    selected_student = studentTable.item(selected_item)['values']

    # Confirm deletion
    confirm = messagebox.askyesno('Confirm Delete', f'Are you sure you want to delete the student: {selected_student[1]}?')
    if not confirm:
        return

    for i, student in enumerate(students):
        if student[0] == selected_student[0]:
            del students[i]
            break

    # Remove the selected student from the UI
    studentTable.delete(selected_item)

    messagebox.showinfo('Success', 'Student deleted successfully')
    save_students()  # Save the updated student list to the CSV file
    selected_item = studentTable.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'Please select a student to delete')
        return

    selected_student = studentTable.item(selected_item)['values']
    
    # Confirm deletion
    confirm = messagebox.askyesno('Confirm Delete', f'Are you sure you want to delete the student: {selected_student[1]}?')
    if not confirm:
        return

    for i, student in enumerate(students):
        if student[0] == selected_student[0]:
            del students[i]
            break

    # Remove the selected student from the UI
    studentTable.delete(selected_item)

    messagebox.showinfo('Success', 'Student deleted successfully')
    save_students()  # Save the updated student list to the CSV file

def update_student():
    selected_item = studentTable.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'Please select a student to update')
        return
    selected_student = studentTable.item(selected_item)['values']

    def submit_update():
        student_id = id_entry.get()
        name = name_entry.get()
        mobile = mobile_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        date = time.strftime('%d/%m/%Y')
        current_time = time.strftime('%H:%M:%S')

        if student_id and name and mobile and email and address and gender and dob:
            for i, student in enumerate(students):
                if student[0] == selected_student[0]:
                    students[i] = [student_id, name, mobile, email, address, gender, dob, date, current_time]
                    break
            messagebox.showinfo('Success', 'Student updated successfully')
            save_students()  # Save the updated student list to the CSV file
            update_window.destroy()
            show_students()  # Refresh the Treeview
        else:
            messagebox.showwarning('Warning', 'Please fill all fields')

    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.geometry('400x400')
    update_window.grab_set()

    Label(update_window, text='ID', font=('arial', 14)).grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(update_window, font=('arial', 14))
    id_entry.insert(0, selected_student[0])
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(update_window, text='Name', font=('arial', 14)).grid(row=1, column=0, padx=10, pady=10)
    name_entry = Entry(update_window, font=('arial', 14))
    name_entry.insert(0, selected_student[1])
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(update_window, text='Mobile', font=('arial', 14)).grid(row=2, column=0, padx=10, pady=10)
    mobile_entry = Entry(update_window, font=('arial', 14))
    mobile_entry.insert(0, selected_student[2])
    mobile_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(update_window, text='Email', font=('arial', 14)).grid(row=3, column=0, padx=10, pady=10)
    email_entry = Entry(update_window, font=('arial', 14))
    email_entry.insert(0, selected_student[3])
    email_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(update_window, text='Address', font=('arial', 14)).grid(row=4, column=0, padx=10, pady=10)
    address_entry = Entry(update_window, font=('arial', 14))
    address_entry.insert(0, selected_student[4])
    address_entry.grid(row=4, column=1, padx=10, pady=10)

    Label(update_window, text='Gender', font=('arial', 14)).grid(row=5, column=0, padx=10, pady=10)
    gender_entry = Entry(update_window, font=('arial', 14))
    gender_entry.insert(0, selected_student[5])
    gender_entry.grid(row=5, column=1, padx=10, pady=10)

    Label(update_window, text='Date of Birth', font=('arial', 14)).grid(row=6, column=0, padx=10, pady=10)
    dob_entry = Entry(update_window, font=('arial', 14))
    dob_entry.insert(0, selected_student[6])
    dob_entry.grid(row=6, column=1, padx=10, pady=10)

    Button(update_window, text='Submit', font=('arial', 14), command=submit_update).grid(row=7, columnspan=2, pady=20)




    selected_item = studentTable.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'Please select a student to delete')
        return

    selected_student = studentTable.item(selected_item)['values']
    
    # Confirm deletion
    confirm = messagebox.askyesno('Confirm Delete', f'Are you sure you want to delete the student: {selected_student[1]}?')
    if not confirm:
        return

    for i, student in enumerate(students):
        if student[0] == selected_student[0]:
            del students[i]
            break

    messagebox.showinfo('Success', 'Student deleted successfully')
    save_students()  # Save the updated student list to the CSV file
    show_students()  # Refresh the Treeview

    selected_item = studentTable.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'Please select a student to delete')
        return

    selected_student = studentTable.item(selected_item)['values']
    
    # Confirm deletion
    confirm = messagebox.askyesno('Confirm Delete', f'Are you sure you want to delete the student: {selected_student[1]}?')
    if not confirm:
        return

    for i, student in enumerate(students):
        if student[0] == selected_student[0]:
            del students[i]
            break

    # Remove the selected student from the UI
    studentTable.delete(selected_item)

    messagebox.showinfo('Success', 'Student deleted successfully')
    save_students()  # Save the updated student list to the CSV file

def load_students():
    if os.path.exists(csv_file_path):
        with open(csv_file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                students.append(row)

def save_students():
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'Date of Birth', 'Added Date', 'Added Time'])
        writer.writerows(students)

def connect_database():
    messagebox.showinfo('Database Connection', 'Database connected successfully')

def add_student():
    def submit_add():
        student_id = id_entry.get()
        name = name_entry.get()
        mobile = mobile_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        date = time.strftime('%d/%m/%Y')
        current_time = time.strftime('%H:%M:%S')

        if student_id and name and mobile and email and address and gender and dob:
            # Check if student ID already exists
            for student in students:
                if student[0] == student_id:
                    messagebox.showerror('Error', 'Student ID already exists')
                    return
            students.append([student_id, name, mobile, email, address, gender, dob, date, current_time])
            messagebox.showinfo('Success', 'Student added successfully')
            save_students()  # Save the updated student list to the CSV file
            add_window.destroy()
            show_students()
        else:
            messagebox.showwarning('Warning', 'Please fill all fields')

    add_window = Toplevel()
    add_window.title('Add Student')
    add_window.geometry('400x400')
    add_window.grab_set()

    Label(add_window, text='ID', font=('arial', 14)).grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(add_window, font=('arial', 14))
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(add_window, text='Name', font=('arial', 14)).grid(row=1, column=0, padx=10, pady=10)
    name_entry = Entry(add_window, font=('arial', 14))
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(add_window, text='Mobile', font=('arial', 14)).grid(row=2, column=0, padx=10, pady=10)
    mobile_entry = Entry(add_window, font=('arial', 14))
    mobile_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(add_window, text='Email', font=('arial', 14)).grid(row=3, column=0, padx=10, pady=10)
    email_entry = Entry(add_window, font=('arial', 14))
    email_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(add_window, text='Address', font=('arial', 14)).grid(row=4, column=0, padx=10, pady=10)
    address_entry = Entry(add_window, font=('arial', 14))
    address_entry.grid(row=4, column=1, padx=10, pady=10)

    Label(add_window, text='Gender', font=('arial', 14)).grid(row=5, column=0, padx=10, pady=10)
    gender_entry = Entry(add_window, font=('arial', 14))
    gender_entry.grid(row=5, column=1, padx=10, pady=10)

    Label(add_window, text='Date of Birth', font=('arial', 14)).grid(row=6, column=0, padx=10, pady=10)
    dob_entry = Entry(add_window, font=('arial', 14))
    dob_entry.grid(row=6, column=1, padx=10, pady=10)

    Button(add_window, text='Submit', font=('arial', 14), command=submit_add).grid(row=7, columnspan=2, pady=20)

def show_students():
    for row in studentTable.get_children():
        studentTable.delete(row)
    for student in students:
        studentTable.insert('', END, values=student)

def search_student():
    def search():
        query = search_entry.get()
        search_window.destroy()
        for row in studentTable.get_children():
            studentTable.delete(row)
        for student in students:
            if query.lower() in student[1].lower() or query in student[0]:
                studentTable.insert('', END, values=student)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.geometry('300x100')
    search_window.grab_set()

    Label(search_window, text='Search by ID or Name', font=('arial', 14)).pack(pady=10)
    search_entry = Entry(search_window, font=('arial', 14))
    search_entry.pack(pady=10)

    Button(search_window, text='Search', font=('arial', 14), command=search).pack()

def update_student():
    selected_item = studentTable.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'Please select a student to update')
        return
    selected_student = studentTable.item(selected_item)['values']

    def submit_update():
        student_id = id_entry.get()
        name = name_entry.get()
        mobile = mobile_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        date = time.strftime('%d/%m/%Y')
        current_time = time.strftime('%H:%M:%S')

        if student_id and name and mobile and email and address and gender and dob:
            for i, student in enumerate(students):
                if student[0] == selected_student[0]:
                    students[i] = [student_id, name, mobile, email, address, gender, dob, date, current_time]
                    break
            messagebox.showinfo('Success', 'Student updated successfully')
            save_students()  # Save the updated student list to the CSV file
            update_window.destroy()
            show_students()
        else:
            messagebox.showwarning('Warning', 'Please fill all fields')

    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.geometry('400x400')
    update_window.grab_set()

    Label(update_window, text='ID', font=('arial', 14)).grid(row=0, column=0, padx=10, pady=10)
    id_entry = Entry(update_window, font=('arial', 14))
    id_entry.insert(0, selected_student[0])
    id_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(update_window, text='Name', font=('arial', 14)).grid(row=1, column=0, padx=10, pady=10)
    name_entry = Entry(update_window, font=('arial', 14))
    name_entry.insert(0, selected_student[1])
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    Label(update_window, text='Mobile', font=('arial', 14)).grid(row=2, column=0, padx=10, pady=10)
    mobile_entry = Entry(update_window, font=('arial', 14))
    mobile_entry.insert(0, selected_student[2])
    mobile_entry.grid(row=2, column=1, padx=10, pady=10)

    Label(update_window, text='Email', font=('arial', 14)).grid(row=3, column=0, padx=10, pady=10)
    email_entry = Entry(update_window, font=('arial', 14))
    email_entry.insert(0, selected_student[3])
    email_entry.grid(row=3, column=1, padx=10, pady=10)

    Label(update_window, text='Address', font=('arial', 14)).grid(row=4, column=0, padx=10, pady=10)
    address_entry = Entry(update_window, font=('arial', 14))
    address_entry.insert(0, selected_student[4])
    address_entry.grid(row=4, column=1, padx=10, pady=10)

    Label(update_window, text='Gender', font=('arial', 14)).grid(row=5, column=0, padx=10, pady=10)
    gender_entry = Entry(update_window, font=('arial', 14))
    gender_entry.insert(0, selected_student[5])
    gender_entry.grid(row=5, column=1, padx=10, pady=10)

    Label(update_window, text='Date of Birth', font=('arial', 14)).grid(row=6, column=0, padx=10, pady=10)
    dob_entry = Entry(update_window, font=('arial', 14))
    dob_entry.insert(0, selected_student[6])
    dob_entry.grid(row=6, column=1, padx=10, pady=10)

    Button(update_window, text='Submit', font=('arial', 14), command=submit_update).grid(row=7, columnspan=2, pady=20)

def delete_student():
    selected_item = studentTable.selection()
    if not selected_item:
        messagebox.showwarning('Warning', 'Please select a student to delete')
        return

    selected_student = studentTable.item(selected_item)['values']
    
    # Confirm deletion
    confirm = messagebox.askyesno('Confirm Delete', f'Are you sure you want to delete the student: {selected_student[1]}?')
    if not confirm:
        return

    for i, student in enumerate(students):
        if student[0] == selected_student[0]:
            del students[i]
            break

    messagebox.showinfo('Success', 'Student deleted successfully')
    save_students()  # Save the updated student list to the CSV file
    show_students()  # Refresh the student table display


    if not students:
        messagebox.showwarning('Warning', 'No data to export')
        return

    with open('students_export.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'Date of Birth', 'Added Date', 'Added Time'])
        writer.writerows(students)
    messagebox.showinfo('Success', 'Student data exported successfully')


    if not students:
        messagebox.showwarning('Warning', 'No data to export')
        return

    with open('students_export.txt', 'w') as file:
        file.write("Student Data:\n\n")
        for student in students:
            file.write(f"ID: {student[0]}\n")
            file.write(f"Name: {student[1]}\n")
            file.write(f"Mobile No: {student[2]}\n")
            file.write(f"Email: {student[3]}\n")
            file.write(f"Address: {student[4]}\n")
            file.write(f"Gender: {student[5]}\n")
            file.write(f"Date of Birth: {student[6]}\n")
            file.write(f"Added Date: {student[7]}\n")
            file.write(f"Added Time: {student[8]}\n")
            file.write("\n")

    messagebox.showinfo('Success', 'Student data exported successfully')




def export_students():
    if not students:
        messagebox.showwarning('Warning', 'No data to export')
        return

    file_path = 'students_export.txt'  # Define the file path

    with open(file_path, 'w') as file:
        file.write("Student Data:\n\n")
        for student in students:
            file.write(f"ID: {student[0]}\n")
            file.write(f"Name: {student[1]}\n")
            file.write(f"Mobile No: {student[2]}\n")
            file.write(f"Email: {student[3]}\n")
            file.write(f"Address: {student[4]}\n")
            file.write(f"Gender: {student[5]}\n")
            file.write(f"Date of Birth: {student[6]}\n")
            file.write(f"Added Date: {student[7]}\n")
            file.write(f"Added Time: {student[8]}\n")
            file.write("\n")

    # Show success message
    messagebox.showinfo('Success', 'Student data exported successfully')

    # Open the exported file in Notepad
    os.startfile(file_path, 'open')


count = 0
text = ''

def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(300, slider)

def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)

root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+0+0')
root.resizable(0, 0)
root.title('Student Management System Dashboard')

datetimeLabel = Label(root, font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()
s = 'Student Management System'
sliderLabel = Label(root, text=s, font=('times new roman', 28, 'italic bold'), width=40)
sliderLabel.place(x=200, y=0)
slider()

connectDb = ttk.Button(root, text='Connect Database', command=connect_database)
connectDb.place(x=1000, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file='studenta.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=22, command=add_student)
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=22, command=search_student)
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=22, command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=22, command=update_student)
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=22, command=show_students)
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton = ttk.Button(leftFrame, text='Export Student', width=22, command=export_students)
exportstudentButton.grid(row=6, column=0, pady=20)

exitstudentButton = ttk.Button(leftFrame, text='Exit', width=22, command=root.quit)
exitstudentButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

Scrollbarx = Scrollbar(rightFrame, orient=HORIZONTAL)
Scrollbary = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'Date of Birth', 'Added Date', 'Added Time'),
                            xscrollcommand=Scrollbarx.set, yscrollcommand=Scrollbary.set)

Scrollbarx.config(command=studentTable.xview)
Scrollbary.config(command=studentTable.yview)
Scrollbarx.pack(side=BOTTOM, fill=X)
Scrollbary.pack(side=RIGHT, fill=Y)
studentTable.pack(fill=BOTH, expand=1)

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile No', text='Mobile No')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('Date of Birth', text='Date of Birth')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')

studentTable.config(show='headings')





# Load students from the CSV file on startup
load_students()
show_students()

root.mainloop()
