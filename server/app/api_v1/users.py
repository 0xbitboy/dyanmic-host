from flask import request
from . import api
from .. import db
from ..models import User
from ..decorators import json, paginate


@api.route('/users/<int:id>', methods=['GET'])
@json
def get_user(id):
    return User.query.get_or_404(id)