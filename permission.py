from app import db
from permissionrecord import UserPermissionRecord, ProblemPermissionRecord

def check_problem_permission(uid, pid):
    user_groups = UserPermissionRecord.query.filter_by(uid=uid)
    problem_groups = ProblemPermissionRecord.query.filter_by(pid=pid)

    common_groups = user_groups.intersect(problem_groups)
    