from numpy import argmax
from numpy import array
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from keras.utils import to_categorical
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class Classifier:
	def __init__(self,input_shape,labeled_data):

		self.input_height, self.input_width = input_shape
		self.train_data, self.train_labels, self.test_data, self.test_labels = labeled_data
		
		self.categories = list(set(self.train_labels + self.test_labels))

	def onehot_labels(self):
		
		# integer encode
		label_encoder = LabelEncoder()
		integer_encoded = label_encoder.fit_transform(array(self.categories))

		# binary encode
		onehot_encoder = OneHotEncoder(sparse=False)
		integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
		onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

		# Replace all labells with one-hot labels
		self.train_onehot_labels = [onehot_encoded[self.categories.index(item)] for item in self.train_labels]
		
	def train_nn(self, epochs):	
		
		no_input_neurons = self.input_height * self.input_width
		k = int(np.log(no_input_neurons)) + 1

		print(self.train_data[0])
		model = keras.Sequential([keras.layers.Flatten(input_shape = (self.input_height,self.input_width)),
						#keras.layers.Dropout(0.5),
		                keras.layers.Dense(2**k,activation = tf.nn.sigmoid),    
		                #keras.layers.Dropout(0.2),   
		                #keras.layers.Dense(2**(k-2),activation = tf.nn.sigmoid),                   
		                keras.layers.Dense(len(self.categories),activation = tf.nn.softmax)])
		model.compile(optimizer = 'adam',loss='sparse_categorical_crossentropy',metrics =['accuracy'])

		model.fit(self.train_data, self.train_labels, epochs = epochs)



	def predict(self,input):
		pass

