import deezerApi
album = deezerApi.get_album(304127)
if album:
    print(album)