from flask import Flask,jsonify,request
from data import data 

app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data" : data,
        "status" : "success"
    }),200

@app.route("/star")
def star():
  name = request.args.get("Name")
  star_data = next(item for item in data if item["Name"] == name)
  return jsonify({
     "data":star_data,
     "status":"success"
  }),200

if __name__ == "__main__":
   app.run
