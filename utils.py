import math
import pandas
import numpy as np

def mean(arr: list):
	suma: int = 0

	for n in arr:
		suma += n
	return suma / len(arr)


def median(arr: list):
	arr.sort()
	return arr[int(len(arr) / 2)]


def mode(arr: list):
	dic = {}
	n = 0

	for i in arr:
		if not i in dic:
			dic[i] = 1
		else:
			dic[i] += 1

	for g, j in dic.items():
		if j == max(dic.values()):
			n = g;

	return n


def min(arr: list):
	n = arr[0]

	for i in arr:
		if i < n:
			n = i

	return n


def max(arr: list):
	n = arr[0]

	for i in arr:
		if i > n:
			n = i

	return n


def standard_derivation(arr):
	m = mean(arr)
	suma = 0

	for i in range(len(arr)):
		suma += (arr[i] - m)**2

	return np.sqrt(suma / (len(arr) - 1))


def percentile(arr: list, perc):
	return sorted(arr)[int(math.ceil((len(arr) * perc) / 100)) - 1]


def standarize(data):
	for i, value in enumerate(data):
		std = standard_derivation(data)
		data[i] = (value - mean(data)) / std
	return data


def destandarize(data):
	for i, value in enumerate(data):
		std = standard_derivation(data)
		data[i] = (value * std) + mean(data)
	return data


def normalize(data: pandas.DataFrame):
	for value in data.columns:
		_min = min(data[value])
		_max = max(data[value])
		data[value] = (data[value].values - _min) / (_max - _min)
	return data


def denormalize(data: pandas.DataFrame, reference: pandas.DataFrame):
	for value in data.columns:
		_min = min(reference[value])
		_max = max(reference[value])
		data[value] = data[value] * (_max - _min) + _min
	return data