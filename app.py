from flask import Flask, render_template
from config import custom_settings, navigation, site
from datetime import datetime

def change_active_nav(nav:list, idx:int) -> list:
    for i, item in enumerate(nav):
        nav[i]['current'] = False
    
    nav[idx]['current'] = True
    return nav

app = Flask(__name__)

@app.route("/")
def home():

    posts = [{
        "class": "ciao",
        "url": "/ciao",
        "title": "Title",
        "primary_tag":{
            "url": "/ciao",
            "name": "ciao"
        },
        "date": datetime.now()
    },
    {
        "class": "ciao",
        "url": "/ciao",
        "title": "Title",
        "primary_tag":{
            "url": "/ciao",
            "name": "ciao"
        },
        "date": datetime.now()
    }]
    navigation = [
        {"slug": "home", "label": "Home", "url": "/", "current": False, "absolute": True},
        {"slug": "about", "label": "About", "url": "/about", "current": False, "absolute": True},
    ]
    navigation = change_active_nav(navigation, 0)

    return render_template("index.html", custom=custom_settings, navigation=navigation, site=site, current_year=2024, posts=posts)

@app.route("/about")
def about():
    navigation = [
        {"slug": "home", "label": "Home", "url": "/", "current": False, "absolute": True},
        {"slug": "about", "label": "About", "url": "/about", "current": False, "absolute": True},
    ]
    navigation = change_active_nav(navigation, 1)
    return render_template("about.html", custom=custom_settings, site=site, navigation=navigation, current_year=2024)

if __name__ == "__main__":
    app.run(debug=True)
