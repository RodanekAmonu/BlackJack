class loader():
    def __init__(self,path='input.txt'):
        self.loadertype=''
        self.size=0
        self.initdata=[]
        try:
            f = open(path, 'r')
        except FileNotFoundError as e:
            print('file: {} not found'.format(path))
            print(e)
        self.data = ''
        self.data += f.read()
        f.close()
        positions = self.important_positioins()

        self.loadertype=self.data[positions[0]+1:positions[1]]
        self.size = int(self.data[positions[2] + 1:positions[3]])

        inidat = self.data[positions[4] + 1:positions[5]]
        inidat = inidat.split(',')
        inidat[0] = inidat[0][1:]
        inidat[-1] = inidat[-1][:-1]
        for i in range(len(inidat)):
            self.initdata.append(int(inidat[i]))

    def important_positioins(self):
        ret = []
        for i in range(len(self.data)):
            c = self.data[i]
            if c == '=' or c == '\n':
                ret.append(i)
        return ret
#Wczytywanie danych z pliku