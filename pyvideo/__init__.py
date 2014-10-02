from flask import Flask
from .utils import get_config
get_config()

from pymongo import MongoClient
import config

app = Flask(__name__)
db = MongoClient(config.mongo_url).pyvideo

from . import views
