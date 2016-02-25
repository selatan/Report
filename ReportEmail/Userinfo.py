#coding=utf-8



class Userinfo():

    #插入数据
    def insert(self,conn,params):
        cu=conn.cursor()
        cu.execute("INSERT INTO userinfo(username,email,pw,email_list,bugzilla_account,bugzilla_pw) VALUES(?,?,?,?,?,?)",params)
        conn.commit()

    #更新数据
    def update(self,conn,params):
        cu=conn.cursor()
        cu.execute("UPDATE userinfo SET pw = ? and email_list = ? and bugzilla_pw = ? WHERE username = ?",params)
        conn.commit()

     #查询数据
    def select(self,conn,params):
        cu = conn.cursor()
        cu.execute("SELECT * FROM userinfo where username = ?",params)
        #print(cu.fetchall())  #从结果中取出所有数据
        return cu.fetchall()