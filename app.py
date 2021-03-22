#
from flask import Flask, render_template,request


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home():
    return "<h1>Hello Brand and wonderful very New World!!</h1>"

@app.route("/add2number",methods=['GET','POST'])
def addtonumber():
    try:
        if request.method == "POST":
            val1 = request.form["val1"]
            val2 = request.form["val2"]
            val3 = int(val1) + int(val2)
            return render_template('index.html',value=val3)
        if request.method == "GET":
            return render_template('index.html')
        return render_template('index.html')
    except Exception as e:
        return f"Somthing Went Wrong!!, {e}"


# if __name__ == "__main__":
#     app.run()

if __name__ == "__main__":
    app.run(debug=True)
