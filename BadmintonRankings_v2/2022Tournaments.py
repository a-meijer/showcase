# Hardcode everything to bypass user input and test on all tournament data at once

import os
from modules import io as myio
from modules import loadPlayers as playerLoader
from modules import saveSystem as saveSystem
from modules import matches as matches
from modules import player as player
from modules import saveSystem as saveSystem
from modules import processTournaments as processTournaments

def PROCESS_2022_TOURNAMENTS():
    
    # Set matchlist path
    matchlist = "data/matchlist.csv"

    # Set ranking output path
    savestate = "data/output.csv"

    # Set datafile paths
    tdata = "data/tdata.csv"
    directory = "data/2022/players/"

    ''' Hardcoded matches '''
    # Add these in the correct chronological order
    # See Tournaments/2023/_TOURNAMENT_LIST.txt for order of tournaments

    matchfiles = []
    tnames = []
    tdates = []
    
    # Campbell River
    matchfiles.append("Tournaments/2022/2022_CRBC.csv")
    tnames.append("2022 Campbell River")
    tdates.append("2022-03-11")

    # Victoria Closed
    matchfiles.append("Tournaments/2022/2022_VictoriaClosed.csv")
    tnames.append("2022 Victoria Closed")
    tdates.append("2022-05-06")

    # Provincial Championships
    matchfiles.append("Tournaments/2022/2022_Provincials.csv")
    tnames.append("2022 Provincial Championships")
    tdates.append("2022-05-27")

    # New Era Open
    matchfiles.append("Tournaments/2022/2022_NewEra.csv")
    tnames.append("2022 New Era Open")
    tdates.append("2022-08-05")

    # Nanaimo Open
    matchfiles.append("Tournaments/2022/2022_NanaimoOpen.csv")
    tnames.append("2022 Nanaimo Open")
    tdates.append("2022-10-08")

    # Thanksgiving Tournament
    matchfiles.append("Tournaments/2022/2022_Thanksgiving.csv")
    tnames.append("2022 C1 Thanksgiving Tournament")
    tdates.append("2022-10-08")

    # Island Open
    matchfiles.append("Tournaments/2022/2022_IslandOpen.csv")
    tnames.append("2022 Island Open")
    tdates.append("2022-11-19")

    processTournaments.run(matchlist, savestate, tdata, directory, matchfiles, tnames, tdates, "2022")

    print("2022 match processing complete.")
    return

PROCESS_2022_TOURNAMENTS()