import math
import pandas
import numpy as np

NORMALIZE: bool = True

def mean(arr: list):

	if len(arr) == 0:
		return None

	suma: int = 0

	for n in arr:
		suma += n
	return suma / len(arr)


def median(arr: list):

	if len(arr) == 0:
		return None

	arr.sort()
	return arr[int(len(arr) / 2)]


def mode(arr: list):

	if len(arr) == 0:
		return None

	dic = {}
	n = 0

	for i in arr:
		if not i in dic:
			dic[i] = 1
		else:
			dic[i] += 1

	for g, j in dic.items():
		if j == max(list(dic.values())):
			n = g

	return n


def variance(arr: list):

	if len(arr) == 0:
		return None

	n = len(arr)
	m = mean(arr)

	deviations = [(x - m) ** 2 for x in arr]
	variance = sum (deviations) / n
	return variance


def min(arr: list):

	if len(arr) == 0:
		return None

	n = arr[0]

	for i in arr:
		if i < n:
			n = i

	return n


def max(arr: list):

	if len(arr) == 0:
		return None

	n = arr[0]

	for i in arr:
		if i > n:
			n = i

	return n


def standard_derivation(arr):
	if len(arr) == 0:
		return None
	m = mean(arr)
	suma = 0

	for i in range(len(arr)):
		suma += (arr[i] - m)**2

	return np.sqrt(suma / (len(arr) - 1))


def percentile(arr: list, perc):
	if len(arr) == 0:
		return None
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


def replace_nan_with_median(data: pandas.DataFrame) -> pandas.DataFrame:
	num_cols = data.select_dtypes(include=[float, int]).columns
	for col in num_cols:
		values = data[col].dropna().tolist()
		med = median(values)
		if med is not None:
			data[col] = data[col].fillna(med)
	return data

