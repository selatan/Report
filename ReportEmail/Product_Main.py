#coding=utf-8

import sqlite3
from ReportEmail.Product import Product
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')

#connection = sqlite3.connect("E:/workspace/python/Report/db/myData.db")
connection = sqlite3.connect("/Users/a1/Desktop/ProjectReport/myData.db")


dao = Product()
id = dao.insert(connection,("bestie_Android","1.3.2",unicode("模块1,模块2")))
print(id)
id = dao.insert(connection,("bestie_Android","1.3.3",unicode("模块1,模块2")))
print(id)

#dao.insert(connection,("bestie_Android","1.4.0","模块1,模块2,模块3"))
#dao.insert(connection,("bestie_Ios","1.1.0","模块1,模块4"))
#dao.insert(connection,("bestie_IOS","1.2.0","模块1,模块2,模块3,模块4"))
#dao.insert(connection,("bestie_IOS","1.3.1","模块2,模块3,模块4"))





connection.close()