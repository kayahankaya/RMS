import tkinter as tk
from tkinter import messagebox
from BL.login_bl import Login_bl

win = tk.Tk()

win.title("RMS")

win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)

heading = tk.Label(win , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

username = tk.Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = tk.Label(win, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

user_name = tk.StringVar()
password = tk.StringVar()

userentry = tk.Entry(win, width=40 , textvariable = user_name)
userentry.insert(tk.END, 'kayahankaya')
userentry.focus()
userentry.place(x=200 , y=223)

passentry = tk.Entry(win, width=40, show="*" ,textvariable = password)
passentry.insert(tk.END, 'Istanbul.ngykkaya91')
passentry.place(x=200 , y=260)

def show_error(textvar1,textvar2):
    messagebox.showerror(textvar1,textvar2)

def show_info(textvar1,textvar2):
    messagebox.showinfo(textvar1,textvar2)

loginobj = Login_bl(user_name,password,win,userentry,passentry,show_error,show_info)

btn_login = tk.Button(win, text = "Login" ,font='Verdana 10 bold',command = loginobj.login)
btn_login.place(x=200, y=293)

btn_login = tk.Button(win, text = "Clear" ,font='Verdana 10 bold', command = loginobj.clear)
btn_login.place(x=260, y=293)

win.mainloop()