from flask import Flask, request, jsonify
import json

app = Flask(__name__)

DS_Students = {}

@app.route('/', methods=['GET'])
def get_records():
    return jsonify(DS_Students)

@app.route('/', methods=['POST'])
def create_record():
    added = {}
    for k,v in request.args.items():
        if not k in DS_Students.keys():
            added[k] = v
            DS_Students[k] = v
    return jsonify({"added": added, "current": DS_Students})

@app.route('/', methods=['DELETE'])
def delete_record():
    deleted = {}
    for k,v in request.args.items():
        try:
            DS_Students.pop(k)
            deleted[k] = v
        except:
            continue
    return jsonify({"deleted": deleted, "current": DS_Students})
                
if __name__ == '__main__':
    app.run(debug=True)