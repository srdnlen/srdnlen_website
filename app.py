from flask import Flask, render_template
from config import custom_settings, navigation, site

app = Flask(__name__)

@app.route("/")
def home():

    return render_template("index.html", custom=custom_settings, navigation=navigation, site=site, current_year=2024)

if __name__ == "__main__":
    app.run(debug=True)
