# Hantering av registrering och inloggning
from db.database import add_user, get_user_by_email, delete_user

def register_user(name, email, password):
    if get_user_by_email(email):
        return False
    else:
        add_user(name,email,password)
	return True

def remove_user(email, userid):
    if get_user_by_email(email):
        delete_user(userid)
        return True
    else:
        return False

def user_login(email,password):
    user = get_user_by_email(email)
    if user[3] == password:
        return True
    else:
        return False

