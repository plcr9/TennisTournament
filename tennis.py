class Player:
  def __init__(self, name-"", ranking_points=0):
    self.name = name
    self.ranking_points = ranking_points

  def update_ranking_points(self, points_change):
    self.ranking_points += points_change

class Match:
  def __init__(
    self,
    player_1=Player(),
    player_2=Player(),
    best_of_5=True,
  ):
    self.players = (player_1, player_2)
    self.best_of_5 = best_of_5
    self.sets_to_play = 5 if best_of_5 else 3
  
