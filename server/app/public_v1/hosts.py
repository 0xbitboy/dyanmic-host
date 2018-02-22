from flask import request,Response
from . import public
from .. import db
from ..models import Agent,AgentGroup
from ..decorators import json, paginate


@public.route('/hosts/<string:group_sid>', methods=['GET'])
@json
def getHosts(group_sid):
    agent_group = AgentGroup.query.filter(AgentGroup.sid==group_sid).one_or_none()
    if agent_group is None:
        return {},200,{"message":"Cant not find agent group which sid ="+group_sid}
    agents = Agent.query.filter(Agent.default_group_sid==group_sid).filter(Agent.status==1).all()
    return agents

    
@public.route('/hosts/<string:group_sid>/hostfile', methods=['GET'])
def getHostfle(group_sid):
    hostsText = ""
    agent_group = AgentGroup.query.filter(AgentGroup.sid==group_sid).one_or_none()
    if agent_group is not None:
         agents = Agent.query.filter(Agent.default_group_sid==group_sid).filter(Agent.status==1).all()
         for agent in agents:
             updateTimeStr = agent.update_time.strftime("%Y-%m-%d %H:%M:%S")
             hostsText += ("#agent_id=%s,update_time=%s,%s \n%s %s\n"%(agent.id,updateTimeStr,agent.remark,agent.ip,agent.host_name))
    response = Response(hostsText,mimetype="text/html")
    return response


