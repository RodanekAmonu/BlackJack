import game_of_life as game
import dataLoader as Loader
#
# set=[5,6,7,26,27,45,47]
# g = game.GameMap(5,[5,12,17,22,14,6])
# # g = game.GameMap(20,set)
# for i in range(20):
#     print(g)
#     # print(g.living_neighbors_list())
#     g = g.map_update()
#     print('..............................')
loader = Loader.loader()
# print(loader.loadertype)
# print(loader.size)
# print(loader.initdata)

g = game.GameMap(loader.size, loader.initdata)

for i in range(20):
    print(g)
    # print(g.living_neighbors_list())
    g = g.map_update()
    print('..............................')
