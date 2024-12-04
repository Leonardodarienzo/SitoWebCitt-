from flask import Flask, render_template

app = Flask(__name__)

# Rotte principali
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/servizi.html")
def servizi():
    return render_template("servizi.html")

@app.route("/documenti.html")
def documenti():
    return render_template("documenti.html")

@app.route("/tributi.html")
def tributi():
    return render_template("tributi.html")

@app.route("/anagrafe.html")
def anagrafe():
    return render_template("anagrafe.html")

@app.route("/turismo.html")
def turismo():
    return render_template("turismo.html")

@app.route("/notizie.html")
def notizie():
    return render_template("notizie.html")

@app.route("/attrazioni.html")
def attrazioni():
    return render_template("attrazioni.html")

@app.route("/storia.html")
def storia():
    return render_template("storia.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
