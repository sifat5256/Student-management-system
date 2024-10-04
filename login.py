from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if userNameEntry.get()=='' or userPasswordEntry.get()=='':
        messagebox.showerror('Error','fields can not be empty')
    elif userNameEntry.get()=='sifat' and userPasswordEntry.get()=='12345':
        messagebox.showinfo('success','welcome')
        window.destroy()
        import sms
        
    else:
        messagebox.showerror('Error','Please enter correct details')
window=Tk()
window.geometry('1280x700+0+0')
window.title('log in  student management System')
window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=backgroundImage)

bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')

loginFrame.place(x=400,y=150)
logoImage=PhotoImage(file='student.png')
logoLavel=Label(loginFrame,image=logoImage)
logoLavel.grid(row=0,column=0,columnspan=2,pady=10)



userNameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=userNameImage,text='User name',compound=LEFT,
font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10)

userNameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=2,fg='royalblue')
userNameEntry.grid(row=1,column=1,pady=10,padx=20)





userPasswordImage=PhotoImage(file='password.png')
userPasswordLabel=Label(loginFrame,image=userPasswordImage,text='Password',compound=LEFT,
font=('times new roman',20,'bold'),bg='white')
userPasswordLabel.grid(row=2,column=0,pady=10)

userPasswordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=2,fg='royalblue')
userPasswordEntry.grid(row=2,column=1,pady=10,padx=20)


loginButton=Button(loginFrame,text='Login',font=('times new roman',16,'bold'),bg='cornflowerblue',width=12,fg='white',activebackground='cornflowerblue',activeforeground='white',cursor='hand2',

command=login)
loginButton.grid(row=3,column=1)



window.mainloop()
