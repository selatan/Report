#coding=utf-8

import sqlite3
from ReportEmail.Newdate import Newdate
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#connection = sqlite3.connect("E:/workspace/python/Report/db/myData.db")
connection = sqlite3.connect("/Users/a1/Desktop/ProjectReport/myData.db")

dao = Newdate()

#dao.insert(connection,(3,"2016-02-23", None, None,None,None,None,None,None,"5"))
#dao.insert(connection,(3,"2016-02-24", None, None,None,None,None,None,"2", "5"))

# data = dao.select(connection, (3, "2016-02-25"))
# if (data == None) :
#     dao.insert(connection,(3,"2016-02-25", None, None,None,None,None,None,None,"5"))
#     print("insert in executed")
# else :
#     print("update is executed")
#     pass


#dao.insert(connection,("bestie_Android","1.4.0","模块1,模块2,模块3"))
#dao.insert(connection,("bestie_Ios","1.1.0","模块1,模块4"))
#dao.insert(connection,("bestie_IOS","1.2.0","模块1,模块2,模块3,模块4"))
#dao.insert(connection,("bestie_IOS","1.3.1","模块2,模块3,模块4"))





connection.close()