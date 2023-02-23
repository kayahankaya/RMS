import pymysql

with open(r"C:\Users\LENOVO\Desktop\password.txt") as f:
    password_input = f.read()


def getdbbcon():
    con = pymysql.connect(host="localhost", user="root", password=password_input, database="rms_kk")
    return con