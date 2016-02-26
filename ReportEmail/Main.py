# coding=utf-8
import sqlite3

# from ReportEmail.Userinfo import *
# from ReportEmail.Newrequest import *
# from ReportEmail.Newdate import *
# from ReportEmail.Product import *
# from ReportEmail.Receiver import *
# from ReportEmail.Returntesting import *
# from ReportEmail.Userproduct import *
#
# # 为每一个类创建一个对象
# userinfo = Userinfo()
# newrequest = Newrequest()
# newdate = Newdate()
# product = Product()
# receiver = Receiver()
# returntesting = Returntesting()
# userproduct = Userproduct()
#
#
# class DbManager:
#     @classmethod
#     def userinfo_insert(cls, conn, params):
#         userinfo.insert(conn, params)
#
#     @classmethod
#     def userinfo_select(cls, conn, params):
#         result = userinfo.select(conn, params)
#         return result
#
#     @classmethod
#     def userinfo_update(cls, conn, params):
#         userinfo.update(conn, params)
#
#     @classmethod
#     def newrequest_insert(cls,conn,params):
#         newrequest.insert(conn,params)
#
#     @classmethod
#     def newrequest_remove(cls,conn,params):
#         newrequest.remove(conn,params)




def get_connection():
    conn = sqlite3.connect("/Users/a1/Desktop/ProjectReport/myData.db")
    #conn = sqlite3.connect("E:/workspace/python/Report/db/myData.db")
    return conn