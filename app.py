from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        dob = request.form["dob"]
        course = request.form["course"]
        phone = request.form["phone"]
        email = request.form["email"]

        students.append({
            "name": name,
            "age": age,
            "dob": dob,
            "course": course,
            "phone": phone,
            "email": email
        })

        return redirect("/")

    return render_template("index.html", students=students)

@app.route("/delete/<int:index>")
def delete(index):
    students.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)