class Avatar:

  def __init__(self, name, hat, haircolor, height, gender, superpower):
    self.name = name
    self.hat = hat
    self.haircolor = haircolor
    self.height = height
    self.gender = gender
    self.superpower = superpower

  # Change the current avatar superpower
  def change_superpower(self, superpower):
    self.superpower = superpower

  # Change the current avatar haircolor
  def change_haircolor(self, haircolor):
    self.haircolor = haircolor

  # Prints out the current avatar information
  def animate_avatar(self):
    print('Name:{}  Hat:{}  Haircolor:{}  Height:{}  Gender:{}  Superpower:{}'.format(
      self.name, self.hat, self.haircolor,
      str(self.height), self.gender, self.superpower))

  # Returns the current avatar name
  def av_name(self):
    return self.name

  # Returns the current avatar in list format
  def av_list(self):
    return list(self.__dict__.items())
