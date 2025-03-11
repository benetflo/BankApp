# ui display
import time
from functions import *

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

def main():
    # display login menu
    display_menu(start_items)    
    
    # start menu
    while True:
        clear()
        display_menu(start_items)
        latest_action = move_cursor(start_items)
        
        # check if user pressed enter
        if latest_action == "enter":
            if latest_action == 0:
                # call login function
                login_screen()
                time.sleep(0.2)
                
            elif latest_action == 1:
                # call create account function
                create_account_screen()
                time.sleep(0.2)
    
    # main menu (post login)
    """
    while True:
        pass
    """ 
            
    

if __name__ == "__main__":
    main()