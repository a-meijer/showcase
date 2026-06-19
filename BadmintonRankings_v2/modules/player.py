class Player:
    def __init__(self, name, id, wins, losses, rating, rank, highestRank, previousRank, highestRating, previousRating, latestTournament, ratingConfidence):
        self.name = name
        self.id = id
        self.wins = wins
        self.losses = losses
        self.rating = rating
        self.highestRating = highestRating
        self.previousAnnualRating = previousRating
        self.previousAnnualRank = previousRank
        self.rank = rank
        self.highestRank = highestRank
        self.matchHistory = []
        self.titles = []
        self.latestTournament = latestTournament
        self.ratingConfidence = ratingConfidence

    def update_confidence(self):
        if(self.wins + self.losses < 10):
            self.ratingConfidence = 100
        elif(self.wins + self.losses < 25):
            self.ratingConfidence = 50
        elif(self.wins + self.losses < 50):
            self.ratingConfidence = 25
        else:
            self.ratingConfidence = 10
        return self.ratingConfidence
        
    def winrate(self):
        total_matches = self.wins + self.losses
        if total_matches == 0:
            return 0.0
        return self.wins / total_matches

    def __str__(self):
        return f"Player(name={self.name}, id={self.id}, wins={self.wins}, losses={self.losses}, rating={self.rating})"

