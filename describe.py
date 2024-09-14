import pandas
import numpy
import utils

def ft_describe(data: pandas.DataFrame) -> pandas.DataFrame:
    desc = {}
    for column in data.select_dtypes(include=numerics): #select_dtypes = Get numeric columns from readed data csv
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

        desc[column] = stat
    
    data_frame: pandas.DataFrame = pandas.DataFrame(desc)
    print(data_frame)
        

if __name__ == '__main__':
    data = pandas.read_csv("./datasets/dataset_train.csv")
    numerics = [float, int]

    ## ESTE ES EL RESULTADO QUE TENGO QUE IMITAR
    print("------------ESTE ES EL RESULTADO QUE TENGO QUE IMITAR------------")
    desc = data.describe(include=numerics)
    print(desc)
    print("-----------------------------------------------------------------")

    ft_describe(data)


