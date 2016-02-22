#coding=utf-8

class Userproduct():

    #@params 传入参数的元祖，例如：(产品名, 版本号)
    #插入数据
    def insert(self, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO userproduct VALUES(?, ?)", params)
        conn.commit()

    #删除数据
    def remove(self,conn,params):
        cu = conn.cursor()
        cu.execute("DELETE FROM userproduct WHERE ProductName= ? and Version= ?",params)
        conn.commit()

    #修改数据
    def update(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE userproduct SET Version= ? WHERE ProductName= ? and Version = ?",param)
        conn.commit()

    #查询数据
    def select(self,conn,param):
        cu = conn.cursor()
        cu.execute("SELECT * FROM userproduct where ProductName=?",param)
        #print(cu.fetchall())  #从结果中取出所有数据
        return cu.fetchall()