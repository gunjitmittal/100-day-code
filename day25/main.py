from heapq import nlargest
import pandas
data = pandas.read_csv("Squirrel_Data.csv")
fur_data = data["Primary Fur Color"]
gray_squirrels_no = len(data[fur_data == "Gray"])
red_squirrels_no = len(data[fur_data == "Cinnamon"])
black_squirrels_no = len(data[fur_data == "Black"])
data = {"Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_squirrels_no, red_squirrels_no, black_squirrels_no]}
fur_colour_count = pandas.DataFrame(data)
fur_colour_count.to_csv("Squirrel_count.csv")
