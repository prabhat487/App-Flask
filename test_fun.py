from flask import Flask,request,jsonify
import mysql.connector as conn
app=Flask(__name__)
@app.route('/test')
def test_func():
    name=request.args.get('name')
    email=request.args.get('email')
    return "i am {} and my email id is : {}".format(name,email)

@app.route('/data')
def get_data_from():
    db=request.args.get('db')
    tn=request.args.get('tn')
    try:
        mydb=conn.connect(host='localhost',user='root',passwd='mysql123',database=db)
        cur=mydb.cursor()
        cur.execute(f"select * from {tn}")
        res=cur.fetchall()
        mydb.commit()
    except Exception as e:
        return jsonify(str(e))
    finally:
        mydb.close()
    return jsonify(str(res))

if __name__=='__main__':
    app.run()