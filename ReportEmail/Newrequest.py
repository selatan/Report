#coding=utf-8


class Newrequest():


    # @conn 数据库连接
    # @params 传入参数的元祖，例如：(产品名, 版本号)
    # 插入数据
    def insert(self, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO newrequest VALUES(?,?,?,?,?)", params)
        conn.commit()

    # 删除数据
    def remove(self,conn,params):
        cu = conn.cursor()
        cu.execute("DELETE FROM newrequest WHERE ? = ? and ? = ?",params)
        conn.commit()

    # 修改数据
    def update(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newrequest SET ? = ? WHERE ? = ?",param)
        conn.conmmit()

    # 查询数据
    def select(self,conn,param):
        cu = conn.cursor()
        cu.execute("SELECT * FROM newrequest",param)
        print(cu.fetchall())