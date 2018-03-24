import pymysql.cursors

# connect
db = pymysql.connect(host="localhost",
                     user="yuq",
                     password="123456",
                     db="datascience",
                     charset='utf8',
                     cursorclass=pymysql.cursors.DictCursor)


try:

    with db.cursor() as cursor:
        # Read a single record
        sql = "SHOW TABLES"
        cursor.execute(sql, ())
        result = cursor.fetchall()
        print(result)
finally:
    db.close()
