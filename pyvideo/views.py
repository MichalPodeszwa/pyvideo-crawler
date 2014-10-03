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


@app.route("/get_embed/<int:video_id>")
def get_embed(video_id):
    embed = db.videos.find_one({"_id": video_id})["embed"]
    return render_template(
        "show_video.html", embed=embed, video_id=video_id)


@app.before_request
@requires_auth
def require_auth():
    """This function is called only so that requires_auth is called"""
    pass
