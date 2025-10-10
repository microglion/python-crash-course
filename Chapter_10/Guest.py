from pathlib import Path

path = Path("guest.txt")
user = input("Please enter your name:")
path.write_text(user)
