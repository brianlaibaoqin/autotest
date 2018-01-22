# -*- coding:utf-8 -*-
import pymysql
import os,sys
"""
class DBuser():
  #创建连接
    conn = pymysql.connect(host='192.168.0.126', port=3306, user='root', passwd='mysql@youngmaker@com@2017', db='youngmaker', charset='utf8')
    cur = conn.cursor()
    sql = 'DELETE from`onethink_ucenter_member` WHERE `username` = %r ' %user
    try:
        cur.execute(sql)
        #提交
        conn.commit()
        print("ok")
    except Exception as e:
        #错误回滚
        print(e)
        print("出错了")
        conn.rollback()
    finally:
        conn.close()
"""
aa = os.path.split(os.path.realpath(__file__))[0]

print(aa)
