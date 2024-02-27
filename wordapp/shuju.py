import pymysql
def change(sql,isInsert=False):

    conn = pymysql.connect(
        user='root',  # The first four arguments is based on DB-API 2.0 recommendation.
        password="123456",
        host='localhost',
        database='nano',
        port=3306,
    )
    try:
        cursor = conn.cursor()
        result = cursor.execute(sql)
        conn.commit()
        if isInsert:
            new_id = cursor.lastrowid
            return new_id  # 返回增加的id
        else:
            return result
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def add(sql):
    return change(sql,isInsert=True)

def upd(sql):
    return change(sql)

def delete(sql):
    return change(sql)



