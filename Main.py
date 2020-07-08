from DataManager import DataManager
from Classifier import Classifier
import os

data_dir = 'Data'
keywords_file = 'Items.txt'
no_images = 5
image_format = 'jpg'

data_manager = DataManager(keywords_file,data_dir,image_format)

if os.path.exists(data_dir):
	print('Data exists')
else:
	print('Downloading Data')
	data_manager.download_images(no_images)
	print('Preprocessing Data')
	data_manager.preprocess_images(100,100)

print('Shuffling and Splitting Data')
data_manager.shuffle_training_data()
data_manager.split_data(0.2)

labeled_data = data_manager.return_train_test_data()

classifier = Classifier((100,100),labeled_data)
classifier.onehot_labels()

print('Training Neural Network')
classifier.train_nn(epochs = 5)