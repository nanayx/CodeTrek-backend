from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session, jsonify
import json
from utils.firebase_helper import *
from flask_cors import CORS

app=Flask(__name__,
    static_folder="static",
    static_url_path="/"
)
CORS(app)
app.secret_key="any string but secret"

@app.route("/",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/hello")
def hello():
    name=request.args.get("name","")
    session["username"]=name
    return "你好"+name

@app.route("/talk")
def talk():
    name=session["username"]
    return name+",nice to meet you"


@app.route("/getEXP")
def getEXPByID():
    player_id = request.args.get("id")
    exp = getEXPByIDFB(player_id)
    return jsonify({'exp':exp})


@app.route("/getLEVEL")
def getLEVELByID():
    user_email = request.args.get("email")
    level = getLEVELByEMFB(user_email)
    return jsonify({'level':level})

@app.route("/getRANK")
def getScoreRank():
    data = getUserScoreRank()
    return jsonify(data)

@app.route("/calculate",methods=["POST"])
def cal():
    #maxNum=request.args.get("max","")
    maxNum=request.form["max"]
    maxNum=int(maxNum)
    result=0
    for i in range(1,maxNum+1):
        result+=i
    return render_template("result.html", data=result)

@app.route("/show")
def show():
    name=request.args.get("n","")
    return "歡迎光臨"+name

@app.route("/page")
def page():
    return render_template("page.html")


app.run(port=3000, host='0.0.0.0', threaded=True)

