from pathlib import Path

path = Path("guest_book.txt")
guests = ''
users = True
while users:
    user = input("Please enter your name: (or enter q if no more users)\n")
    if user == 'q':
        break
    else:
        guests += user + "\n"
        path.write_text(guests)
