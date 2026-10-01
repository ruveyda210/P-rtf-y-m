from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        print("İsim:", name)
        print("E-posta:", email)
        print("Mesaj:", message)

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)