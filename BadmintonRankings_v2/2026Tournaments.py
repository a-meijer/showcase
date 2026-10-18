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
    directory = "data/2026/players/"
    
    ''' Hardcoded matches '''
    # Add these in the correct chronological order
    # See Tournaments/2023/_TOURNAMENT_LIST.txt for order of tournaments

    matchfiles = []
    tnames = []
    tdates = []

    # Cindy Simpson Memorial
    matchfiles.append("Tournaments/2026_SUMMER/2026_CindySimpson.csv")
    tnames.append("2026 Cindy Simpson Memorial")
    tdates.append("2026-01-09")
    
    # Kelowna Winter Open
    matchfiles.append("Tournaments/2026_SUMMER/2026_KelownaWinter.csv")
    tnames.append("2026 Kelowna Winter Open")
    tdates.append("2026-01-23")

    # Jack Underhill
    matchfiles.append("Tournaments/2026_SUMMER/2026_JackUnderhill.csv")
    tnames.append("2026 Jack Underhill")
    tdates.append("2026-02-06")

    # Kamloops Open in Kelowna
    matchfiles.append("Tournaments/2026_SUMMER/2026_Kamloops.csv")
    tnames.append("2026 Kamloops Open in Kelowna")
    tdates.append("2026-03-20")

    # Easter Open
    matchfiles.append("Tournaments/2026_SUMMER/2026_EasterOpen.csv")
    tnames.append("2026 Easter Open")
    tdates.append("2026-04-03")
    
    # Provincial Championships
    matchfiles.append("Tournaments/2026_SUMMER/2026_Provincials.csv")
    tnames.append("2026 Provincial Championships")
    tdates.append("2026-04-10")

    # VRC Club Championships
    matchfiles.append("Tournaments/2026_SUMMER/2026_VRC.csv")
    tnames.append("2026 VRC Club Championships")
    tdates.append("2026-04-13")

    # Victoria Closed
    matchfiles.append("Tournaments/2026_SUMMER/2026_VictoriaClosed.csv")
    tnames.append("2026 Victoria Closed")
    tdates.append("2026-05-29")
    
    # Canada Winter Games Trial
    matchfiles.append("Tournaments/2026_SUMMER/2026_CWGT.csv")
    tnames.append("2026 Canada Winter Games Trial")
    tdates.append("2026-06-20")

    # White Rock Tournament
    matchfiles.append("Tournaments/2026_SUMMER/2026_WhiteRock.csv")
    tnames.append("2026 White Rock Tournament")
    tdates.append("2026-06-20")

    processTournaments.run(matchlist, savestate, tdata, directory, matchfiles, tnames, tdates, "2026")

    print("2026 match processing complete.")
    return

PROCESS_TOURNAMENTS()