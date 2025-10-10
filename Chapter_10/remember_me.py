from pathlib import Path
import json

def get_stored_username(path):
    #get stored username if available.
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    #prompt for a new username
    username = input("What's your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    #greet the user by name.
    path = Path('username.json')
    username = get_stored_username(path)
    if username:                                                
        correctUser = input(f"are you {username}? enter 'Y' for Yes or 'N' for No ")
        if correctUser == 'Y':
            print(f"Welcome back, {username}!")
        else: 
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!") 
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()