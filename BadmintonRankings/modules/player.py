class Player:
    def __init__(self, name, id, wins, losses, rating, rank, highestRank, previousRank, highestRating, previousRating):
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

    def update_ranking(self, new_rating):
        self.rating = new_rating
        if new_rating > self.highestRating:
            self.highestRating = new_rating

    def winrate(self):
        total_matches = self.wins + self.losses
        if total_matches == 0:
            return 0.0
        return self.wins / total_matches

    def __str__(self):
        return f"Player(name={self.name}, id={self.id}, wins={self.wins}, losses={self.losses}, rating={self.rating})"

