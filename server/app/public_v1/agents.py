from flask import request
from . import public
from .. import db
from ..models import Agent,AgentGroup
from ..decorators import json, paginate
from ..utils import random_str

'''
    Sync agent info
'''
@public.route('/agents/<string:id>', methods=['PUT','POST'])
@json
def update_agent(id):
     """update agent info."""
     form = request.form
     ip = form['ip']
     host_name = form['host_name']
     agent = Agent.query.get_or_404(id);
     agent.ip =ip;
     agent.host_name = host_name;
     agent.status = 1;
     db.session.commit();
     return {}     
