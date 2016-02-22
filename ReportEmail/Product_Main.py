#coding=utf-8

import sqlite3
from ReportEmail.Product import Product

connection = sqlite3.connect("/Users/a1/Desktop/ProjectReport/myData.db")
dao = Product()



dao.insert(connection,("bestie_Android","1.3.0","模块1,模块2,模块4"))
#dao.insert(connection,("bestie_Android","1.4.0","模块1,模块2,模块3"))
#dao.insert(connection,("bestie_Ios","1.1.0","模块1,模块4"))
#dao.insert(connection,("bestie_IOS","1.2.0","模块1,模块2,模块3,模块4"))
#dao.insert(connection,("bestie_IOS","1.3.1","模块2,模块3,模块4"))





connection.close()