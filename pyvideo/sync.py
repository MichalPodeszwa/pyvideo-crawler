import requests
from . import db
from pymongo import errors as pymongo_err
BASE_URL = "http://pyvideo.org/api/v2/video?page={}&ordering=-added"


def sync():
    i = 1
    should_reload = False
    resp = requests.get(BASE_URL.format(i))
    while resp.status_code == 200:
        resp = resp.json()
        for entry in resp["results"]:
            video = video_to_dict(entry)
            if video["url"]:
                try:
                    db.videos.insert(video)
                except pymongo_err.DuplicateKeyError:
                    return should_reload
                else:
                    should_reload = True
        i += 1
        print("Getting page number {}".format(i))
        resp = requests.get(BASE_URL.format(i))
        if i == 5:
            break
    return should_reload


def video_to_dict(video):
    return {
        "_id": video["id"],
        "title": video["title"],
        "conference": video["category"],
        "url": get_url(video),
        "embed": video["embed"],
        "added": video["added"].split("T")[0],
        "interested": True,
        "watched": False,
    }


def get_url(video):
    url = video["source_url"]
    if "youtube" in url:
        return url
    return None
