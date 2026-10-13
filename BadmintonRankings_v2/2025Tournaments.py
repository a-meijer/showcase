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
    directory = "data/2025/players/"
    
    ''' Hardcoded matches '''
    # Add these in the correct chronological order
    # See Tournaments/2023/_TOURNAMENT_LIST.txt for order of tournaments

    matchfiles = []
    tnames = []
    tdates = []

    # Kelowna Open 
    matchfiles.append("Tournaments/2025/2025_KelownaOpen.csv")
    tnames.append("2025 Kelowna Open")
    tdates.append("2025-01-03")

    # Campbell River Open 
    matchfiles.append("Tournaments/2025/2025_CRBC.csv")
    tnames.append("2025 Campbell River Open")
    tdates.append("2025-01-10")

    # Jack Underhill
    matchfiles.append("Tournaments/2025/2025_JackUnderhill.csv")
    tnames.append("2025 Jack Underhill")
    tdates.append("2025-02-07")

    # Provincial Championships
    matchfiles.append("Tournaments/2025/2025_Provincials.csv")
    tnames.append("2025 Provincial Championships")
    tdates.append("2025-04-04")

    # Easter Open
    matchfiles.append("Tournaments/2025/2025_EasterOpen.csv")
    tnames.append("2025 Easter Open")
    tdates.append("2025-04-18")

    # VRC Club Championships
    matchfiles.append("Tournaments/2025/2025_VRCClosed.csv")
    tnames.append("2025 VRC Club Championships")
    tdates.append("2025-04-21")

    # Victoria Closed
    matchfiles.append("Tournaments/2025/2025_VictoriaClosed.csv")
    tnames.append("2025 Victoria Closed")
    tdates.append("2025-06-06")

    # Whiterock Tournament
    matchfiles.append("Tournaments/2025/2025_WhiteRock.csv")
    tnames.append("2025 White Rock Tournament")
    tdates.append("2025-06-21")

    # Smash Champs Grand Opening
    matchfiles.append("Tournaments/2025/2025_SmashChamps.csv")
    tnames.append("2025 Smash Champs Grand Opening")
    tdates.append("2025-08-02")

    # Nanaimo Open
    matchfiles.append("Tournaments/2025/2025_Nanaimo.csv")
    tnames.append("2025 Nanaimo Open")
    tdates.append("2025-10-03")
    
    # Thanksgiving Tournament
    matchfiles.append("Tournaments/2025/2025_Thanksgiving.csv")
    tnames.append("2025 Thanksgiving Tournament")
    tdates.append("2025-10-11")

    # Island Open
    matchfiles.append("Tournaments/2025/2025_IslandOpen.csv")
    tnames.append("2025 Island Open")
    tdates.append("2025-11-14")

    # Kelowna Fall Open
    matchfiles.append("Tournaments/2025/2025_KelownaFall.csv")
    tnames.append("2025 Kelowna Fall Open")
    tdates.append("2025-11-21")

    # Surrey Open
    matchfiles.append("Tournaments/2025/2025_SurreyOpen.csv")
    tnames.append("2025 Surrey Open")
    tdates.append("2025-11-29")

    # Boxing Week Tournament
    matchfiles.append("Tournaments/2025/2025_BoxingWeek.csv")
    tnames.append("2025 Boxing Week Tournament")
    tdates.append("2025-12-26")

    processTournaments.run(matchlist, savestate, tdata, directory, matchfiles, tnames, tdates, "2025")

    print("2025 match processing complete.")
    return

PROCESS_TOURNAMENTS()