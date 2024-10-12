import pandas
import matplotlib.pyplot as plt
import os
import utils
import numpy as np
from typing import Callable
import pickle

def sigmoid_function(x):
	return (1 / (1 + np.exp(-x)))

def cost_function(data, vals, theta):
	size = len(vals)
	h = sigmoid_function(data @ theta)
	cost = -(1 / size) * ((vals @ np.log(h)) + ((1 - vals) @ np.log(1 - h)))
	return cost

def gradient_descent(data, vals, theta, learning_rate: float, iterations: int):
	size = len(vals)
	all_cost = np.zeros(iterations)

	for i in range(iterations):
		sigmoid = sigmoid_function(data @ theta)
		gradient = (1 / size) * data.T @ (sigmoid - vals)
		theta = theta - (learning_rate * gradient)
		all_cost[i] = cost_function(data, vals, theta)
	
	return theta, all_cost


def replace_nan_with_median(data: pandas.DataFrame) -> pandas.DataFrame:
	num_cols = data.select_dtypes(include=[float, int]).columns
	for col in num_cols:
		values = data[col].dropna().tolist()
		median = utils.median(values)
		if median is not None:
			data[col] = data[col].fillna(median)
	return data


if __name__ == '__main__':
	
	learning_rate = 0.01
	iterations = 10000
	
	data: pandas.DataFrame = pandas.read_csv("./datasets/dataset_train.csv")
	data = replace_nan_with_median(data)

	# GET HOUSES
	print("--------------Hogwarts Houses--------------\n")
	category = data['Hogwarts House'].astype('category')
	y = category.cat.codes.to_numpy() # Get the original results to compare our precission 
	orig_houses = category.cat.categories.tolist()
	print(orig_houses)
	houses = np.arange(len(orig_houses))

	# GET SELECTED FEATURES
	print("\n\n--------------Selected Features--------------\n")
	features = ['Ancient Runes', 'Defense Against the Dark Arts', 'Charms', 'Divination']
	data = data[features]
	print(data)

	# STANDARIZE DATA
	print("\n\n--------------STANDARIZE DATA--------------\n")
	data = data.to_numpy()
	data = utils.standarize(data)
	print(data)

	# ADD BIAS AS AN EXTRA FEATURE
	print("\n\n--------------Features With BIAS--------------\n")
	#data = data.to_numpy()
	data = np.insert(data, 0, 1.0, axis=1)
	print(data)

	# EXECUTE TRAINING
	print("\n\n--------------TRAINING--------------\n")
	all_thetas = np.zeros((len(houses), data.shape[1]))
	all_costs = []
	for i, house in enumerate(houses):
		vals = np.where(y == house, 1, 0) # For each Hogwarts house make a list from students with 1 if they are from that house or 0 if not
		theta, cost = gradient_descent(data, vals, all_thetas[i], learning_rate, iterations)
		all_thetas[i] = theta
		all_costs.append(cost)
		print(orig_houses[house])
		print (f"THETAS: {theta.tolist()}")
		print (f"COST: {cost}\n")

	# print(all_thetas)
	# print(all_costs)

	# DRAW LOSS COST
	plt.rcParams["figure.figsize"] = (10, 10)
	fig = plt.figure() 
	for i, cost_history in enumerate(all_costs):
		plt.subplot(2, 2, i + 1)
		plt.plot(cost_history) 
		plt.title(orig_houses[i])
		plt.xlabel('Iterations')
		plt.ylabel('Cost')

	fig.tight_layout()
	plt.savefig('plots/cost.png')

	# SAVE RESULTS
	output_dir = 'datasets'
	os.makedirs('datasets', exist_ok=True)
	output_path = os.path.join('datasets', 'logreg_thetas.pkl')
	with open(output_path, 'wb') as f:
		pickle.dump(all_thetas, f)
	print(f'Thetas values saved in {output_path}.')
	
	# with open(output_path, 'rb') as file:
	# 	weights = pickle.load(file)
	# 	print(weights)