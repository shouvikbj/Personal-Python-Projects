from flask import Flask,flash,render_template,redirect,request
import csv

file = open("login.csv","a")
writer = csv.writer(file)
file2 = open("login.csv","r")
reader = csv.reader(file2)

app = Flask(__name__)

@app.route("/")
def login3():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/reguser",methods = ["POST"])
def reguser():
    uname = request.form.get("uname")
    password = request.form.get("pass")
    store = uname+password
    test = False
    for line in reader:
        if(log == line[0]):
            test = True    

    if(test):
        return  render_template("tryagain.html")
    else:
        writer.writerow((store,''))
        file.close()
        return render_template("login.html")

@app.route("/login",methods = ["POST"])
def login1():
    name = request.form.get("uname")
    password = request.form.get("pass")
    log = name+password
    test = False
    for line in reader:
        if(log == line[0]):
            test = True

    if(test):
        return render_template("success.html")
    else:
        return render_template("failure.html")

@app.route("/tryagain")
def tryagain():
    return render_template("tryagain.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
