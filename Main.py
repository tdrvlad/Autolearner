from DataManager import DataManager
from Classifier import Classifier

data_dir = 'Data'
keywords_file = 'Items.txt'
no_images = 5
image_format = 'jpg'

data_manager = DataManager(keywords_file,data_dir,image_format)
'''
data_manager.download_images(no_images)
data_manager.preprocess_images(100,100)
'''
data_manager.shuffle_training_data()
data_manager.split_data(0.2)

labeled_data = data_manager.return_train_test_data()

classifier = Classifier((100,100),labeled_data)
classifier.onehot_labels()
classifier.train_nn(epochs = 5)