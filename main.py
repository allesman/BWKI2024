import ytMusicApi,ytDownloader,imgDownloader

query = "New Levels New Devils"

img,ids = ytMusicApi.get_album(query)

imgDownloader.download(img,query)

ytDownloader.download_album(ids,query)

# https://huggingface.co/docs/datasets/image_dataset#imagefolder