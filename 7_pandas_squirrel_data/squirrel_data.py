import pandas

# Save csv data to pandas DataFrame
squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Data.csv')

# Count squirrel of specific fur colors and save to squirrel_count.csv
black_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
cinnamon_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
gray_fur_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])

fur_count_dict = {
    "Fur color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_fur_count, gray_fur_count, cinnamon_fur_count]
}

fur_count_dataframe = pandas.DataFrame(fur_count_dict)
fur_count_dataframe.to_csv("fur_count.csv")
