from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            result = a + b
        except:
            result = "Error: Invalid input"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
