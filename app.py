from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/om_oss")
def om_oss():
    return render_template("om_oss.html")

@app.route("/bestilling", methods=["GET", "POST"])
def bestilling():
    produkter = ['Pizza', 'Burger', 'Burrito','Den fjerde maten']
    storrlser = ['Liten','Middels','Stor']
    if request.method == "POST":
        navn = request.form["navn"]
        produkt = request.form["produkt"]
        storrelse = request.form["storrelse"]
        antall = request.form["antall"]
        kommentar = request.form.get("kommentar", "")
        return render_template("bekreftelse.html",navn=navn,produkt=produkt,storrelse=storrelse,antall=antall,kommentar=kommentar)
    return render_template("bestilling.html",produkter=produkter,storrlser=storrlser)

if __name__ == "__main__":
    app.run(debug=True)