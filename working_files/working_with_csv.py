import csv

# Open the CSV file "names.csv" in read mode
# The "with" statement ensures proper closing of the file after its use
with open("working_files/names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Iterate over each row in the CSV file using the csv_reader object and then print each one
    for line in csv_reader:
        print(line)

