from flask import Flask,request, jsonify

app=Flask(__name__)

@app.route('/abc',methods=['GET','POST'])
def test1():
    if (request.method=='POST'):
        a=request.json['num1']
        b=request.json['num2']
        result=a+b
        return jsonify((result))

@app.route('/abc/pk',methods=['GET','POST'])
def menu():
    bal=0
    pin=1234
    if (request.method=='POST'):
       user_input=request.json['num']
       if user_input==pin:
         bal=bal+100
    return jsonify(str(bal))


if __name__=='__main__':
    app.run()