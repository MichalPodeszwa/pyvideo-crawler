from . import app
from .auth import requires_auth


@app.route("/")
def index():
    return "Hello world"


@app.before_request
@requires_auth
def require_auth():
    """This function is called only so that requires_auth is called"""
    pass
