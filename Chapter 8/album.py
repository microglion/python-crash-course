def make_album(artist, album, Num_songs=None):
    albums = {'artist':artist, 'album':album,}
    if Num_songs:
        albums['number of songs'] = Num_songs

    return(albums)

while True:
    print("\nPlease enter artist name:")
    print("\nenter 'q' to quit:")

    art_name = input('artist: ')
    if art_name == 'q':
        break

    print("\nPlease enter album name:")
    print("\nenter 'q' to quit:")

    alb_name = input('album: ')
    if alb_name == 'q':
        break

    print("\nPlease enter number of songs:")
    print("\nenter 'p' if you don't know the number of songs")
    print("\nenter 'q' to quit:")

    num_songs = input('number of songs: ')
    if num_songs == 'q':
        break
    elif num_songs == 'p':
        num_songs = None
    else:
        num_songs = int(num_songs)

    entered_album = make_album(art_name, alb_name, num_songs)
    print(entered_album)