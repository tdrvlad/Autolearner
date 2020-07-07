import cv2
import glob
import os
import numpy as np
from google_images_download import google_images_download
import random

class DataManager:
	def __init__(self,keywords_file,directory_name,image_format):

		self.image_format = image_format
		self.directory_path = directory_name + '/'

		with open(keywords_file) as self.file:
			self.keywords = [word for line in self.file for word in line.split()]
	
	def download_images(self,no_images):
		response = google_images_download.googleimagesdownload()  
  
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
				"format": self.image_format, 
				"limit": no_images, 
				"print_urls":True, 
				"size": "medium", 
				"output_directory": self.directory_path} 
			try: 
			    response.download(arguments) 
			  
			# Handling File NotFound Error     
			except FileNotFoundError:  
				pass

		for item in self.keywords: 
			downloadimages(item)   

	def preprocess_images(self,height,width):
		self.height = height
		self.width = width

		for direct in os.listdir(self.directory_path):
			
			images = glob.glob(self.directory_path + direct + '/*.' + self.image_format)

			n = 1

			for image in images:
						
				img = cv2.imread(image)
				img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

				try:
					img_resized = cv2.resize(img, dsize=(self.height, self.width), interpolation=cv2.INTER_CUBIC)
				except:
					pass

				new_file = self.directory_path + direct + '/' + str(direct) + str(n) + '.' + self.image_format

				while os.path.exists(new_file):
					n += 1
					new_file = self.directory_path + direct + '/' + str(direct) + str(n) + '.' + self.image_format

				cv2.imwrite(new_file,img_resized)	

				n += 1

				os.remove(image)

	def mirror_images(self):
		for direct in os.listdir(self.directory_path):
			
			images = glob.glob(self.directory_path + direct + '/*.' + self.image_format)

			for image in images:
										
				img = cv2.imread(image)

				try:
					img_mirror = cv2.flip(img, 1)
				except:
					pass

				end = '.' + self.image_format
				new_file = image.replace(end,'') + 'mirrored.' + self.image_format

				cv2.imwrite(new_file, img_mirror)	

	def shuffle_training_data(self):
		data = []
		labels = []
		for direct in os.listdir(self.directory_path):
			
			images = glob.glob(self.directory_path + direct + '/*.' + self.image_format)

			data += images
			labels += [direct] * len(images)

		
		labeled_data = list(zip(data, labels))
		random.shuffle(labeled_data)

		self.labeled_data = labeled_data

	def split_data(self,test_ratio):
		n = int(len(self.labeled_data) * test_ratio)

		self.test_labeled_data = self.labeled_data[:n]
		self.train_labeled_data = self.labeled_data[n:]

		
	def return_train_test_data(self):
		test_data, test_labels = zip(*self.test_labeled_data)
		train_data, train_labels = zip(*self.train_labeled_data)

		return train_data, train_labels, test_data, test_labels
	

if __name__ == '__main__':

	data_manager = DataManager('Items.txt','Data','jpg')
	data_manager.download_images(10)
	data_manager.preprocess_images(100,100)
	data_manager.shuffle_training_data()
	data_manager.split_data(0.2)
	train_data, train_labels, test_data, test_labels = data_manager.return_train_test_data()

