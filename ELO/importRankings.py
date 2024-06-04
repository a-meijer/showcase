import csv

# Open the CSV file
with open('inputRankings.csv', newline='') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Do something with the row data
        print(row)
        # Print each element of the row
        for element in row:
            print(element)
