from pathlib import Path
import json

def get_stored_data(path):
    #get stored data if available.
    if path.exists():
        contents = path.read_text()
        data = json.loads(contents)
        return data
    else:
        return None

def get_new_data(path):
    #prompt for a new username.
    data = {}
    data['username'] = input("What's your name? ")
    data['age'] = input("What's your age? ")
    data['sex'] = input("what is your gender? M(male), F(female) or O(other)")
    contents = json.dumps(data)
    path.write_text(contents)
    return data

def greet_user():
    #greet the user by name.
    path = Path('username.json')
    data = get_stored_data(path)
    if data:                                                
        print(f"Welcome back, {data['username']}! You are {data['age']} years old & {data['sex']} gender. ")
    else:
        data = get_new_data(path)
        print(f"We'll remember you when you come back, {data['username']}!")

greet_user()