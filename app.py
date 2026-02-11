from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("students.db")

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        marks = int(request.form["marks"])
        result = "Pass" if marks >= 40 else "Fail"

        cur.execute(
            "INSERT INTO students (name, marks, result) VALUES (?, ?, ?)",
            (name, marks, result)
        )
        conn.commit()
        return redirect("/")

    cur.execute("SELECT name, marks, result FROM students")
    data = cur.fetchall()

    cur.execute("SELECT AVG(marks) FROM students")
    avg = cur.fetchone()[0]

    cur.execute("SELECT name, MAX(marks) FROM students")
    topper = cur.fetchone()

    conn.close()

    return render_template("index.html", data=data, avg=avg, topper=topper)

if __name__ == "__main__":
    app.run(debug=True)
