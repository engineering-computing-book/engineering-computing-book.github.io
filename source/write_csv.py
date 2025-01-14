import csv

data = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  #  Data to save
with open("data.csv", "w") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerows(data)
