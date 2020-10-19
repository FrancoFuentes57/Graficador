from flask import Flask,jsonify,request,json
from pulp import *

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def index():
    return {
        'name':'Hello World'
    }

@app.route('/api/data',methods=['POST'])
def create():
    request_data = json.loads(request.data)
    print(request_data)
    maxmin = request_data['data']['maxmin']
    xObj = request_data['data']['xObj']
    yObj = request_data['data']['yObj']
    todas = request_data['data']['names']

    for x in range(len(todas)):
        print(todas[x]['valorX'], todas[x]['valorY'],todas[x]['igualador'],todas[x]['resultado'])

    
    

    return json.dumps(todas)

    

if __name__ == '__main__':
    app.run(debug=True) 