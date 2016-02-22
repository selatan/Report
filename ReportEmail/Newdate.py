#coding=utf-8


class newdate():


    # @conn 数据库连接
    # @params 传入参数的元祖，例如：(产品名, 版本号)
    # 插入数据
    def insert(self, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO newdate VALUES(?,?,?,?,?)", params)
        conn.commit()

    # 修改数据
    def update(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET ? = ? WHERE ? = ?",param)
        conn.conmmit()

    # 查询数据
    def select(self,conn,param):
        cu = conn.cursor()
        cu.execute("SELECT * FROM newdate",param)
        print(cu.fetchall())