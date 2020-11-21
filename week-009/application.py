from flask import Flask, redirect, render_template, request
import csv
import math

app = Flask(__name__)

# Registered students
students = []

@app.route('/')
def index():
    name = request.args.get("name", "world")
    return render_template('index.html', name=name)

@app.route('/registrants')
def registrants():
    return render_template('registered.html', students=students)

@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    room = request.form.get("room")
    if not name or not room:
        return render_template('failure.html')
    file = open('registered.csv', 'a', newline='')
    writer = csv.writer(file)
    writer.writerow((request.form.get('name'), request.form.get('dorm')))
    file.close()
    students.append(f"{name} from {room}")
    return render_template("success.html")

@app.route("/registered")
def registered():
    with open("registered.csv", "r", newline='') as file:
        reader = csv.reader(file)
        students = list(reader)
    return render_template("registered.html", students=students)

    ##How to find a way to add a header row to the CSV. 
    #Then load the array of objects. Researchow to header to csv.
    #To load the data a list of objects.

#     https://docs.python.org/3/library/csv.html
# Mark Monday4:32 PM
# [ "John". "Doe" ]
# { firstName: "John", lastName: "Doe" }

@app.route('/sqrt/<num>')
def squared_root_num(num):
    num = str(math.sqrt(int(num)))
    return render_template("index.html")
    

@app.route('/user/<username>')
def message(username):
    return f"Hello {username}. Nice to meet you!"

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return result
    else:
        return f"this was a {request.method}"
