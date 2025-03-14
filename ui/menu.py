from functions import *
from user import User

menu_items = [  
    "Show balance",
    "Deposit",
    "Show transactions",
    "Withdraw",
    "Change password",
    "Cancel account",
    "Logout"]

start_items = [
    "Login",
    "Create account"]

login_items = [
    "Username",
    "Password"]

create_items = [
    "Username",
    "Password",
    "Confirm password"]


# display login menu
def login_menu():
    clear()
    display_menu(start_items) 
    latest_action = move_cursor(start_items)
    m_index = get_mouse_index()
    
    # check if user pressed enter
    if latest_action == "enter":
        if m_index == 0:
            # call login function
            login()
            time.sleep(1)
            
        elif m_index == 1:
            # call create account function
            create_account()
            time.sleep(1)


# display create accoun menu
def create_account_menu(items):

    username = input(f"{items[0]}: ")
    clear()
    
    while True:
        password = input(f"{items[1]}: ") 
        clear()
        
        confirm_password = input(f"{items[2]}: ")
        clear()
        
        if password != confirm_password:
            print("Passwords do not match")
            input("Press enter to try again")
            continue
        
        else:
            break
    
    print(username)
    print(password)
    print(confirm_password)

    

if __name__ == "__main__":
    create_account_menu(create_items)