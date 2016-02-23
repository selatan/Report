#coding=utf-8

import sqlite3

#cx = sqlite3.connect("E:/workspace/python/Report/db/myData.db")
cx = sqlite3.connect("/Users/a1/Desktop/ProjectReport/myData.db")
cu = cx.cursor()

# 创建表userinfo——表1
cu.execute('''CREATE TABLE "userinfo"(
         "username"  TEXT NOT NULL,
         "email"  TEXT NOT NULL,
         "pw"  TEXT NOT NULL,
         "email_list"  TEXT NOT NULL,
         "bugzilla_account"  TEXT NOT NULL,
         "bugzilla_pw"  TEXT NOT NULL,
          PRIMARY KEY ("username"))''')

#创建表userproduct——表2
cu.execute('''CREATE TABLE "userproduct" (
         "product_id"  INTEGER NOT NULL,
          "username"  TEXT NOT NULL,
          FOREIGN KEY ("product_id") REFERENCES "product" ("id"))''')

#创建表allproduct——表3
cu.execute('''CREATE TABLE "product" (
        "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "product_name"  TEXT NOT NULL,
        "version"  TEXT NOT NULL,
        "component"  TEXT NOT NULL,
         UNIQUE ("product_name", "version"))''')

#创建表newrequest——表4
cu.execute('''CREATE TABLE "newrequest" (
       "product_id"  INTEGER NOT NULL,
        "new_request"  TEXT NOT NULL,
        "is_testing"  INTEGER NOT NULL DEFAULT 0,
        "is_finish"  INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY ("product_id") REFERENCES "product" ("id"))''')

#创建表returntesting——表5
cu.execute('''CREATE TABLE "returntesting" (
         "product_id"  INTEGER NOT NULL,
         "returun"  INTEGER NOT NULL,
         "is_finish"  INTEGER NOT NULL DEFAULT 0,
          FOREIGN KEY ("product_id") REFERENCES "product" ("id"))''')

#创建表receiver——表6
cu.execute('''CREATE TABLE "receiver" (
         "product_id"  INTEGER NOT NULL,
          "receiver"  TEXT NOT NULL,
          "cc"  TEXT,
          "bcc"  TEXT,
          PRIMARY KEY ("product_id"),
          FOREIGN KEY ("product_id") REFERENCES "product" ("id"))''')

#创建表newdata——表7
cu.execute('''CREATE TABLE "newdate" (
         "product_id"  INTEGER NOT NULL,
          "date"  TEXT NOT NULL,
          "new_everyday"  TEXT,
          "reopen_everyday"  TEXT,
          "resolved_everyday"  TEXT,
          "new"  TEXT,
          "in_progress"  TEXT,
          "reopen"  TEXT,
           "resolved"  TEXT,
           "closed"  TEXT,
           FOREIGN KEY ("product_id") REFERENCES "product" ("id"),
           UNIQUE ("product_id", "date"))''')




