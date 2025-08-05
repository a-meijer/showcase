# Hardcode everything to bypass user input and test on all tournament data at once

import os
from modules import io as myio
from modules import createInitialRankings as cir
from modules import outputRankings as oir
from modules import matches as matches

# Initialize ranks dictionary
ranks = {}
# Set K constant
K = 100

def PROVINCIAL_RANKINGS():
    # Load initial players
    ranks = cir.loadNewPlayers(ranks, "Tournaments/2022_ProvincialChampionship/2022_ProvincialChampionship.csv")

    # Print initial rankings
    ranks = oir.sortRankings(ranks)
    print("Initial Rankings:")
    oir.outputRankingsToConsole(ranks)

    # Process matches
    ranks = matches.processMatches(ranks, K, "Tournaments/2022_ProvincialChampionship/2022_ProvincialChampionship.csv", "2022 Provincial Championship")
    ranks = oir.sortRankings(ranks)

    ranks = cir.loadNewPlayers(ranks, "Tournaments/2023_JackUnderhill/2023_JackUnderhill.csv")
    ranks = matches.processMatches(ranks, K, "Tournaments/2023_JackUnderhill/2023_JackUnderhill.csv", "2023 Jack Underhill")
    ranks = oir.sortRankings(ranks)

    ranks = cir.loadNewPlayers(ranks, "Tournaments/2023_ProvincialChampionship/2023_ProvincialChampionship.csv")
    ranks = matches.processMatches(ranks, K, "Tournaments/2023_ProvincialChampionship/2023_ProvincialChampionship.csv", "2023 Provincial Championship")
    ranks = oir.sortRankings(ranks)

    ranks = cir.loadNewPlayers(ranks, "Tournaments/2024_JackUnderhill/2024_JackUnderhill.csv")
    ranks = matches.processMatches(ranks, K, "Tournaments/2024_JackUnderhill/2024_JackUnderhill.csv", "2024 Jack Underhill")
    ranks = oir.sortRankings(ranks)

    ranks = cir.loadNewPlayers(ranks, "Tournaments/2024_ProvincialChampionship/2024_ProvincialChampionship.csv")
    ranks = matches.processMatches(ranks, K, "Tournaments/2024_ProvincialChampionship/2024_ProvincialChampionship.csv", "2024 Provincial Championship")
    ranks = oir.sortRankings(ranks)

    ranks = cir.loadNewPlayers(ranks, "Tournaments/2024_WingsOpen/2024_WingsOpen.csv")
    ranks = matches.processMatches(ranks, K, "Tournaments/2024_WingsOpen/2024_WingsOpen.csv", "2024 Wings Open")
    ranks = oir.sortRankings(ranks)

    ranks = cir.loadNewPlayers(ranks, "Tournaments/2024_ShuttlesportOpen/2024_ShuttlesportOpen.csv")
    ranks = matches.processMatches(ranks, K, "Tournaments/2024_ShuttlesportOpen/2024_ShuttlesportOpen.csv", "2024 Shuttlesport Open")
    ranks = oir.sortRankings(ranks)

    ranks = cir.loadNewPlayers(ranks, "Tournaments/2025_JackUnderhill/2025_JackUnderhill.csv")
    ranks = matches.processMatches(ranks, K, "Tournaments/2025_JackUnderhill/2025_JackUnderhill.csv", "2025 Jack Underhill")
    ranks = oir.sortRankings(ranks)

    ranks = cir.loadNewPlayers(ranks, "Tournaments/2025_ProvincialChampionship/2025_ProvincialChampionship.csv")
    ranks = matches.processMatches(ranks, K, "Tournaments/2025_ProvincialChampionship/2025_ProvincialChampionship.csv", "2025 Provincial Championship")
    ranks = oir.sortRankings(ranks)

    # Output final rankings
    print("Final Rankings:")
    oir.outputRankingsToConsole(ranks)
    # Output to CSV
    print(f"Outputting final rankings to output.csv...")
    oir.outputRankingsToCSV(ranks, "output.csv")
    print(f"Final rankings have been saved to output.csv.\n")

    return

def ISLAND_RANKINGS():

    # Pending data for Island tournaments:
    # 2022 Campbell River Open
    # Nanaimo Open
    # Victoria Closed
    # Island Open

    return