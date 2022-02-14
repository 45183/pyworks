import sqlite3

def getconn():
    conn = sqlite3.connect("c:/ncstest4/")
    return conn

def create_table():
    conn = getconn()
    cur = conn.cursor()
    sql = """
        CREATE TABLE member(
        memberId    char(5) PRIMARY KEY,
        passwd      char(10) NOT NULL,
        name        TEXT NOT NULL,
        gender      char(4)
        age         INTEGER
        )
    """
    cur.execute(sql)
    conn.commit()
    print("member 테이블 생성")
    conn.close()

def select_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "SELECT * FROM member"
    cur.execute(sql)
    rs = cur.fetchall()
    print(rs)
    conn.close()

def insert_member():
    conn = getconn()
    cur = conn.cursor()
    sql = "INSERT INTO member(memberId, passwd, name, gender, ager)" \
          "VALUES ('', '', '', '', )"
    cur.execute(sql)
    conn.commit()
    conn.close()