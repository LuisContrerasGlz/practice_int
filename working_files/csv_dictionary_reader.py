import csv

with open("working_files/names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Iterate over each row in the CSV file using the csv_reader object and then print the email using the key of the dictionary
    for line in csv_reader:
        print(line["email"])
