from app import db

class UserPermissionRecord(db.Model):
    username = db.Column(db.String(100))
    group_id = db.Column(db.Integer)

class GroupPermissionRecord(db.Model):
    group_id = db.Column(db.Integer)
    pid = db.Column(db.Integer)