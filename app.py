from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("students.db")


@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db()
    cur = conn.cursor()

    # ADD STUDENT
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

    # SEARCH
    search_query = request.args.get("search")

    if search_query:
        cur.execute(
            "SELECT id, name, marks, result FROM students WHERE name LIKE ?",
            ("%" + search_query + "%",)
        )
    else:
        cur.execute("SELECT id, name, marks, result FROM students")

    data = cur.fetchall()

    # AVERAGE
    cur.execute("SELECT AVG(marks) FROM students")
    avg = cur.fetchone()[0]

    # TOPPER
    cur.execute("SELECT name, MAX(marks) FROM students")
    topper = cur.fetchone()

    conn.close()

    return render_template("index.html", data=data, avg=avg, topper=topper)


@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()
    cur = conn.cursor()

    if request.method == "POST":
        name = request.form["name"]
        marks = int(request.form["marks"])
        result = "Pass" if marks >= 40 else "Fail"

        cur.execute(
            "UPDATE students SET name=?, marks=?, result=? WHERE id=?",
            (name, marks, result, id)
        )
        conn.commit()
        conn.close()
        return redirect("/")

    cur.execute("SELECT name, marks FROM students WHERE id=?", (id,))
    student = cur.fetchone()
    conn.close()

    return render_template("edit.html", student=student)


if __name__ == "__main__":
    app.run(debug=True)
