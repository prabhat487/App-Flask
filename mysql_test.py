import mysql.connector as conn
from flask import Flask , request , jsonify
app=Flask(__name__)
mydb=conn.connect(host='localhost',user='root',passwd='mysql123')
#print(mydb.is_connected())
cursor=mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable(name varchar(30), number int)")
@app.route('/insert',methods=['GET','POST'])
def insert():
    if (request.method=='POST'):
        name=request.json['name']
        number=request.json['number']
        cursor.execute("insert into taskdb.tasktable values(%s,%s)",(name,number))
        mydb.commit()
        return jsonify(str('successfully inserted'))

@app.route('/fetch',methods=['GET','POST'])
def fetch():
    if request.method=='POST':
        query=request.json['query']
        cursor.execute(query)
        result=cursor.fetchall()
        return jsonify(str(result))
@app.route('/update',methods=['POST'])
def update():
    if request.method=='POST':
        get_name=request.json['name']
        cursor.execute("update taskdb.tasktable set number=number+500 where name=%s",(get_name,))
        mydb.commit()
        return jsonify((str('successfully updated')))
@app.route('/delete',methods=['POST'])
def delete():
    if request.method=='POST':
        del_name=request.json['name']
        cursor.execute("delete from taskdb.tasktable where name=%s",(del_name,))
        mydb.commit()
        return jsonify(str('successfuly deleted'))
@app.route('/fetch_data',methods=['POST','GET'])
def fetch_data():
    if request.method=='POST':
        cursor.execute("select * from taskdb.tasktable")
        l=[]
        for i in cursor.fetchall():
            l.append(i)
        return jsonify(str(l))
if __name__=='__main__':
    app.run()