import csv

# Open the CSV file "names.csv" in read mode
# The "with" statement ensures proper closing of the file after its use
with open("working_files/names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # Iterate over each row in the CSV file using the csv_reader object and then print each one
    for line in csv_reader:
        print(line)


    # Reset the file pointer to the beginning of the file
    csv_file.seek(0)

    # Making a copy of the file in a new one
        
    with open("new_names.csv", "w") as new_file:
        csv_writer = csv.writer(new_file)

        for line in csv_reader:
            csv_writer.writerow(line)

