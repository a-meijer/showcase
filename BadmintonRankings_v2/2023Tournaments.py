# Hardcode everything to bypass user input and test on all tournament data at once

import os
from modules import io as myio
from modules import loadPlayers as playerLoader
from modules import saveSystem as saveSystem
from modules import matches as matches
from modules import player as player
from modules import saveSystem as saveSystem
from modules import processTournaments as processTournaments

def PROCESS_2023_TOURNAMENTS():

    # Set matchlist path
    matchlist = "data/matchlist.csv"

    # Set ranking path
    savestate = "data/output.csv"

    # Set datafile path
    tdata = "data/tdata.csv"
    directory = "data/2023/players/"
    
    ''' Hardcoded matches '''
    # Add these in the correct chronological order
    # See Tournaments/2023/_TOURNAMENT_LIST.txt for order of tournaments

    matchfiles = []
    tnames = []
    tdates = []

    # New Year's Tournament 
    matchfiles.append("Tournaments/2023/2023_C1NY.csv")
    tnames.append("2023 New Year's Tournament")
    tdates.append("2023-01-01")
    # BC Senior Elite
    matchfiles.append("Tournaments/2023/2023_SeniorElite.csv")
    tnames.append("2022-2023 BC Senior Elite")
    tdates.append("2023-01-06")
    # Campbell River
    matchfiles.append("Tournaments/2023/2023_CRBC.csv")
    tnames.append("2023 Campbell River")
    tdates.append("2023-01-13")
    # Kelowna Adult Open
    matchfiles.append("Tournaments/2023/2023_KelownaAdult.csv")
    tnames.append("2023 Kelowna Adult Open")
    tdates.append("2023-01-15")
    # Wing's-GHS Tournament
    matchfiles.append("Tournaments/2023/2023_Wings.csv")
    tnames.append("2023 Wing's-GHS Tournament")
    tdates.append("2023-02-25")
    # Jack Underhill
    matchfiles.append("Tournaments/2023/2023_JackUnderhill.csv")
    tnames.append("2023 Jack Underhill")
    tdates.append("2023-03-31")
    # Easter Open
    matchfiles.append("Tournaments/2023/2023_EasterOpen.csv")
    tnames.append("2023 Easter Open")
    tdates.append("2023-04-07")
    # Provincial Championship
    matchfiles.append("Tournaments/2023/2023_Provincials.csv")
    tnames.append("2023 Provincials")
    tdates.append("2023-04-22")
    # 12.2 O-Go-PoCo Open
    matchfiles.append("Tournaments/2023/2023_OGoPoCo.csv")
    tnames.append("2023 OGo-PoCo B&Y Open")
    tdates.append("2023-05-26")
    # Victoria Closed
    matchfiles.append("Tournaments/2023/2023_VictoriaClosed.csv")
    tnames.append("2023 Victoria Closed")
    tdates.append("2023-06-02")
    # White Rock Tournament
    matchfiles.append("Tournaments/2023/2023_WhiteRock.csv")
    tnames.append("2023 White Rock Tournament")
    tdates.append("2023-06-23")
    # Nanaimo Open
    matchfiles.append("Tournaments/2023/2023_NanaimoOpen.csv")
    tnames.append("2023 Nanaimo Open")
    tdates.append("2023-09-22")
    # POCOmon GO Open
    matchfiles.append("Tournaments/2023/2023_POCOmonOpen.csv")
    tnames.append("2023 POCOmon GO Open")
    tdates.append("2023-09-23")
    # Thanksgiving Tournament
    matchfiles.append("Tournaments/2023/2023_Thanksgiving.csv")
    tnames.append("2023 C1 Thanksgiving Tournament")
    tdates.append("2023-10-07")
    # November BC Senior Elite
    matchfiles.append("Tournaments/2023/2023_NovSeniorElite.csv")
    tnames.append("2023-2024 BC Senior Elite")
    tdates.append("2023-11-17")
    # Island Open
    matchfiles.append("Tournaments/2023/2023_IslandOpen.csv")
    tnames.append("2023 Island Open")
    tdates.append("2023-11-24")
    # Kelowna Open
    matchfiles.append("Tournaments/2023/2023_KelownaOpen.csv")
    tnames.append("2023 Kelowna Open")
    tdates.append("2023-12-02")


    processTournaments.run(matchlist, savestate, tdata, directory, matchfiles, tnames, tdates, "2023")

    print("2023 match processing complete.")
    return

PROCESS_2023_TOURNAMENTS()