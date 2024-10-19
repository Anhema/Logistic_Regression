import pandas
import utils
import sys

def ft_describe(data: pandas.DataFrame, inc = [float, int]) -> pandas.DataFrame:
	desc = {}
	for column in data.select_dtypes(include = inc): #select_dtypes = Get numeric columns from readed data csv
		stat = {}
		column_data = data[column].dropna().to_list() # dropna() = Delete NULL elements from a list

		stat["count"] = len(column_data)
		stat["mean"] = utils.mean(column_data)
		stat["std"] = utils.standard_derivation(column_data)
		stat["min"] = utils.min(column_data)
		stat["25%"] = utils.percentile(column_data, 25)
		stat["50%"] = utils.percentile(column_data, 50)
		stat["75%"] = utils.percentile(column_data, 75)
		stat["max"] = utils.max(column_data)
		stat["mode"] = utils.mode(column_data)
		stat["var"] = utils.variance(column_data)

		desc[column] = stat
	
	data_frame: pandas.DataFrame = pandas.DataFrame(desc)
	print(data_frame)
	return data_frame
		

if __name__ == '__main__':

	if len(sys.argv) != 2:
		print("The arguments are bad")
		exit(1)

	try:
		data: pandas.DataFrame = pandas.read_csv(sys.argv[1])
	except:
		print("Error reading data")
		exit(1)

	numerics = [float, int]

	## ORIGINAL DESCRIBE
	print("------------ORIGINAL DESCRIBE RESULT------------")
	desc = data.describe(include=numerics)
	print(desc)
	print("-----------------------------------------------------------------\n")

	ft_describe(data)


