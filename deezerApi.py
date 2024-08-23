from typing import Union, Tuple, Any

import requests,json


def get_album(album_id:int)-> Union[bool, tuple[Any, Any]]:
    r = requests.get(f"https://api.deezer.com/album/{album_id}")
    parsed = json.loads(r.text)
    if "error" in parsed:
        return False
        # raise Exception("Invalid Album ID.")
    return parsed["title"],parsed["cover_xl"]