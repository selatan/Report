# coding=utf-8

from Userinfo import *
from Newrequest import *
from Newdate import *
from Product import *
from Receiver import *
from Returntesting import *
from Userproduct import *

# 为每一个类创建一个对象
userinfo = Userinfo()
newrequest = Newrequest()
newdate = Newdate()
product = Product()
receiver = Receiver()
returntesting = Returntesting()
userproduct = Userproduct()


class DbManager:
    @classmethod
    def userinfo_insert(cls, conn, params):
        userinfo.insert(conn, params)

    @classmethod
    def userinfo_select(cls, conn, params):
        result = userinfo.select(conn, params)
        return result

    @classmethod
    def userinfo_update(cls, conn, params):
        userinfo.update(conn, params)

    @classmethod
    def newrequest_insert(cls,conn,params):
        newrequest.insert(conn,params)


