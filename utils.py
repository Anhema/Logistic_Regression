import math
import pandas

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


def standard_derivation(arr: list):
	m = mean(arr)
	suma: int = 0

	for i in arr:
		suma += (i - m)**2

	return math.sqrt(suma / (len(arr) - 1))


def percentile(arr: list, perc):
	return sorted(arr)[int(math.ceil((len(arr) * perc) / 100)) - 1]


def standarize(data):
	for i, value in enumerate(data):
		data[i] = (value - mean(data)) / standard_derivation(data)
	return data
