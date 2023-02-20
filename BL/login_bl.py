from DAL.Sql.Repository.UserRepository import UserRepository
from UI.tabs.Dashboard import Dashboard

class Login_bl:
    
    def __init__(self,*args):

        self.user_name = args[0]
        self.password = args[1]
        self.win = args[2]
        self.userentry = args[3]
        self.passentry = args[4]
        self.show_error = args[5]
        self.show_info = args[6]

    def login(self):

        if self.user_name.get()=="" or self.password.get()=="":
            textvar1 = "Error"
            textvar2 = "Enter User Name And Password"
            self.show_error(textvar1,textvar2)
        else:
            user_repository = UserRepository()
            selected_user = user_repository.get_user_by_username(self.userentry.get())
            if selected_user.password == self.passentry.get() and selected_user.user_id == 1:
                textvar1 = "Success"
                textvar2 = "Successfully Admin Login"
                self.show_info(textvar1,textvar2)
                self.win.destroy() 
                Dashboard().dash_admin()
            elif selected_user.password == self.passentry.get() and selected_user.user_id != 1:
                textvar1 = "Success"
                textvar2 = "Successfully User Login"
                self.show_info(textvar1,textvar2)
                self.win.destroy() 
                Dashboard().dash_user()
            else:
                textvar1 = "Error"
                textvar2 = f"ERROR : {str('Error')}"
                self.show_error(textvar1,textvar2,self.win)

    def clear(self):
        self.userentry.delete(0,)
        self.passentry.delete(0,)