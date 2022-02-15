from Avatar import Avatar
from Game import Game

# Create four avatars
luigi = Avatar('Luigi', 'green', 'brown', "5'2", 'male', 'Vicious Vortex')
mario = Avatar('Mario', 'red', 'brown', "5'1", 'male', 'Fireballs')
wario = Avatar('Wario', 'yellow', 'brown', "5'9", 'male', 'Dash Attack')
waluigi = Avatar('Waluigi', 'purple', 'brown', "7'7", 'male', 'Drop Rocket')

# Animate one avatar
wario.animate_avatar()
# Change avatar superpower
wario.change_superpower('Disguise')
wario.change_haircolor('green')
# See superpower and haircolor is different
wario.animate_avatar()

# Instantiate game obj
game = Game()

# Add the avatars to game one at a time.
game.add_avatar(luigi)
game.add_avatar(mario)
game.add_avatar(wario)
game.add_avatar(waluigi)

# Create super_mario object by making it equal game()
super_mario = game

# Animate all avatars via super_mario object
super_mario.animate_all_avatars()

# Stop game and clear all_avatar list
game.stop_game()
# Animate will show no values other than game over
game.animate_all_avatars()
