import pandas
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns

def generate_pair(subjects, data):
	colors = {
		"Gryffindor":"red",
		"Slytherin":"green",
		"Ravenclaw":"blue",
		"Hufflepuff":"grey"
	}

	plt.clf()
	data = data.drop(columns=['Index'])

	matrix = data.select_dtypes(include = [float, int])
	matrix['Hogwarts House'] = data['Hogwarts House']
	sns.pairplot(matrix, hue='Hogwarts House', palette = colors)
	#plt.title('Heatmap of Correlations\n\n', fontsize="50", fontweight = "bold")

	parent_dir = "./plots/"
	if not os.path.isdir(parent_dir):
		os.mkdir(parent_dir)
	plt.savefig(parent_dir + "pair_plot.jpg")


if __name__ == '__main__':
	data = pandas.read_csv("./datasets/dataset_train.csv")
	data_numeric = data.select_dtypes(include = [float, int])

	plt.rcParams["figure.figsize"] = (20, 20)
	fig = plt.figure() 

	plt.title('Pair Plot\n\n', fontsize="50", fontweight = "bold")
	plt.axis('off')
	generate_pair(data_numeric.columns, data)
	
	fig.tight_layout()
	