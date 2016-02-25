#coding=utf-8

class Userproduct():

    #@params 传入参数的元祖，例如：(用户姓名, 产品id)
    #插入数据
    def insert(self, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO userproduct(username,product_id) VALUES(?,?)", params)
        conn.commit()

    #删除数据
    def remove(self,conn,params):
        cu = conn.cursor()
        cu.execute("DELETE FROM userproduct WHERE username = ? and product_id= ?",params)
        conn.commit()


    #查询数据
    def select(self,conn,params):
        cu = conn.cursor()
        cu.execute("SELECT * FROM userproduct where username = ?",params)
        #print(cu.fetchall())  #从结果中取出所有数据
        return cu.fetchall()