import csv
import pymysql
import pandas as pd

db = pymysql.connect(user='root', passwd='1234', host='127.0.0.1',db='schedule_app',charset='utf8')
cursor = db.cursor(pymysql.cursors.DictCursor)
f =  open('courses.csv', 'r', encoding = 'utf-8')
r = csv.reader(f)
i = 0
for line in r :
    if i != 0 :
        sql = ("INSERT INTO lecture_list (CODE, LECTURE, PROF, LOCATION, START, END, DAY) VALUES ('%s','%s','%s','%s','%s','%s','%s')")%(line[0],line[1],line[2],line[3],line[4],line[5],line[6])
        cursor.execute(sql)
        db.commit()
    i = i + 1
f.close()

sql = "SELECT * FROM `lecture_list`;"
cursor.execute(sql)
result = cursor.fetchall()
result = pd.DataFrame(result)
print(result)
