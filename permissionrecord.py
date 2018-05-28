from app import db

class UserPermissionRecord(db.Model):
    uid = db.Column(db.Integer)
    gid = db.Column(db.Integer)

class ProblemPermissionRecord(db.Model):
    gid = db.Column(db.Integer)
    pid = db.Column(db.Integer)