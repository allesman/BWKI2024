from pytubefix import YouTube

def download(url:str,index:int,title:str)->None:
    yt = YouTube(f'http://youtube.com/watch?v={url}')
    yt.streams.filter(only_audio=True)[0].download(output_path=f"videos/{title}/",filename=f"{index}.mp3")

def download_album(ids:list[str],title:str)->None:
    for i,url in enumerate(ids):
        print(f"Downloading track {i+1}/{len(ids)} for {title}")
        download(url,i,title)