import DAL.Sql.Db.DbManager as DbManager
from DAL.Sql.Db.Entities.UserEntity import UserEntity

class UserRepository:

    def __init__(self):

        self.dbcontext = DbManager.getdbbcon()

    def get_user_by_username(self,username):

        cur = self.dbcontext.cursor()
        cur.execute("select * from users where username=%s",(username))
        row = cur.fetchone()
        temp_user = UserEntity()
        temp_user.user_id = row[0]
        temp_user.lastname = row[1]
        temp_user.firstname = row[2]
        temp_user.username = row[3]
        temp_user.password = row[4]
        temp_user.created_at = row[5]
        temp_user.updated_at = row[6]
        return temp_user

    def get_user_by_user_id(self,user_id):

        cur = self.dbcontext.cursor()
        cur.execute("select * from users where user_id=%s",(user_id))
        row = cur.fetchone()
        temp_user = UserEntity()
        temp_user.user_id = row[0]
        temp_user.lastname = row[1]
        temp_user.firstname = row[2]
        temp_user.username = row[3]
        temp_user.password = row[4]
        temp_user.created_at = row[5]
        temp_user.updated_at = row[6]
        return temp_user




            

        


