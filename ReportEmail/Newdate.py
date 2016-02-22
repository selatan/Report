#coding=utf-8


class newdate():


    # @conn 数据库连接
    # @params 传入参数的元祖，例如：(产品名, 版本号)
    # 插入数据
    def insert(self, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO newdate VALUES(?,?,?,?,?,?,?,?,?,?)", params)
        conn.commit()

    # 根据产品id和日期修改每日新增bug数
    def update_new_everyday(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET new_everyday = ? WHERE product_id = ? and date = ?",param)
        conn.conmmit()

     # 根据产品id和日期修改每日reopen bug数
    def update_reopen_everyday(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET reopen_everyday = ? WHERE product_id = ? and date = ?",param)
        conn.conmmit()

     # 根据产品id和日期修改每日修复bug数
    def update_resolved_everyday(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET resolved_everyday = ? WHERE product_id = ? and date = ?",param)
        conn.conmmit()

    # 根据产品id和日期修改每日new状态的bug数
    def update_new(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET new = ? WHERE product_id = ? and date = ?",param)
        conn.conmmit()

    # 根据产品id和日期修改in_progress状态的bug数
    def update_in_progress(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET in_progress = ? WHERE product_id = ? and date = ?",param)
        conn.conmmit()

    # 根据产品id和日期修改reopen状态的bug数
    def update_reopen(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET reopen = ? WHERE product_id = ? and date = ?",param)
        conn.conmmit()

    # 根据产品id和日期修改resolved状态的bug数
    def update_resolved(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET resolved = ? WHERE product_id = ? and date = ?",param)
        conn.conmmit()

    # 根据产品id和日期修改in_progress状态的bug数
    def update_closed(self,conn,param):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET closed = ? WHERE product_id = ? and date = ?",param)
        conn.conmmit()

     # 根据产品id和日期删除一条数据
    def remove(self, conn, params):
        cu = conn.cursor()
        cu.execute("DELETE FROM newdate WHERE product_id = ? and date = ?", params)
        conn.commit()


    # 查询数据
    def select(self,conn,param):
        cu = conn.cursor()
        cu.execute("SELECT * FROM newdate where product_id = ? and date = ?",param)
        print(cu.fetchall())