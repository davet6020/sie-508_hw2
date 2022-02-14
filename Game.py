class Game:
  all_avatars = {}

  def __init__(self):
    self.one_avatar = None

  # Initialize an internal empty list of objects
  def start_game(self):
    self.all_avatars = self.all_avatars

  # Add one avatar at a time to the avatars object
  def add_avatar(self, one_avatar):
    self.one_avatar = one_avatar
    # Get the keys/values from one_avatar and put them into list d
    d = [self.one_avatar.av_list()]
    # add name of one_avatar as key and d as value
    self.all_avatars[self.one_avatar.av_name()] = d

  # Print out all current game avatars
  def animate_all_avatars(self):
    if self.all_avatars:
      print('--- All Game Avatars ---')
      for key, val in self.all_avatars.items():
        for av in val:
          print("".join(map(str, av)))
    else:
      print('--- Game Over ---')

  # When game is stopped, clear the internal list of avatars
  def stop_game(self):
    self.all_avatars.clear()
