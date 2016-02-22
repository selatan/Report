#coding=utf-8



class Userinfo():

    #插入数据
    def insert(self,conn,param):
        cu=conn.cursor()
        cu.execute("INSERT INTO userinfo VALUES(?,?,?,?,?,?)",param)
        conn.commit()

    #更新数据
    def update(self,conn,param):
        cu=conn.cursor()
        cu.execute("UPDATE userinfo SET Name = ? WHERE ? = ?",param)
        conn.commit()
