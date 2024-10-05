import pandas
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import os

def generate_histogram(rows: int, cols: int, subjects, data: pandas.DataFrame):
	colors = {
		"Gryffindor":"red",
		"Slytherin":"grey",
		"Ravenclaw":"blue",
		"Hufflepuff":"green"
	}
	
	for i, subject in enumerate(subjects):
		if i == 0:
			continue
		for house in data["Hogwarts House"].unique().tolist():
			plt.subplot(rows, cols, i)
			plt.title(subject, fontsize=16)
			x = data.loc[data["Hogwarts House"] == house, subject].dropna()
			plt.hist(x, alpha = 0.5, ec='black', color=colors[house])
			plt.xlabel("Scores")  
			plt.ylabel("Students")

	ax = plt.subplot(rows, cols, len(subjects))
	#create legend
	handles = [Rectangle((0,0), 1, 1, color=c, ec="k") for c in ["red", "grey", "blue", "green"]]
	labels= ["Gryffindor","Slytherin", "Ravenclaw", "Hufflepuff"]
	plt.legend(handles, labels, loc="center", fontsize="16")
	plt.axis('off')


if __name__ == '__main__':
	data: pandas.DataFrame = pandas.read_csv("./datasets/dataset_train.csv")
	data_numeric: pandas.DataFrame = data.select_dtypes(include = [float, int])

	plt.rcParams["figure.figsize"] = (20, 10)
	fig = plt.figure() 

	plt.title('Histogram\n\n', fontsize="20", fontweight = "bold")
	plt.axis('off')
	generate_histogram(2, int(len(data_numeric.columns) / 2), data_numeric.columns, data)
	
	fig.tight_layout()

	parent_dir = "./plots/"
	if not os.path.isdir(parent_dir):
		os.mkdir(parent_dir)
	plt.savefig(parent_dir + "histogram.jpg")