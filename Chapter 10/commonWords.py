from pathlib import Path
filenames = ['AlicesAdventuresInWonderland.txt', 'howToLiveOn24HoursADay.txt', 'TheStrangeCaseofDrJekyllandMrHyde.txt']


for filename in filenames:
    path = Path(filename)
    try:
        contents=path.read_text(encoding='utf-8')
        count = contents.lower().count('the ')
        
    except FileNotFoundError:
        pass
    else:
        print(f"\n{filename}:")
        print(count)

        