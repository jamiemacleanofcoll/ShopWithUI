from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates")

@app.route("/")
def helloworld():
    return render_template("homepage.html")

@app.route("/test")
def show_test():
    return "This is the test page"

app.run(debug=True)
