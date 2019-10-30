from flask import Flask, render_template

app = Flask(__name__)


@app.route("/MonteSeuPC/")
def montapc():
    return render_template("MonteSeuPC.html")

if __name__ == "__main__":
    app.run()
