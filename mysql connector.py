



import pymysql

try:
    con =pymysql.connect(host='localhost' ,user='root' ,password='12345678' ,db='farhan')
except:
    print('wrong')
try:
    can =con.cursor()
    quary ='SELECT * FROM farhan.data;'
    data =can.execute(quary)
except:
    print('this is a wrong')
result=can.fetchall()
for i in result:
    print(i)






































