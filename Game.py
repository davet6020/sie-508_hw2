from Object import Object
from pprint import pprint
avatars = []

class Game:

  def __init__(self):
    self.avatars = Object()

  # Initialize an internal empty list of objects
  def start_game(self):
    self.avatars = avatars

  # Add one avatar at a time to the avatars object
  def add_avatar(self, name, avatar):
    avatars.append(avatar)
    self.avatars.name = name

  def animate_all_avatars(self):
    self.avatars = avatars

    for avatar in self.avatars:
      print('Name:{}  Hat:{}  Haircolor:{}  Height:{}  Gender:{}  Superpower:{}'.format(
        avatar.name, avatar.hat, avatar.haircolor, str(avatar.height),
        avatar.gender, avatar.superpower))

  def remove_all_avatars(self):
    pass

  def stop_game(self):
    avatars.clear()
    self.avatars = avatars
