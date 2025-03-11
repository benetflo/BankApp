# Hantering av registrering och inloggning
from database import add_user, get_user_by_email, delete_user

def register_user(name, email, password):
    if get_user_by_email(email):
        print("email already in use")
    else:
        add_user(name,email,password)

def remove_user(email, userid):
    if get_user_by_email(email):
        delete_user(userid)
    else:
        print("No user with that email exists")

def user_loggin(email,password):
    user = get_user_by_email(email)
    if user[3] == password:
        return True
    else:
        print("No user with that email exists")







    
