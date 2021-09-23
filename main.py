import tkinter as tk
from tkinter import *
from tkinter import messagebox

window = tk.Tk()
window.title('Diary')
window.geometry('500x500')
window.config(bg='grey')

password = 123456

def setTextInput(text):
    e.delete(0,"end")
    e.insert(0, text)

def checkPass():

        attempt = int(e.get())

        if attempt != password:
            messagebox.showinfo('', 'Wrong password')
        else:
            openDiary()


        messagebox.showinfo('','You must enter a number')

def openDiary():
    frame.destroy()
    frame2.pack()
    addExistingText()

def addExistingText():
    file = open("diary.txt",'r')
    diaryEntries = file.read()

    diary.insert(END, diaryEntries)
    file.close()

def addEntry():
    file = open("diary.txt",'w')
    newText = file.write(diary.get(1.0,END))

    file.close()

frame = Frame(window)
frame2 = Frame(window)

diary = Text(frame2, width = 40, height = 10)
diary.pack(pady = 20)
saveText = tk.Button(frame2,text = "Save",width = 10,command = lambda:addEntry())
saveText.pack(pady = 20)

label = tk.Label(frame,text="Welcome to your diary",fg="white",bg="black",width=20,height=5)
label.pack(padx = 10 , pady = 10)

e = Entry(frame)
e.pack()
e.focus_set()

enterPassword = tk.Button(frame,text = "Enter Password",command = lambda:checkPass())
enterPassword.pack(padx = 10 , pady = 10)

frame.pack(side ='top',expand = True,fill = 'both')
frame.config(bg="grey")

window.mainloop()
