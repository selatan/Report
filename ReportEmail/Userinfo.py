#coding=utf-8



class Userinfo():

    #插入数据
    def insert(self,conn,param):
        cu=conn.cursor()
        cu.execute("INSERT INTO userinfo(username,email,pw,email_list,bugzilla_account,bugzilla_pw) VALUES(?,?,?,?,?,?)",param)
        conn.commit()

    #更新数据
    def update(self,conn,param):
        cu=conn.cursor()
        cu.execute("UPDATE userinfo SET pw = ? and email_list = ? and bugzilla_pw = ? WHERE username = ?",param)
        conn.commit()
