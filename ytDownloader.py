from pytube.exceptions import AgeRestrictedError
from pytubefix import YouTube
import yt_dlp

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': "C:\\Users\\allesman",
    'outtmpl': 'C:\\Users\\allesman\\Desktop',
}

def download(url:str,index:int,title:str)->None:
    try :
        yt = YouTube(f'http://youtube.com/watch?v={url}',use_oauth=True,allow_oauth_cache=True)
        yt.streams.filter(only_audio=True)[0].download(output_path=f"videos/{title}/",filename=f"{index}.mp3")
    except Exception as e:
        print(f"Age restricted video for {title} at index {index}, using yt_dlp")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'http://youtube.com/watch?v={url}'])

def download_album(ids:list[str],title:str)->None:
    for i,url in enumerate(ids):
        # check if the file already exists
        try:
            with open(f"videos/{title}/{i}.mp3") as f:
                print(f"Track {i+1}/{len(ids)} for {title} already exists")
                continue
        except FileNotFoundError:
            print(f"Downloading track {i+1}/{len(ids)} for {title}")
            download(url,i,title)