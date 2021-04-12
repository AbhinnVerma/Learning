from tkinter import *
import mysql.connector
from tkinter import messagebox


def Submit():
    name = nameEntry.get()
    passwd = passwdEntry.get()
    if (nameEntry and passwdEntry)!= '':
        outputEntry.delete(0, END)
        outputEntry.insert(0,f"{name}, {passwd}")
        
        cursor.execute("Select * FROM ids")
        messagebox.showinfo("Log in", "Logged in Successfully!")

def Create():
    signUpName = nameEntrySignUp.get()
    signUpPasswd = passwdEntrySignUp.get()
    if (signUpName and signUpPasswd)!= '':
        outputEntry.delete(0, END)
        outputEntry.insert(0, f"{signUpName}, {signUpPasswd}")
        
        cursor.execute(f"Insert into ids(name, passwd) VALUES({signUpName}, {signUpPasswd});")
        messagebox.showinfo("Sign Up", "Creation Successful!")

def something():
    pass
#-------------------------------- DB --------------------------------
db = mysql.connector.connect(host="localhost", user="root", passwd="password", database="loginsys")
cursor = db.cursor()
cursor.execute("Create table if not exists ids(name varchar(30) PRIMARY KEY, passwd varchar(30) NOT NULL);")


#-------------------------------- UI -----------------------------------
root = Tk()
root.geometry("550x240")
root.title("Login Basic")
root.resizable(False, True)

# Frame
loginFrame = LabelFrame(root, text="Login", padx=10, pady=10)
loginFrame.grid(row=0, column=0, padx=10, pady=10)

signUpFrame = LabelFrame(root, text="Signup", padx=10, pady=10)
signUpFrame.grid(row=0, column=1, padx=10, pady=10)

outputFrame = LabelFrame(root, text="Output", padx=10, pady=10)
outputFrame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Label
nameLabel = Label(loginFrame, text="Name : ")
nameLabel.grid(row=0, column=0)

passwdLabel = Label(loginFrame, text="Password : ")
passwdLabel.grid(row=1, column=0)

nameLabelSignUp = Label(signUpFrame, text="Name : ")
nameLabelSignUp.grid(row=0, column=0)

passwdLabelSignUp = Label(signUpFrame, text="Password : ")
passwdLabelSignUp.grid(row=1, column=0)

outputLabel = Label(outputFrame, text="OUTPUT : ")
outputLabel.grid(row=0, column=0)

# Entries
###--- Log In
nameEntry = Entry(loginFrame, width = 25)
nameEntry.grid(row=0, column=1)

passwdEntry = Entry(loginFrame, width = 25, show = "*")
passwdEntry.grid(row=1, column=1)
###--- Sign UP
nameEntrySignUp = Entry(signUpFrame, width = 25)
nameEntrySignUp.grid(row=0, column=1)

passwdEntrySignUp = Entry(signUpFrame, width = 25)
passwdEntrySignUp.grid(row=1, column=1)
###--- Output
outputEntry = Entry(outputFrame, width=50)
outputEntry.grid(row=0,column=1, columnspan=2)

# Buttons
submitButton = Button(loginFrame, text="Submit", width=20, command=Submit)
submitButton.grid(row=3, column=1)

createButton = Button(signUpFrame, text="Create", width=20, command=Create)
createButton.grid(row=3, column=1)


root.mainloop()
