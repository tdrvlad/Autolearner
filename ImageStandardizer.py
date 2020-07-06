import cv2
import numpy as np
from PIL import Image
import glob
import os
from resizeimage import resizeimage
import numpy as np

from skimage.measure import block_reduce

class Standardizer:

	def __init__(self, image_format, directory):
		self.directory = directory
		self.image_format = image_format

	def resize_images(self,height,width):
		self.height = height
		self.width = width

		for direct in os.listdir(self.directory + '/'):
			
			images = glob.glob(self.directory + '/' + direct + '/*.' + self.image_format)

			for image in images:
										
				img = cv2.imread(image)

				img_resized = cv2.resize(img, dsize=(self.height, self.width), interpolation=cv2.INTER_CUBIC)

				cv2.imwrite(image,img_resized)			

if __name__ == '__main__':

	keywords_file = 'Items.txt'
	no_images = 10
	image_format = 'jpg'

	resizer = Standardizer(image_format,'Data')
	resizer.resize_images(500,700)