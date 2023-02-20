import pymysql

def getdbbcon():
    con = pymysql.connect(host="localhost", user="root", password="4evdhpmjq21X", database="rms_kk")
    return con