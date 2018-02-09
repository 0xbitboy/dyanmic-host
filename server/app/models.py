from datetime import datetime
from dateutil import parser as datetime_parser
from dateutil.tz import tzutc
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import url_for, current_app
from . import db
from .exceptions import ValidationError
from .utils import split_url
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, ForeignKey


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    def export_data(self):
        return {
            'id': self.id,
            'username': self.username
        }

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

class AgentGroup(db.Model):
    __tablename__ = 'agent_groups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    name = db.Column(db.String(64), unique=True)
    sid = db.Column(db.String(18),unique=True)

class Agent(db.Model):
    __tablename__ = 'agents'
    id = db.Column(db.String(8), primary_key=True)
    host_name = db.Column(db.String(128))
    ip = db.Column(db.String(64))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    remark = db.Column(db.String(256))
    status = db.Column(db.Integer) #1,0
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    __table_args__ = (
        UniqueConstraint('user_id', 'host_name', name='idx_qn_user_id_host_name') , # 联合唯一索引,name索引的名字
    )

    def export_data(self):
            return {
            'id': self.id,
            'host_name': self.host_name,
            'ip':self.ip,
            'remark':self.remark,
            'status':self.status,
            'create_time':self.create_time,
            'update_time':self.update_time
        }
