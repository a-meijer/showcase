from datetime import date

class Player:
    def __init__(self, name, id, wins, losses, rating, rank, highestRank, previousRank, highestRating, previousRating, latestTournament, RD):
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
        self.RD = RD

    # Given two player objects, return K value for self; K = 100*g(RD) 
    def glick(self, opponent, BASE_K, INITIAL_RD): 
        self_factor = self.RD / INITIAL_RD
        opp_factor = 1 / (1 + opponent.RD / INITIAL_RD)

        return BASE_K * self_factor * (1+opp_factor)

    def winrate(self):
        total_matches = self.wins + self.losses
        if total_matches == 0:
            return 0.0
        return self.wins / total_matches

    def __str__(self):
        return f"Player(name={self.name}, id={self.id}, wins={self.wins}, losses={self.losses}, rating={self.rating})"

