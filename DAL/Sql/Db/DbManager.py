import pymysql

def getdbbcon():
    con = pymysql.connect(host="localhost", user="root", password="XXXXXXX", database="XXXXXX")
    return con