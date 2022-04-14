

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="players", port=3306)

cur = conn.cursor()

query = "update player set plyName = 'Pusarla Venkata Sindhu' where plyid = 'PLY525'"

cur.execute(query)

conn.commit()

conn.close()

"""
delete query

delete from player where plyid = '32234'

"""