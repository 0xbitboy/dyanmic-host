from flask import request
from . import api
from .. import db
from ..models import Agent,AgentGroup
from ..decorators import json, paginate


@api.route('/hosts/<string:group_sid>', methods=['GET'])
@json
def getAllHosts(group_sid):
    agent_group = AgentGroup.query.filter(AgentGroup.sid=group_sid).one_or_none();
    if agent_group is None:
        return {},200,{message:"Cant not find agent group which sid ="+group_sid}
    return {}
    


