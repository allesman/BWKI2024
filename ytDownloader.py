from pytubefix import YouTube

def download(url:str,index:int,title:str)->None:
    yt = YouTube(f'http://youtube.com/watch?v={url}',use_oauth=True,allow_oauth_cache=True)
    yt.streams.filter(only_audio=True)[0].download(output_path=f"videos/{title}/",filename=f"{index}.mp3")

def download_album(ids:list[str],title:str)->None:
    for i,url in enumerate(ids):
        if url is None:
            print(f"Track {i+1}/{len(ids)} for {title} is not available")
            continue
        # check if the file already exists
        try:
            with open(f"videos/{title}/{i}.mp3") as f:
                print(f"Track {i+1}/{len(ids)} for {title} already exists")
                continue
        except FileNotFoundError:
            print(f"Downloading track {i+1}/{len(ids)} for {title}")
            download(url,i,title)