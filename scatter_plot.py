import pandas
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import seaborn as sns

def generate_scatter(subjects, data):
	colors = {
		"Gryffindor":"red",
		"Slytherin":"green",
		"Ravenclaw":"blue",
		"Hufflepuff":"grey"
	}

	#data.drop(columns=['Index'])
	subjects = subjects.delete(0)

	for i, subject in enumerate(subjects):
		for j, subject_J in enumerate(subjects):
			for house in data["Hogwarts House"].unique().tolist():
				plt.subplot(len(subjects), len(subjects), ((i * len(subjects)) + j) + 1)
				x = data.loc[data["Hogwarts House"] == house].dropna()
				plt.scatter(x[subject], x[subject_J], alpha = 1, ec = "white", color=colors[house])
				plt.xticks(visible=False)
				plt.yticks(visible=False)
				if i == 0:
					if not j % 2 == 0:
						plt.title(subject_J, pad=20)
					else:
						plt.title(subject_J)
				if j == 0:
					if not i % 2 == 0:
						plt.ylabel(subject, labelpad = 20)
					else:
						plt.ylabel(subject)
					#plt.ylabel(subject)

	fig.tight_layout()
	parent_dir = "./plots/"
	if not os.path.isdir(parent_dir):
		os.mkdir(parent_dir)
	plt.savefig(parent_dir + "scatter_plot.jpg")


def generate_correlation_matrix(subjects, data):
	
	plt.clf()
	plt.title('Heatmap of Correlations\n', fontsize="50", fontweight = "bold")
	
	data = data.drop(columns=['Index'])
	matrix = data.corr()
	g = sns.heatmap(matrix, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
	g.set_yticklabels(g.get_yticklabels(), rotation = 0, fontsize = 12)
	g.set_xticklabels(g.get_xticklabels(), fontsize = 12)

	fig.tight_layout()
	parent_dir = "./plots/"
	if not os.path.isdir(parent_dir):
		os.mkdir(parent_dir)

	plt.savefig(parent_dir + "correlation_matrix.jpg")


if __name__ == '__main__':
	data = pandas.read_csv("./datasets/dataset_train.csv")
	data_numeric = data.select_dtypes(include = [float, int])

	plt.rcParams["figure.figsize"] = (20, 20)
	fig = plt.figure() 

	plt.title('Scatter Plot\n', fontsize="50", fontweight = "bold")
	plt.axis('off')
	generate_scatter(data_numeric.columns, data)
	generate_correlation_matrix(data_numeric.columns, data_numeric)
	
	fig.tight_layout()
	