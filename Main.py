from ImageDownloader import Downloader 
from ImageStandardizer import Standardizer 


data_dir = 'Data'
keywords_file = 'Items.txt'
no_images = 10
image_format = 'jpg'

downloader = Downloader(keywords_file,data_dir)
downloader.download_images(no_images)

resizer = Standardizer(image_format,data_dir)
resizer.resize_images(200,200)