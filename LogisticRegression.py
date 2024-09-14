import utils
import pandas

def main():
	csv = pandas.read_csv("./datasets/dataset_train.csv")
	csv.describe()

main()