import csv

input_filename = 'inputMatches.csv'
output_filename = 'inputRankings.csv'

unique_names = set()

# Open the CSV file
with open(input_filename, newline='') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Do something with the row data
        for element in row:
            unique_names.add(element.strip())

# Open/Create the output file  
with open(output_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for element in unique_names:
        writer.writerow([element, 1000])