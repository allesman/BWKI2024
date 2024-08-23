from ytmusicapi import YTMusic

def get_album(album_name:str)->tuple[str,list[str]]:
    ytmusic = YTMusic()
    r = ytmusic.search(query=album_name,filter="albums",limit=1)[0]
    img = r["thumbnails"][-1]["url"]
    album_id = r["browseId"]
    r = ytmusic.get_album(album_id)
    ids = [track["videoId"] for track in r["tracks"]]
    return img,ids