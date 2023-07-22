class Player:
  def __init__(self, name-"", ranking_points=0):
    self.name = name
    self.ranking_points = ranking_points

  def update_ranking_points(self, points_change):
    self.ranking_points += points_change

  def __str__(self):
    return self.name

  def __repr__(self):
    return (
      f"Player(name='{self.name}',"
      f"ranking_points={self.ranking_points})"
    )

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
  
class Set:
  def __init__(self, match: Match, set_number=0):
    self.match = match
    self.set_number = set_number

class Game:
  points = 0, 15, 30, 40, "Ad"
  
  def __init__(self, set: Set, game_number=0):
    self.set = set
    self.game_number = game_number
    self.players = self.set.match.players
    self.score = {
      self.players[0]: 0,
      self.players[1]: 0,
    }
    self.winner = None

  def score_point(self, player: Player):
    if self.winner:
      print(
        "Error: You tried to add a point to a completed game!"
      )
      return
    game_won = False
    
    current_point = self.score[player]

    if self.score[player] == 40:
      if "Ad" in self.score.values():
        for each_player in self.players:
          self.score[each_player] = 40
      elif list(self.score.values()) == [40, 40]:
        self.score[player] = "Ad"
      else:
        game_won = True
    elif self.score[player] == "Ad":
      game_won = True
    else:
      self.score[player] = Game.points[
        Game.points.index(current_point) + 1
      ]
      
    
    if game_won:
      self.score[player] = "Game"
      self.winner = player

  def __str__(self):
    score_values = list(self.score.values())
    return f"{score_values[0]} - {score_values[1]}"

  def __repr__(self):
    return (
      f"Game(set={self.set!r}, "
      f"game_number={self.game_number})"
    )
