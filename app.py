from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
    
@app.route("/greeting")
def greeting():
    return """
    
    <h1>안녕!!!</h1>
    <ul>
        <li>한식</li>
        <li>중식</li>
        <li>양식</li>
        <li>선택시</li>
        <li>일식</li>
        <li>투움바파스타</li>
    
    
    
    </ul>
    
    
    
    """
    
@app.route("/index")
def index():
    return render_template("index.html")
    
@app.route("/lunch")
def lunch():
    menus = ["짜장면", "투움바 파스타", "김치찜", "굴국밥", "만두라면"]
    pick = random.choice(menus)
    return render_template("lunch.html", one_pick = pick)
    
@app.route("/lotto")
def lotto():
    lo_pick = random.sample(range(1,46),6)
    return render_template("lotto.html", lotto_pick = lo_pick)
    
@app.route("/student/<string:name>")
def studen(name):
    return render_template("student.html", name = name)
    
    
@app.route("/cube/<int:num>")
def cube(num):
    return  render_template("cube.html", num = num)
    
@app.route("/naver")
def naver():
    return render_template("naver.html")
    
@app.route("/google")
def google():
    return render_template("google.html")
    
    

    
if __name__ =="__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    
    
    
