import pymysql


conn = pymysql.connect(host='192.168.199.162', port=3306, user='root', password='lixiong6660')
conn.close()
