from pathlib import Path
import json
def ask_fav_number():
    """Ask the user for their favorite number and store it in a file."""
    fav_number = input("What is your favorite number? ")
    path = Path('fav_number.json')
    contents = json.dumps(fav_number)
    path.write_text(contents)
    print(f"We'll remember your favorite number {fav_number} when you come back!")

def get_fav_number(path):
    if path.exists():
        contents = path.read_text()
        fav_number = json.loads(contents)
        return fav_number
    else:
        return None
def fav_number():
    #tell user their favorite number
    path = Path('fav_number.json')
    fav_number = get_fav_number(path)
    if fav_number:
        print(f"I know your favorite number! It's {fav_number}")
    else:
        ask_fav_number()


fav_number()