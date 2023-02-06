from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def my_route():
    """Read all the cookies."""
    return render_template("gif_control.html")
