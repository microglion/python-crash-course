from pathlib import Path

path = Path('learningPython.txt')
contents = path.read_text()


for line in contents.splitlines():
    print(line.replace('Python', 'C'))
