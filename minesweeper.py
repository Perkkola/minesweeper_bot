import numpy as np
from utils import grid_to_index, index_to_grid
import sys
sys.setrecursionlimit(10000)

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
          self.game = None
          self.lost = False
          self.started = False

    def new_game(self, x, y):
        game = np.array([[Tile(a, b, 0) for b in range(self.height)] for a in range(self.width)])
        tiles = [z for z in range(self.height*self.width)]

        if self.bombs <= self.height*self.width - 9:
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i >= 0 and j >= 0 and i < self.width and j < self.height:
                        ind = grid_to_index(i, j, self.width)
                        tiles.remove(ind)
        else:
            ind = grid_to_index(x, y, self.width)
            tiles.remove(ind)

        bomb_tiles = np.random.choice(tiles, self.bombs, replace=False)
        self.bombas = []

        for bt in bomb_tiles:
            x, y = index_to_grid(bt, self.width)
            game[x][y].type = 9
            self.bombas.append((x, y, 9))

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    if i >= 0 and j >= 0 and i < self.width and j < self.height and game[i][j].type != 9:
                        game[i][j].type += 1

        self.game = game

    def get_tile(self, x, y):
        tile = self.game[x][y]

        if tile.hidden: return 0

        return tile.type

    def reveal_tile(self, x, y, revealed = None):
        if not self.started:
            self.new_game(x, y)
            self.started = True

        if x < 0 or y < 0 or x >= self.width or y >= self.height or not self.game[x][y].hidden: return


        tile = self.game[x][y]

        if revealed == None:
            revealed = []
        
        revealed.append((x, y, tile.type))
        if tile.type == 0:
            tile.hidden = False
            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    self.reveal_tile(i, j, revealed)

        tile.hidden = False

        if tile.type == 9:
            self.lost = True
            revealed.extend(self.bombas)
        
        return revealed
    
    def __repr__(self):
         return str(self.game)
         