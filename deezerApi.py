from typing import Union, Tuple, Any

import requests,json


def get_album(album_id:int)-> Union[bool, tuple[Any, Any]]:
    r = requests.get(f"https://api.deezer.com/album/{album_id}")
    if not r.ok:
        return False
    parsed = json.loads(r.text)
    if "error" in parsed:
        return False
    return parsed["title"],parsed["cover_xl"]

def file_from_album(album_id:int)->None:
    title,url = get_album(album_id)
    r = requests.get(url)
    img_data= r.content
    with open (f"images/{title}.png","wb") as handler:
        handler.write(img_data)
