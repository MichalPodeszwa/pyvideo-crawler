import requests
from . import db

BASE_URL = "http://pyvideo.org/api/v2/video?page={}&ordering=-added"


def sync():
    videos = []
    i = 1
    resp = requests.get(BASE_URL.format(i))
    while resp.status_code == 200:
        resp = resp.json()
        for entry in resp["results"]:
            video = video_to_dict(entry)
            db.videos.insert(video)
            videos.append(video)
        i += 1
        print("Getting page number {}".format(i))
        resp = requests.get(BASE_URL.format(i))
        if i == 5:
            break

    return videos


def video_to_dict(video):
    return {
        "_id": video["id"],
        "title": video["title"],
        "conference": video["category"],
        "url": get_url(video),
        "embed": video["embed"],
        "added": video["added"],
    }


def get_url(video):
    urls = [
        "source_url", "video_flv_url", "video_webm_url",
        "video_mp4_url", "video_ogv_url"
    ]
    for url in urls:
        if video[url]:
            return video[url]
