from common import db

class UserPermissionRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer)
    gid = db.Column(db.Integer)

class ProblemPermissionRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gid = db.Column(db.Integer)
    pid = db.Column(db.Integer)