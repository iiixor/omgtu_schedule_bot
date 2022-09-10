import csv

class Database():
    # import csv

    with open('database.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
