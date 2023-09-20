from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/calci",methods=["GET","POST"])
def math():
    if request.method=="POST":
        a=float(request.form["A"])
        b=float(request.form["B"])
        c='Addition:- ',a+b,'Subtraction:- ',a-b,'Multiplication:- ',a*b,'Division:- ',a/b
        return render_template("index.html", result=c)
    else:
        return render_template("index.html")
if __name__ == '__main__':
    app.run(port=5000,debug=True)