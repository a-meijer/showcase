# Hardcode everything to bypass user input and test on all tournament data at once

import os
from modules import io as myio
from modules import loadPlayers as playerLoader
from modules import saveSystem as saveSystem
from modules import matches as matches
from modules import player as player
from modules import saveSystem as saveSystem
from modules import processTournaments as processTournaments

def PROCESS_TOURNAMENTS():

    # Set matchlist path
    matchlist = "data/matchlist.csv"

    # Set ranking path
    savestate = "data/output.csv"

    # Set datafile path
    tdata = "data/tdata.csv"
    directory = "data/2024/players/"
    
    ''' Hardcoded matches '''
    # Add these in the correct chronological order
    # See Tournaments/2023/_TOURNAMENT_LIST.txt for order of tournaments

    matchfiles = []
    tnames = []
    tdates = []

    # New Year's Tournament 
    matchfiles.append("Tournaments/2024/2024_C1NY.csv")
    tnames.append("2024 New Year's Tournament")
    tdates.append("2024-01-01")

    # Campbell River
    matchfiles.append("Tournaments/2024/2024_CRBC.csv")
    tnames.append("2024 Campbell River")
    tdates.append("2024-01-12")

    # Canadian Senior Championships
    matchfiles.append("Tournaments/2024/2024_Nationals.csv")
    tnames.append("2024 National Championships")
    tdates.append("2024-01-31")
    
    # Jack Underhill
    matchfiles.append("Tournaments/2024/2024_JackUnderhill.csv")
    tnames.append("2024 Jack Underhill")
    tdates.append("2023-02-17")

    # Easter Open
    matchfiles.append("Tournaments/2024/2024_EasterOpen.csv")
    tnames.append("2024 Easter Open")
    tdates.append("2024-03-29")

    # Sunshine Tournament
    matchfiles.append("Tournaments/2024/2024_Sunshine.csv")
    tnames.append("2024 Sunshine Tournament")
    tdates.append("2024-04-19")

    # Provincial Championship
    matchfiles.append("Tournaments/2024/2024_Provincials.csv")
    tnames.append("2024 Provincials")
    tdates.append("2024-04-26")

    # Victoria Closed
    matchfiles.append("Tournaments/2024/2024_VictoriaClosed.csv")
    tnames.append("2024 Victoria Closed")
    tdates.append("2024-05-24")

    # White Rock Tournament
    matchfiles.append("Tournaments/2024/2024_WhiteRock.csv")
    tnames.append("2024 White Rock Tournament")
    tdates.append("2024-06-22")

    # Nanaimo Open
    matchfiles.append("Tournaments/2024/2024_Nanaimo.csv")
    tnames.append("2024 Nanaimo Open")
    tdates.append("2024-09-27")

    # Thanksgiving Tournament
    matchfiles.append("Tournaments/2024/2024_Thanksgiving.csv")
    tnames.append("2024 C1 Thanksgiving Tournament")
    tdates.append("2024-10-12")

    # Island Open
    matchfiles.append("Tournaments/2024/2024_IslandOpen.csv")
    tnames.append("2024 Island Open")
    tdates.append("2024-11-15")

    # Wing's-GHS Tournament
    matchfiles.append("Tournaments/2024/2024_Wings.csv")
    tnames.append("2024 Wing's Open")
    tdates.append("2024-11-29")

    # Shuttlesport Open
    matchfiles.append("Tournaments/2024/2024_Shuttlesport.csv")
    tnames.append("2024 Shuttlesport Open")
    tdates.append("2024-12-12")

    # Boxing Week Tournament
    matchfiles.append("Tournaments/2024/2024_BoxingWeek.csv")
    tnames.append("2024 Boxing Week Tournament")
    tdates.append("2024-12-27")



    processTournaments.run(matchlist, savestate, tdata, directory, matchfiles, tnames, tdates, "2023")

    print("2024 match processing complete.")
    return

PROCESS_TOURNAMENTS()