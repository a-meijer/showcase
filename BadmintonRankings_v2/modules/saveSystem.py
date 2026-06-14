import csv

class SaveSystem:
    def __init__(self, matchlist, savestate, tdata):
        self.matchlist = matchlist
        self.savestate = savestate
        self.tdata = tdata
        self.matchesPlayed = 0
        self.numberPlayers = 0

    def save(self):
        with open(self.tdata, 'w', newline='') as file:
            csv_writer = csv.writer(file) 
            csv_writer.writerow([self.matchesPlayed, self.numberPlayers])
        return
    
    def load(self):
        with open(self.tdata, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                self.matchesPlayed = int(row[0])
                self.numberPlayers = int(row[1])
        return