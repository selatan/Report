#coding=utf-8


class Receiver():


    # @conn 数据库连接
    # @params 传入参数的元祖，例如：(产品名, 版本号)
    # 插入数据
    def insert(self, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO receiver(product_id,receiver,cc,bcc) VALUES(?,?,?,?)", params)
        conn.commit()

    # 删除数据
    def remove(self,conn,params):
        cu = conn.cursor()
        cu.execute("DELETE FROM receiver WHERE  product_id = ?",params)
        conn.commit()

    # 根据产品id修改收件人\抄送人\密送人地址
    def update(self,conn,params):
        cu = conn.cursor()
        cu.execute("UPDATE receiver SET receiver = ? and cc = ? and bcc = ? WHERE product_id = ?",params)
        conn.conmmit()

    # 查询数据
    def select(self,conn,params):
        cu = conn.cursor()
        cu.execute("SELECT * FROM receiver where product_id = ?",params)
        print(cu.fetchall())