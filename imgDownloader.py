import requests
def download(url:str,title:str)->None:
    r = requests.get(url)
    img_data = r.content
    # check if the file already exists
    try:
        with open(f"images/{title}.png") as f:
            print(f"Album cover for {title} already exists")
            return
    except FileNotFoundError:
        print(f"Downloading album cover for {title}")
        with open(f"images/{title}.png", "wb") as handler:
            handler.write(img_data)