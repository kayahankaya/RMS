import tkinter as tk
from tkinter import messagebox
from BL.login_bl import Login_bl
from UI.tabs.Dashboard import Dashboard

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

def login():

    if user_name.get()=="" or password.get()=="":
        textvar1 = "Error"
        textvar2 = "Enter User Name And Password"
        messagebox.showerror(textvar1,textvar2)
    else:
        selected_user = loginobj.get_user_by_username(userentry.get())
        if selected_user.password == passentry.get() and selected_user.user_id == 1:
            textvar1 = "Success"
            textvar2 = "Successfully Admin Login"
            messagebox.showinfo(textvar1,textvar2)
            win.destroy() 
            Dashboard().dash_admin()
        elif selected_user.password == passentry.get() and selected_user.user_id != 1:
            textvar1 = "Success"
            textvar2 = "Successfully User Login"
            messagebox.show_info(textvar1,textvar2)
            win.destroy() 
            Dashboard().dash_user()
        else:
            textvar1 = "Error"
            textvar2 = f"ERROR : {str('Error')}"
            messagebox.showerror(textvar1,textvar2,win)

def clear():
    userentry.delete(0,)
    passentry.delete(0,)

loginobj = Login_bl()

btn_login = tk.Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)

btn_login = tk.Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

win.mainloop()