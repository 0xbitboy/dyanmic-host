from flask import request,g
from . import api
from .. import db
from ..models import Agent,AgentGroup
from ..decorators import json, paginate
from ..utils import random_str
import datetime


@api.route('/agents/<string:id>', methods=['GET'])
@json
def get_agent(id):
    userId = g.user.id;
    print("userId",userId)
    return Agent.query.filter(Agent.id==id).filter(Agent.user_id == userId).one();

@api.route('/agents/<string:id>', methods=['PUT','POST'])
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

@api.route('/agents/key', methods=['GET'])
@json
def getAgentKey():
    """return a user's agent key to install."""
    userId = g.user.id;
    temp_agent = Agent.query.filter(Agent.user_id == userId).filter(Agent.status==-1).one_or_none()
    if temp_agent is None :
        now = datetime.datetime.now()
        agent = Agent(id=random_str(8),user_id=userId,create_time=now,update_time=now,status=-1)
        baseGroup =AgentGroup.query.filter(AgentGroup.user_id==agent.user_id).filter(AgentGroup.name=='all').one_or_none();
        if baseGroup is None:
            baseGroup = AgentGroup(name='all',user_id=agent.user_id,sid="%d@%s"%(agent.user_id,random_str(8)))
            db.session.add(baseGroup)
            agent.default_group_sid = baseGroup.sid
        db.session.add(agent)
        db.session.commit()
        return agent
    return temp_agent
        
