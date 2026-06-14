# Functions for the IO to select the required input and output CSV files for the algorithm

import os

#
def welcome():
    # Welcome
    print("\nWelcome to the Badminton Rankings System!")
    print("This program will process a tournament and update the player ratings.\n")
    return
    
#
def get_input_filename():
    gotInputFile = False
    inputFile = "Ratings.csv"
    # Get input filename
    print(f"The default input file is {inputFile}. Would you like to use this file? (y/n)")
    useDefaultInput = input().strip().lower() == 'y'
    if useDefaultInput:
        # Check if a file exists at inputFile
        if  not os.path.exists(inputFile):
            print(f"ERROR: The default input file {inputFile} does not exist.")
            print(f"Are you starting a new rating system with {inputFile}? (y/n)")
            newRatingSystem = input().strip().lower() == 'y'
            if newRatingSystem:
                gotInputFile = True
                open(inputFile, 'w').close()  # Create a blank input file
                print(f"Created blank input file {inputFile}.\n")
            else:
                print("Exit the program? (y/n)")
                exitProgram = input().strip().lower() == 'y'
                if exitProgram:
                    print("Exiting the program.\n")
                    exit()
        else:
            gotInputFile = True
            # Check inputFile
            print(f"Selected input file {inputFile}.\n")
    else:
        while(not gotInputFile):
            print("Please enter the path to the input file:")
            inputFile = input().strip()
            # Check if a file exists at inputFile
            if  not os.path.exists(inputFile):
                print(f"WARNING: The input file {inputFile} does not exist.")
                print("Exit the program? (y/n)")
                exitProgram = input().strip().lower() == 'y'
                if exitProgram:
                    print("Exiting the program.\n")
                    exit()
            else:
                gotInputFile = True
                print(f"Selected input file {inputFile}.\n")
    return inputFile

#
def get_output_filename():
    gotOutputFile = False
    outputFile = "outputRatings.csv"
    # Get output filename
    print("The default output file is outputRatings.csv. Would you like to use this file? (y/n)")
    useDefaultOutput = input().strip().lower() == 'y'
    if useDefaultOutput:
        # Check if a file exists at outputFile
        if os.path.exists(outputFile):
            print(f"WARNING: The default output file {outputFile} already exist.")
            print("Overwrite the output file? (y/n)")
            overwrite = input().strip().lower() == 'y'
            if overwrite:
                gotOutputFile = True
                print(f"Selected output file {outputFile}.\n")
        else:
            gotOutputFile = True
            print(f"Selected output file {outputFile}.\n")
    else:
        while( not gotOutputFile ):
            print("Please enter the path to a different output file:")
            outputFile = input().strip()
            if os.path.exists(outputFile):
                print(f"WARNING: The default output file {outputFile} already exist.")
                print("Overwrite the output file? (y/n)")
                overwrite = input().strip().lower() == 'y'
                if overwrite:
                    gotOutputFile = True
                    print(f"Selected output file {outputFile}.\n")
            else:
                gotOutputFile = True
                print(f"Selected output file {outputFile}.\n")
    return outputFile

#
def get_tournament_filename():
    gotTournamentFile = False
    tournamentFile = "Tournaments/2022_ProvincialChampionship/2022_ProvincialChampionship.csv"
    # Get tournament filename
    print("Would you like to use the default tournament file? (y/n)")
    newRatingSystem = input().strip().lower() == 'y'
    if newRatingSystem:
        print("Using default initial tournament file: Tournaments/2022_ProvincialChampionship/2022_ProvincialChampionship.csv")
        print("Default tournament name: 2022 Provincial")
        tournamentName = "2022 Provincial"
        # Check if a file exists at inputFile
        if  not os.path.exists(tournamentFile):
            print(f"ERROR: The tournament file {tournamentFile} does not exist.")
            print("Exit the program? (y/n)")
            exitProgram = input().strip().lower() == 'y'
            if exitProgram:
                print("Exiting the program.\n")
                exit()
        else:
            gotTournamentFile = True
            # Check inputFile
            print(f"Selected tournament file {tournamentFile}.\n")
    else:
        while( not gotTournamentFile ):
            print("Please enter the path to the tournament file:")
            tournamentFile = input().strip()
            # Check if a file exists at tournamentFile
            if not os.path.exists(tournamentFile):
                print(f"ERROR: The tournament file {tournamentFile} does not exist.")
                print("Exit the program? (y/n)")
                exitProgram = input().strip().lower() == 'y'
                if exitProgram:
                    print("Exiting the program.\n")
                    exit()
            else:
                gotTournamentFile = True
                # Check tournamentFile
                print(f"Selected tournament file {tournamentFile}.\n")
        # Get tournament name
        tournamentName = input("Enter the tournament name: ").strip()
    return tournamentFile, tournamentName
