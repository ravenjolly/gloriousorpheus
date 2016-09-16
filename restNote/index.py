from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime
import json

client = MongoClient()
db = client.notez
col = db.notes


app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'sup'



@app.route('/notes/<user>', methods=['POST','GET'])
def new_item(user):
        if request.method == "POST":
                content = request.get_json(silent=True)
                result = col.insert_one(content)
                return "inserted"
        if request.method == 'GET':
                w = col.find_one({"name":user},{"_id":0})
                return json.dumps(w)
                
        


@app.route('/notes/<id>', methods=['GET'])
def gather_notes(id):
        
        return 'ima note'

        

if __name__ == '__main__':
	app.run(debug=True,port=80,host='0.0.0.0')

