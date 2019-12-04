from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('Frontend.html')


@app.route("/produto/")
def produto():
    return render_template('Produto.html')


@app.route("/promocoes/")
def promocoes():
    return render_template('promocoes.html')


@app.route("/montapc/")
def montapc():
    return render_template('MonteSeuPC.html')


if __name__ == "__main__":
    app.run()
