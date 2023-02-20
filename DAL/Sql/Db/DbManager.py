import pymysql

def getdbbcon():
    con = pymysql.connect(host="localhost", user="root", password="XXXXXXXXXX", database="rms_kk")
    return con