import os
import config


def get_config():
    config.mongo_url = os.environ.get("MONGO_URI", None)
    config.username = os.environ.get("USERNAME", "admin")
    config.password = os.environ.get("PASSWORD", "secret")
