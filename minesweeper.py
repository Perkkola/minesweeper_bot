import numpy as np
from enum import Enum

from utils import grid_to_index, index_to_grid


class Tile():
    def __init__(self, x, y, tile_type):
        self.x = x
        self.y = y
        self.type = tile_type
        self.hidden = True

    def __repr__(self):
        return str(self.type)
    
class Game():
    def __init__(self, height, width, bombs):
          self.height = height
          self.width = width
          self.bombs = bombs
          self.lost = False
          self.game = None

    def new_game(self):
        game = np.array([[Tile(x, y, 0) for y in range(self.height)] for x in range(self.width)])
        bomb_tiles = np.random.choice(self.height*self.width, self.bombs, replace=False) #To start from blank, remove 3x3 grid around starting position

        for bt in bomb_tiles:
            x, y = index_to_grid(bt, self.width)
            game[x][y].type = 9

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i >= 0 and j >= 0 and i < self.width and j < self.height and game[i][j].type != 9:
                        game[i][j].type += 1

        self.game = game

    def reveal_tile(self, x, y):
         tile = self.game[x][y]
         tile.hidden = False

         print(tile.type)

         if tile.type == 9:
              print("Mine :(")
              self.lost = True

    def __repr__(self):
         return str(self.game)
         
game = Game(6, 5, 10)
game.new_game()
print(game)

while(True):
     x, y = input("tile")
     if int(x) == -1: exit()

     game.reveal_tile(int(x), int(y))