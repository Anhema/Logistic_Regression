import pandas
import matplotlib.pyplot as plt
import os
import sys
from utils import *
import numpy as np
import pickle

def sigmoid_function(x):
	return (1 / (1 + np.exp(-x)))


def cost_function(data, vals, theta):
	size = len(vals)
	h = sigmoid_function(data @ theta)
	cost = -(1 / size) * ((vals @ np.log(h)) + ((1 - vals) @ np.log(1 - h)))
	return cost


def stochastic_gradient_descent(data, vals, theta, learning_rate: float, iterations: int):
	
	size = len(vals)
	all_cost = []

	for i in range(iterations):
		rand_i = np.random.randint(size)
		x = data[rand_i]
		y = vals[rand_i]
		for n in range(size):
			x_i = x[n]
			y_i = y[n]
			sigmoid = sigmoid_function(x_i @ theta)
			gradient = (sigmoid - y_i) * x_i.T
			theta = theta - (learning_rate * gradient)

		all_cost.append(cost_function(data, vals, theta))
	
	return theta, all_cost


if __name__ == '__main__':
	
	if len(sys.argv) != 2:
		print("The arguments are bad")
		exit(1)

	try:
		data: pandas.DataFrame = pandas.read_csv(sys.argv[1])
		data = replace_nan_with_median(data)
	except:
		print("Error reading data")
		exit(1)
	
	learning_rate = 0.01
	iterations = 100

	# GET HOUSES
	print("--------------Hogwarts Houses--------------\n")
	category = data['Hogwarts House'].astype('category')
	y = category.cat.codes.to_numpy() # Get the original results to compare our precission 
	orig_houses = category.cat.categories.tolist()
	print(orig_houses)
	houses = np.arange(len(orig_houses))

	# GET SELECTED FEATURES
	print("\n\n--------------Selected Features--------------\n")
	#features = ['Ancient Runes', 'Defense Against the Dark Arts', 'Charms']
	features = ['Ancient Runes', 'Defense Against the Dark Arts', 'Charms', 'Divination']
	data = data[features]
	print(data)

	if NORMALIZE:
		# NORMALIZE DATA
		print("\n\n--------------NORMALIZE DATA--------------\n")
		data = normalize(data)
		print(data)
		data = data.to_numpy()
	else:
		# STANDARIZE DATA
		print("\n\n--------------STANDARIZE DATA--------------\n")
		data = data.to_numpy()
		data = standarize(data)
		print(data)

	# ADD BIAS AS AN EXTRA FEATURE
	print("\n\n--------------Features With BIAS--------------\n")
	data = np.insert(data, 0, 1.0, axis=1)
	print(data)

	# EXECUTE TRAINING
	print("\n\n--------------TRAINING--------------\n")
	all_thetas = np.zeros((len(houses), data.shape[1]))
	#all_thetas = np.zeros((data.shape[1], 5))
	all_costs = []
	for i, house in enumerate(houses):
		vals = np.where(y == house, 1, 0) # For each Hogwarts house make a list from students with 1 if they are from that house or 0 if not
		theta, cost = stochastic_gradient_descent(data, vals, all_thetas[i], learning_rate, iterations)
		print(theta)
		all_thetas[i] = theta
		all_costs.append(cost)
		print(orig_houses[house])
		print (f"THETAS: {theta.tolist()}")
		print (f"COST: {cost}\n")

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
	plt.savefig('plots/stochastic_cost.png')

	# SAVE RESULTS
	output_dir = 'datasets'
	os.makedirs('datasets', exist_ok=True)
	output_path = os.path.join('datasets', 'stochastic_logreg_thetas.pkl')
	with open(output_path, 'wb') as f:
		pickle.dump(all_thetas, f)
	print(f'Thetas values saved in {output_path}.')

