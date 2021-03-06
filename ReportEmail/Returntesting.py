# coding=utf-8


class Returntesting():
    # @conn 数据库连接
    # @params 传入参数的元祖，例如：(产品名, 版本号)
    # 插入数据
    @classmethod
    def insert(cls, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO returntesting(product_id,return,is_finish) VALUES(?,?,?)", params)
        conn.commit()

    # 根据产品id和回归功能内容删除数据
    @classmethod
    def remove(cls, conn, params):
        cu = conn.cursor()
        cu.execute("DELETE FROM returntesting WHERE product_id = ? and return = ?", params)
        conn.commit()

    # 根据产品id和回归功能内容修改测试完成情况
    @classmethod
    def update(cls, conn, params):
        cu = conn.cursor()
        cu.execute("UPDATE returntesting SET is_finish = ? WHERE product_id = and return = ?", params)
        conn.conmmit()

    # 查询数据
    @classmethod
    def select(cls, conn, params):
        cu = conn.cursor()
        cu.execute("SELECT * FROM returntesting where product_id = ?", params)
        print(cu.fetchall())
