# 도서 db 만들기

import sqlite3 as sql

def getconn():
    # 데이터 베이스 생성 및 접속
    conn = sql.connect("./book.db")
    return conn

def create_table():
    # 테이블 생성
    con = getconn()
    cursor = con.cursor()
    sql = """
        CREATE TABLE book(
            book_no integer PRIMARY KEY AUTOINCREMENT,
            title   text NOT NULL,
            publisher   text NOT NULL,
            page    integer        
        )
    """
    # AUTOINCREMENT : 자동으로 숫자 올라감
    cursor.execute(sql)
    con.commit()
    con.close()

def insert_book():
    # 도서 추가
    con = getconn()
    cursor = con.cursor()
    sql = "INSERT INTO book(title, publisher, page) VALUES (?, ?, ?)"
    # book_no는 자동이므로 입력x
    cursor.execute(sql, ("점프 투 파이썬", '박응용', 350))
    con.commit()
    con.close()

def select_book():
    # 전체 도서 검색
    con = getconn()
    cursor = con.cursor()
    sql = "SELECT * FROM book"
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    for i in rs:
        print(i)
    con.commit()
    con.close()

def select_one():
    # 특정 도서 검색
    con = getconn()
    cursor = con.cursor()
    sql = "SELECT * FROM book WHERE book_no = ?"
    cursor.execute(sql, (3, ))
    # 책 정보 가져오기
    rs = cursor.fetchone()
    print(rs)
    con.close()
    
def update_book():
    # 도서 정보 수정
    con = getconn()
    cursor = con.cursor()
    sql = "UPDATE book SET page = ? WHERE book_no = ?"
    cursor.execute(sql, (400, 3))
    con.commit()
    con.close()

def delete_book():
    # 도서 삭제
    con = getconn()
    cursor = con.cursor()
    sql = "DELETE FROM book WHERE book_no = ?"
    cursor.execute(sql, (1, ))
    con.commit()
    con.close()

if __name__ == "__main__":
    # conn = getconn()
    # print("연결", conn)
    # create_table()
    # insert_book()
    select_book()
    # select_one()
    # update_book()
    # delete_book()