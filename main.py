from Avatar import Avatar
from Game import Game
from Object import Object
from pprint import pprint


# Create four avatars
luigi = Avatar('Luigi', 'green', 'brown', 5, 'male', 'Vicious Vortex')
mario = Avatar('Mario', 'red', 'brown', 5, 'male', 'Fireballs')
wario = Avatar('Wario', 'yellow', 'brown', 5, 'male', 'Dash Attack')
waluigi = Avatar('Waluigi', 'purple', 'brown', 5, 'male', 'Drop Rocket')

# Create super_mario object and append the four avatars to it
super_mario = Object()
super_mario.luigi = luigi
super_mario.mario = mario
super_mario.wario = wario
super_mario.waluigi = waluigi

game = Game()
game.add_avatar('luigi', luigi)
game.add_avatar('wario', wario)
game.animate_all_avatars()

game.stop_game()
