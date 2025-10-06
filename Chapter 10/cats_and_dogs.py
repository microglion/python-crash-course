from pathlib import Path
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(f"\n{filename}:")
        print(contents)
