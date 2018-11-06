import game_of_life as game

set=[5,6,7,26,27,45,47]
g = game.GameMap(5,[7,12,17])
# g = game.GameMap(20,set)
for i in range(10):
    print(g)
    print(g.living_neighbors_list())
    g = g.map_update()
    print('..............................')