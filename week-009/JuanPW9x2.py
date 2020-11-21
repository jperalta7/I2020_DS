from flask import Flask, request, render_template
import math, csv

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

@app.route('/sqrt/<number>')
def sqr_mum(number):
    return f"{round(math.sqrt(int(number)),2)}"

@app.route('/user/<username>')
def message(username):
    return f"Hello {username}. Welcome to our Python Website!"

@app.route('/register', methods=["POST"])
def register():
    name = request.form.get("name")
    track = request.form.get("track")
    if not name or not track:
        return render_template('failure.html')
    file = open('registered.csv', 'a', newline='')
    writer = csv.writer(file)
    writer.writerow((request.form.get('name'), request.form.get('track')))
    file.close()
    students.append(f"{name} from {track}")
    return render_template("success.html")


@app.route("/registered")
def registered():
    with open("registered.csv", "r", newline='') as file:
        reader = csv.reader(file)
        students = list(reader)
    return render_template("registered.html", students=students)