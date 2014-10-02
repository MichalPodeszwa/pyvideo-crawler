from flask import render_template, jsonify

from . import app, db
from .auth import requires_auth
from .sync import sync


@app.route("/")
def index():
    videos = list(db.videos.find())
    return render_template("index.html", videos=videos)


@app.route("/sync")
def start_sync():
    return jsonify(msg="success", reload=sync())


@app.before_request
@requires_auth
def require_auth():
    """This function is called only so that requires_auth is called"""
    pass
