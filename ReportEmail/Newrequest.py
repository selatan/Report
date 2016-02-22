# coding=utf-8


class Newrequest():
    # @conn 数据库连接
    # @params 传入参数的元祖，例如：(产品名, 版本号)
    # 插入数据
    def insert(self, conn, params):
        cu = conn.cursor()
        cu.execute("INSERT INTO newrequest VALUES(?,?,?,?)", params)
        conn.commit()

    # 根据产品id和新需求删除一条数据
    def remove(self, conn, params):
        cu = conn.cursor()
        cu.execute("DELETE FROM newrequest WHERE product_id = ? and new_request = ?", params)
        conn.commit()

    # 根据产品id修改新需求
    def update_new_request(self, conn, param):
        cu = conn.cursor()
        cu.execute("UPDATE newrequest SET new_request = ? WHERE product_id = ?", param)
        conn.conmmit()

    # 根据产品id修改提测情况(0表示未提测,1表示已提测,默认值为0)
    def update_is_testing(self, conn, param):
        cu = conn.cursor()
        cu.execute("UPDATE newrequest SET is_testing = ? WHERE product_id = ?", param)
        conn.conmmit()

    # 根据产品id修改测试完成情况(0~100,默认值为0)
    def update_is_finish(self, conn, param):
        cu = conn.cursor()
        cu.execute("UPDATE newrequest SET is_finish = ? WHERE product_id = ? and is_testing = 1", param)
        conn.conmmit()

    # 查询数据
    def select(self, conn, param):
        cu = conn.cursor()
        cu.execute("SELECT * FROM newrequest where product_id = ?", param)
        print(cu.fetchall())
