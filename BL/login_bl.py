from tkinter import messagebox
from DAL.Sql.Repository.UserRepository import UserRepository
from BL.Dashboard import Dashboard

class Login_bl:
    def __init__(self,user_name,password,win,userentry,passentry):

        self.user_name = user_name
        self.password = password
        self.win = win
        self.userentry = userentry
        self.passentry = passentry

    def login(self):

        if self.user_name.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","Enter User Name And Password",parent = self.win)    
        else:
            user_repository = UserRepository()
            selected_user = user_repository.get_user_by_username(self.userentry.get())
            if selected_user.password == self.passentry.get() and selected_user.user_id == 1:
                messagebox.showinfo("Success" , "Successfully Admin Login" , parent = self.win)
                self.win.destroy() 
                Dashboard.dash_admin()
            elif selected_user.password == self.passentry.get() and selected_user.user_id != 1:
                messagebox.showinfo("Success" , "Successfully User Login" , parent = self.win)
                self.win.destroy() 
                Dashboard.dash_user()
            else:
                messagebox.showerror("Error" , f"ERROR : {str('Error')}", parent = self.win)

    def clear(self):
        self.userentry.delete(0,)
        self.passentry.delete(0,)