from DAL.Sql.Repository.UserRepository import UserRepository

class Login_bl:
    
    def get_user_by_username(self,username):
        return UserRepository().get_user_by_username(username)