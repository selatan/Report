#coding=utf-8


class Product():


    #@conn 数据库连接
    #@params 传入参数的元祖，例如：(产品名, 版本号)
    #插入数据(参数是3or4)
    def insert(self, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO product(product_name, version, component) VALUES(?,?,?)", params)
        conn.commit()
        return cu.lastrowid

    # 删除数据
    def remove(self,conn,id):
        cu = conn.cursor()
        cu.execute("DELETE FROM product WHERE id = ?",id)
        conn.commit()

    #根据id修改成新的版本号
    def updateVersion(self,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE product SET Version= ? WHERE id = ?",params)
        conn.commit()

    #根据id号修改产品的功能模块
    def updateComponent(self,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE product SET component = ? WHERE id = ?",params)
        conn.commit()

    #根据id号查询数据
    def select(self,conn,id):
        cu = conn.cursor()
        cu.execute("SELECT * FROM product where id =?",id)
        #print(cu.fetchall())  #从结果中取出所有数据
        return cu.fetchall()