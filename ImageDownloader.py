import os
from google_images_download import google_images_download


class Directory_Operator:

	def __init__(self,dir_path):
		self.dir_path = dir_path

	def create_dir(self,dir_name):
		self.dir = self.dir_path + '/' + dir_name
		if not os.path.exists(self.dir):
			os.makedirs(self.dir)

class Downloader:
	def __init__(self,keywords_file,dir_name):
		self.dir_path = dir_name + '/'
		with open(keywords_file) as self.file:
			self.keywords = [word for line in self.file for word in line.split()]
	
	def download_images(self,no_images):
		response = google_images_download.googleimagesdownload()  
  
		self.keywords

		def downloadimages(query): 
			# keywords is the search query 
			# format is the image file format 
			# limit is the number of images to be downloaded 
			# print urs is to print the image file url 
			# size is the image size which can 
			# be specified manually ("large, medium, icon") 
			# aspect ratio denotes the height width ratio 
			# of images to download. ("tall, square, wide, panoramic") 
			arguments = {"keywords": query, 
				"format": "jpg", 
				"limit": no_images, 
				"print_urls":True, 
				"size": "medium", 
				"output_directory": self.dir_path} 
			try: 
			    response.download(arguments) 
			  
			# Handling File NotFound Error     
			except FileNotFoundError:  
				pass

		# Driver Code 
		for item in self.keywords: 
		    downloadimages(item)  
		    print()  

if __name__ == '__main__':
	downloader = Downloader('Items.txt','Data_Raw')
	downloader.download_images(3)



