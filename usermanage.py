
def create_user(username, uid, email, password, display_name, school):
	user_info = UserInfo(username, uid, email, password, display_name, school)
	assert db.
	db.hset('users', username, json.dumps(user_info))



def register_user():
	