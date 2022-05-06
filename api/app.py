from flask import Flask, jsonify, request #import objects from the Flask model
import json


app = Flask(__name__)  # define app using Flask

with open("data/project.json") as f:
    data = json.load(f)

# print(data)

##########
# GET REQUESTS
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})

@app.route('/project_all/', methods = ['GET'])
def returnAll():
    '''
    [{"budget":12000,"description":"Realtime Face Recogniton","id":1,"name":"RTF","user_id":4},{"budget":80000,"description":"Smart Watch Tracker","id":2,"name":"SWT","user_id":1},{"budget":11000,"description":"Upgrade Legacy System","id":3,"name":"ULS","user_id":2}]
    '''
    
    for p in data:
        projects = {p["description"] for p in data }
        # projects = [p["description"] for p in data ]
        # project_name = [p["name"] for p in data ]

    return(jsonify({projects}))




if __name__ == '__main__':
    app.run(debug = True, port = 8000)  # run app on port 8000 in debug mode
