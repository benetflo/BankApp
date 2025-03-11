# functions module for ui
import os
import readchar
import time

mouse_index = 0 # default value
    
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# display menu items and highlight selected item
def display_menu(items):
    global mouse_index
    selected_item = ""
    
    for item in items:
        if items[mouse_index] == item:
            print(f"[X] {item}")
            selected_item = item
        else:
            print(f"[ ] {item}")
            
    
    print(f"mouse index: {mouse_index}")
    
    return selected_item
        
        
def move_cursor(items):
    global mouse_index
    key = readchar.readkey()
    
    if key == readchar.key.UP:
        mouse_index -= 1
        if mouse_index < 0:
            mouse_index = len(items) - 1
        return mouse_index
        
    elif key == readchar.key.DOWN:
        mouse_index += 1
        if mouse_index > len(items) - 1:
            mouse_index = 0
        return mouse_index
    
    elif key == readchar.key.ENTER:
        return "enter"
    
    elif key == readchar.key.ESC:
        return "exit"    


def login_screen():
    print("Login screen called")


def create_account_screen():
    print("Create account screen called")


item = ["test", "boll"]

if __name__ == "__main__":
    print("Hello from functions")
    while True:
        time.sleep(0.4)
        clear()
        display_menu(item)
        move_cursor(item)
        print(f"mouse index: {mouse_index}")