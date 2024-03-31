import csv

# Open the CSV file "data.csv" in read mode
with open("data.csv", "r") as csv_file:
    # Create a csv.DictReader object, specifying the fieldnames as the first row of the CSV file
    csv_reader = csv.DictReader(csv_file)

    # Iterate over each row in the CSV file using the csv.DictReader object
    for row in csv_reader:
        # Each row is represented as a dictionary where keys are column headers
        # Print the values of each column for the current row
        print(row["name"], row["age"], row["country"])


# Writing
        

data = [
    {"name": "John", "age": 25, "country": "USA"},
    {"name": "Alice", "age": 30, "country": "UK"},
    {"name": "Bob", "age": 28, "country": "Canada"}
]


# Define the fieldnames (column headers)
fieldnames = ["name", "age", "country"]

# Specify the name of the CSV file to write to
csv_file_name = "output.csv"

# Write the data to the CSV file
with open(csv_file_name, "w", newline="") as csv_file2:
    # Create a csv.DictWriter object, specifying the fieldnames and the output file
    csv_writer = csv.DictWriter(csv_file2, fieldnames=fieldnames)

    # Write the header (field names) to the CSV file
    csv_writer.writeheader()

    # Write each row of data to the CSV file
    for row in data:
        csv_writer.writerow(row)

print(f"Data has been written to '{csv_file_name}' successfully.")

