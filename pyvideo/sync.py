import requests

BASE_URL = "http://pyvideo.org/api/v2/video?page={}&ordering=-added"


def sync():
    videos = []
    i = 1
    resp = requests.get(BASE_URL.format(i))
    while resp.status_code == 200:
        resp = resp.json()
        for entry in resp["results"]:
            videos.append(entry)
        i += 1
        print("Getting page number {}".format(i))
        resp = requests.get(BASE_URL.format(i))

    return videos
