import ytMusicApi,ytDownloader,imgDownloader,re, pathvalidate


def get_albums(query:list[str]):
    for q in query:
        get_album(q)


def get_album(query:str):
    img,ids = ytMusicApi.get_album(query)
    # sanitize the query to remove any invalid characters
    query = pathvalidate.sanitize_filename(query)
    imgDownloader.download(img,query)
    ytDownloader.download_album(ids,query)

# read the file data/top_5000.csv and get the album title and artist name
# with open('data/top_5000.csv',encoding="utf8") as f:
#     albums = f.readlines()
#     albums = [album.strip().split(',') for album in albums]
#     albums = [album[1] + " " + album[2] for album in albums[1:]]
#     get_albums(albums)

# from https://chartmasters.org/spotify-most-streamed-albums/
with open('data/top_spotify.csv',encoding="utf8") as f:
    albums = f.readlines()
    albums = [re.split(r',(?=")',album.strip()) for album in albums]
    albums = [album[3][1:-1] for album in albums[1:]]
    # print(albums)
    get_albums(albums)