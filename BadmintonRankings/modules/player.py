class Player:
    def __init__(self, name, id, wins, losses, rating):
        self.name = name
        self.id = id
        self.wins = wins
        self.losses = losses
        self.rating = rating

    def update_ranking(self, new_rating):
        self.rating = new_rating

    def __str__(self):
        return f"Player(name={self.name}, id={self.id}, wins={self.wins}, losses={self.losses}, rating={self.rating})"

