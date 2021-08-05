# db1.py
import sqlite3

#연결객체 생성(일단은 메모리에 임시로 저장)
#con = sqlite3.connect(":memory:")
con = sqlite3.connect("c:\\work\\test.db")
#구문을 수행할 커서 객체를 생성
cur = con.cursor()
#데이터를 담을 테이블 생성
cur.execute("create table PhoneBook(name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values('derick','010-111');")
#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values(?,?);",(name, phoneNumber))
#다중의 레코드(데이터를 입력하는 경우)
datalist = (("tom","010-123"),("dsp","010-456"))
cur.executemany("insert into PhoneBook values(?,?);",(datalist))

#결과를 검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)