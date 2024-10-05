import pandas
import matplotlib.pyplot as plt
import os
import utils
import numpy
from typing import Callable
import pickle

def sigmoid(x):
	return (1 / 1 + numpy.exp(-x))


def gradient_descent(features, categories, gradient: Callable[[float], float], learn_rate: float, max_iter: int, tol: float = 0.01):
	print(x @ theta)
	return theta


if __name__ == '__main__':
	features = ['Ancient Runes', 'Defense Against the Dark Arts', 'Charms', 'Divination']
	data: pandas.DataFrame = pandas.read_csv("./datasets/dataset_train.csv")
	
	category = data['Hogwarts House'].astype('category')
	y = category.cat.codes.to_numpy()
	classes = category.cat.categories.tolist()
	print(y)
	print(classes)
	print(data)

	data = data[features]
	##AÑADIR BIAS QUE ES UN FEATURE EXTRA (THETA0 EN EL LINEAR REGRESSION)

	#history, result = gradient_descent(data, 2, sigmoid, 0.1, 100)
