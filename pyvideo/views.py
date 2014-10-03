from flask import render_template, jsonify, request
from . import app, db
from .auth import requires_auth
from .sync import sync
import json

@app.route("/")
def index():
    videos = list(db.videos.find())
    return render_template("index.html", videos=videos)


@app.route("/sync")
def start_sync():
    return jsonify(msg="success", reload=sync())


@app.route("/get_embed/<int:video_id>")
def get_embed(video_id):
    video = db.videos.find_one({"_id": video_id})
    return render_template(
        "show_video.html", video=video)


def get_args():
    video_id = request.args.get("id", None)
    field = request.args.get("field", None)
    if not video_id or not field:
        return (None, None)
    return (video_id, field)


@app.route("/change_state")
def change_state():
    video_id = int(request.args.get("id", 0))
    field = request.args.get("field", None)
    video = db.videos.find_one({"_id": video_id})

    if field == "watched":
        db.videos.update(
            {"_id": video_id},
            {"$set": {"watched": not video["watched"]}}
        )
        new_msg = not video["watched"]

    elif field == "interest":
        db.videos.update(
            {"_id": video_id},
            {"$set": {"interested": not video["interested"]}}
        )
        new_msg = not video["interested"]

    return jsonify(msg="success", new=new_msg)


@app.before_request
@requires_auth
def require_auth():
    """This function is called only so that requires_auth is called"""
    pass
