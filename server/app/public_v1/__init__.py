from flask import Blueprint
from ..auth import auth_token
from ..decorators import etag, rate_limit

public = Blueprint('public', __name__)

@public.before_request
@rate_limit(limit=20, period=15)
def before_request():
    pass


@public.after_request
@etag
def after_request(rv):
    """Generate an ETag header for all routes in this blueprint."""
    return rv


from . import hosts,agents,errors