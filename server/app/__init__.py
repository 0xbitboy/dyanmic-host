import os
from flask import Flask, jsonify, g
from flask.json import JSONEncoder
import calendar
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from .decorators import json, no_cache, rate_limit

db = SQLAlchemy()

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                if obj.utcoffset() is not None:
                    obj = obj - obj.utcoffset()
                millis = int(
                    calendar.timegm(obj.timetuple()) * 1000 +
                    obj.microsecond / 1000
                )
                return millis
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)
    app.json_encoder = CustomJSONEncoder
    # apply configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    # initialize extensions
    db.init_app(app)

    # register blueprints
    from .api_v1 import api as api_blueprint
    from .public_v1 import public as public_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    app.register_blueprint(public_blueprint, url_prefix='/public/v1')

    # register an after request handler
    @app.after_request
    def after_request(rv):
        headers = getattr(g, 'headers', {})
        rv.headers.extend(headers)
        return rv


    return app
