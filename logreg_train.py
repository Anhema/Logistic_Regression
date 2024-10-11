import pandas
import matplotlib.pyplot as plt
import os
import utils
import numpy as np
from typing import Callable
import pickle

def sigmoid(x):
	return (1 / 1 + np.exp(-x))


def gradient_descent(data, classes, theta, learning_rate: float, iterations: int):
	size = len(data)
	cost_history = np.zeros(iterations)

	for i in range(iterations):
		s = sigmoid(data @ theta)
		gradient = (1 / size) * data.T @ (size - classes)
		theta = theta - learning_rate * gradient
		
	return theta


def fill_missing_with_median(df: pandas.DataFrame) -> pandas.DataFrame:
    numerical_cols = df.select_dtypes(include=[float, int]).columns
    for col in numerical_cols:
        non_na_values = df[col].dropna().tolist()
        median_value = utils.median(non_na_values)
        if median_value is not None:
            df[col] = df[col].fillna(median_value)
    return df


if __name__ == '__main__':
	
	learning_rate = 0.01
	iterations = 1000
	
	data: pandas.DataFrame = pandas.read_csv("./datasets/dataset_train.csv")
	data = fill_missing_with_median(data)
	# GET HOUSES
	print("--------------Hogwarts Houses--------------\n")
	category = data['Hogwarts House'].astype('category')
	y = category.cat.codes.to_numpy()
	classes = category.cat.categories.tolist()
	print(classes)

	# GET SELECTED FEATURES
	print("\n\n--------------Selected Features--------------\n")
	features = ['Ancient Runes', 'Defense Against the Dark Arts', 'Charms', 'Divination']
	data = data[features]
	print(data)

	#AÑADIR BIAS QUE ES UN FEATURE EXTRA
	print("\n\n--------------Features With BIAS--------------\n")
	data = data.to_numpy()
	data = np.insert(data, 0, 1, axis=1)
	print(data)

	theta = np.zeros((len(classes), data.shape[1]))[0]
	gradient_descent(data, y, theta, learning_rate, iterations)
