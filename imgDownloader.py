import requests
def download(url:str,title:str)->None:
    r = requests.get(url)
    img_data = r.content
    print(f"Downloading album cover for {title}")
    with open(f"images/{title}.png", "wb") as handler:
        handler.write(img_data)