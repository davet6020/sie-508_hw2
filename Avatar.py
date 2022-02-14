class Avatar:
  def __init__(self, name, hat, haircolor, height, gender, superpower):
    self.name = name
    self.hat = hat
    self.haircolor = haircolor
    self.height = height
    self.gender = gender
    self.superpower = superpower

  def change_superpower(self, superpower):
    self.superpower = superpower

  def animate_avatar(self):
    print('Name:{}  Hat:{}  Haircolor:{}  Height:{}  Gender:{}  Superpower:{}'.format(self.name, self.hat, self.haircolor, str(self.height), self.gender, self.superpower))
