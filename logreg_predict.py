import pandas
import matplotlib.pyplot as plt
import os
import sys
from utils import *
import numpy as np
import pickle


def sigmoid_function(x):
	return (1 / (1 + np.exp(-x)))


if __name__ == '__main__':

	if len(sys.argv) != 3 or not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".pkl"):
		print("The arguments are bad")
		exit(1)

	try:
		data_orig: pandas.DataFrame = pandas.read_csv(sys.argv[1])
		data_orig = replace_nan_with_median(data_orig)
	except:
		print("Error reading data" + e)
		exit(1)
	
	if not os.path.exists(sys.argv[2]):
		print(".pkl file not found")
		exit(1)

	with open(sys.argv[2], 'rb') as file:
		thetas = pickle.load(file)
		print(thetas)

	features = ['Ancient Runes', 'Defense Against the Dark Arts', 'Charms', 'Divination']
	data_orig = data_orig[features]

	if NORMALIZE:
		data = normalize(data_orig)
		data = data.to_numpy()
	else:
		data = data_orig.to_numpy()
		data = standarize(data)
	
	data = np.insert(data, 0, 1.0, axis=1)
	probabilities = sigmoid_function(data @ thetas.T)
	predictions =  np.argmax(probabilities, axis=1)
	houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
	predictions_houses = [houses[predict] for predict in predictions]

	result = pandas.DataFrame({
		'Index': data_orig.index,
		'Hogwarts House': predictions_houses
	})

	output_file = 'datasets/houses.csv'
	result.to_csv(output_file, index=False)