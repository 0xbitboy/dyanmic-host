from . import db

class User(db.model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

class AgentGroup(db.model):
    __tablename__ = 'agent_groups'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(64), unique=True)

class Agent(db.model):
    __tablename__ = 'agents'
    id = db.Column(db.Integer, primary_key=True)
    host_name = db.Column(db.String(128), unique=True)
    ip = db.Column(db.String(64), unique=True);
    group_id = db.Column(db.Integer, db.ForeignKey('agent_groups.id'))
