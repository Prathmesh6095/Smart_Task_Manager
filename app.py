from flask import Flask, render_template, request, redirect
import sqlite3
import joblib

app = Flask(__name__)

model = joblib.load("priority_model.pkl ")
vectorizer = joblib.load("vectorizer.pkl")


def predict_priority(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)
    return prediction[0]


@app.route("/")
def index():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    conn.close()

    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["GET","POST"])
def add_task():

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        deadline = request.form["deadline"]

        priority = predict_priority(description)

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
        "INSERT INTO tasks(title,description,deadline,priority) VALUES(?,?,?,?)",
        (title,description,deadline,priority)
        )

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_task.html")


if __name__ == "__main__":
    app.run(debug=True)