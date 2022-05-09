# NAME: Alphabetizer.rb
# DATE: May 8, 2022 - Created
#       May 8, 2022 - added I/O to input filenames; saved to repository.
# AUTH: Andrew Meijer, ATRM
# The purpose of this program is to alphabetize the lines of a text file and output the result to a new text file.

# Get the name of the file to alphabetize using CLI
puts "Enter the name of the file to alphabetize:"
filename = gets.chomp

# filename for the new file being created
ofn = filename + "_alph"

# Print to console
filename = filename + ".txt"
ofn = ofn + ".txt"
puts "inputting from file: " + filename
puts "outputting to file: " + ofn

#inFile = File.new(filename, "r")
#outFile = File.new(filename"w")

#inFile.close
#outFile.close