#coding=utf-8


class Newdate():


    # @conn 数据库连接
    # @params 传入参数的元祖，例如：(产品名, 版本号)
    # 插入数据
    @classmethod
    def insert(cls, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO newdate(product_id,date,new_everyday,reopen_everyday,resolved_everyday,new,in_progress,reopen,resolved,closed) "
                   "VALUES(?,?,?,?,?,?,?,?,?,?)", params)
        conn.commit()

    #新增一条数据，若该product_id和date已经存在则更新数据
    @classmethod
    def insertOrUpdate(cls, conn, params):
        cu = conn.cursor()
        data = cls.select(conn, (params[0], params[1]))
        if (data == None) :
            cls.insert(conn,params)
        else :
            cls.update_all(conn,params)
        conn.commit()

    # 根据产品id和日期修改所有数据
    @classmethod
    def update_all(cls,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET new_everyday = ?,reopen_everyday=?,resolved_everyday=?,new=?,in_progress=?,"
                   "reopen=?,resolved=?,closed=? WHERE product_id = ? and date = ?",params)
        conn.conmmit()


    # 根据产品id和日期修改每日新增bug数
    @classmethod
    def update_new_everyday(cls,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET new_everyday = ? WHERE product_id = ? and date = ?",params)
        conn.conmmit()

     # 根据产品id和日期修改每日reopen bug数
    @classmethod
    def update_reopen_everyday(cls,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET reopen_everyday = ? WHERE product_id = ? and date = ?",params)
        conn.conmmit()

     # 根据产品id和日期修改每日修复bug数
    @classmethod
    def update_resolved_everyday(self,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET resolved_everyday = ? WHERE product_id = ? and date = ?",params)
        conn.conmmit()

    # 根据产品id和日期修改每日new状态的bug数
    def update_new(cls,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET new = ? WHERE product_id = ? and date = ?",params)
        conn.conmmit()

    # 根据产品id和日期修改in_progress状态的bug数
    @classmethod
    def update_in_progress(cls,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET in_progress = ? WHERE product_id = ? and date = ?",params)
        conn.conmmit()

    # 根据产品id和日期修改reopen状态的bug数
    @classmethod
    def update_reopen(cls,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET reopen = ? WHERE product_id = ? and date = ?",params)
        conn.conmmit()

    # 根据产品id和日期修改resolved状态的bug数
    @classmethod
    def update_resolved(cls,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET resolved = ? WHERE product_id = ? and date = ?",params)
        conn.conmmit()

    # 根据产品id和日期修改in_progress状态的bug数
    @classmethod
    def update_closed(cls,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE newdate SET closed = ? WHERE product_id = ? and date = ?",params)
        conn.conmmit()

     # 根据产品id和日期删除一条数据
    @classmethod
    def remove(cls, conn, params):
        cu = conn.cursor()
        cu.execute("DELETE FROM newdate WHERE product_id = ? and date = ?", params)
        conn.commit()

    # 查询数据
    @classmethod
    def select(cls,conn,params):
        cu = conn.cursor()
        cu.execute("SELECT * FROM newdate where product_id = ? and date = ?",params)
        print(cu.fetchall())