import pymongo
from flask import Flask,request,jsonify
app=Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://prabhat:mongodb123@cluster0.iean9di.mongodb.net/?retryWrites=true&w=majority")
db = client.test
database= client['taskdb']
collection=database['taskcollection']

@app.route('/insert',methods=['POST'])
def insert_mongo():
    if request.method=='POST':
        name=request.json['name']
        number=request.json['number']
        collection.insert_one({name:number})
        return jsonify(str('successfully inserted'))

@app.route('/fetch',methods=['POST'])
def fetch():
    if request.method=='POST':
        l=[]
        for i in collection.find({},{'_id':0}):
            l.append(i)
        return jsonify(str(l))
@app.route('/update',methods=['POST'])
def update():
    if request.method=='POST':
        get_name=request.json['name']
        get_number=request.json['number']
        nw_no=request.json['nw_no']
        collection.update_one({get_name:get_number},{'$set':{get_name:nw_no}})
        return jsonify((str('updated successfully')))

if __name__=='__main__':
    app.run()