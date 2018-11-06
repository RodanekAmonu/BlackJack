class Cell():

    def __init__(self, pos_x=0, pos_y=0, status=False):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.status = status
        self.old_status = status

    def update(self, live_neighbors):
        self.old_status=self.status
        if live_neighbors > 3 or live_neighbors < 2:
            self.status = False
        elif live_neighbors == 3:
            self.status = True

    def __repr__(self):
        return bool(self.status)

    def __str__(self):
        if self.status:
            return 'O'
        else:
            return '.'


class GameMap():

    def __init__(self, size=20, live_set=[1,3,5,22,24,26]):
        self.size = size
        self.game_map = []
        for i in range(size):
            for j in range(size):
                self.game_map.append(Cell(i,j,False))
        # self.size=size
        for i in range(len(self.game_map)):

                for j in live_set :
                        if i == j:
                            self.game_map[i].status = True


    def __repr__(self):
        return self.game_map

    def __str__(self):
        r = ''
        for i in range(len(self.game_map)):
            if i % self.size == 0:
                r += '\r\n'
            r += str(self.game_map[i])
        return r

    def living_neighbors_list(self):
        living_cells = []
        ret = []
        for i in range(self.size*self.size):
            living_cells.append(0)
            ret.append(0)
        start = self.size + 1
        stop = len(self.game_map) - self.size - 1
        for i in range(start, stop, 1):
            if self.game_map[i].status:
                living_cells[i - 1 - self.size] += 1
                living_cells[i - 1] += 1
                living_cells[i - 1 + self.size] += 1
                living_cells[i - self.size] += 1
                living_cells[i + self.size] += 1
                living_cells[i + 1 - self.size] += 1
                living_cells[i + 1] += 1
                living_cells[i + 1 + self.size] += 1
        return living_cells

    def map_update(self):
        l = self.living_neighbors_list()
        for i in range(len(l)):
            self.game_map[i].update(l[i])

        return self



