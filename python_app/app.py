from flask import Flask, render_template, redirect
from datetime import datetime
import json
import configparser 
from ghost_apis import get_posts, get_posts_by_id

def change_active_nav(nav:list, idx:int) -> list:
    for i, item in enumerate(nav):
        nav[i]['current'] = False
    
    nav[idx]['current'] = True
    return nav

app = Flask(__name__, static_folder='static')
config = configparser.ConfigParser()
config.read('config.ini')
ghost_api = config['Ghost']['admin_url']
api_key = config["Ghost"]['key']
site = {
    "color_scheme": config['site']['color_scheme'],
    "darkmode_accent_color": config['site']['darkmode_accent_color'],
    "logo": config['site']['logo'],
    "url": config['site']['url']
}
limit = int(config['post']['limit'])

@app.route("/")
def home():

    navigation = json.loads(config['site']['navigation'])
    navigation = change_active_nav(navigation, 0)

    posts, meta = get_posts(ghost_api, api_key, limit)
    return render_template("index.html", navigation=navigation, site=site, current_year=2024, posts=posts, meta=meta, 
                           page_url_next=f"/pages/{meta['pagination']['next']}", 
                           page_url_prev=f"/pages/{meta['pagination']['prev']}")

@app.route("/pages/<int:num>")
def pages(num):

    navigation = json.loads(config['site']['navigation'])
    navigation = change_active_nav(navigation, 0)

    posts, meta = get_posts(ghost_api, api_key, limit, page=num)
    if meta['pagination']['prev'] == 1:
        return render_template("index.html", navigation=navigation, site=site, current_year=2024, posts=posts, meta=meta, 
                           page_url_next=f"/pages/{meta['pagination']['next']}",
                           page_url_prev=f'/')
    return render_template("index.html", navigation=navigation, site=site, current_year=2024, posts=posts, meta=meta, 
                           page_url_next=f"/pages/{meta['pagination']['next']}",
                           page_url_prev=f"/pages/{meta['pagination']['prev']}")

@app.route("/posts/<id>")
def post(id):

    navigation = json.loads(config['site']['navigation'])
    post = get_posts_by_id(ghost_api, api_key, id)
    print(post)
    return render_template("post.html", navigation=navigation, site=site, current_year=2024, post=post)

@app.route("/about")
def about():

    navigation = json.loads(config['site']['navigation'])
    navigation = change_active_nav(navigation, 1)   
    with open('members.json', 'r') as fp:
        members = json.load(fp)
    num = {cat: len(i) for cat, i in members.items()}

    return render_template("about.html", site=site, navigation=navigation, current_year=2024, members=members, num=num)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
