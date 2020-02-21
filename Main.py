import numpy as np
import pandas as pd

class Esamination:
    def __init__(self, data):
        info = data.iloc[0, 0].split()
        self.numfile = int(info[0])
        self.numtarget = int(info[1])
        self.numserver = int(info[2])
        self.file = []
        self.dependecy = []
        self.targets = []
        for i in range(1, self.numfile * 2, 2):
            self.file.append(data.iloc[i, 0].split())
            self.dependecy.append(data.iloc[i + 1, 0].split())
        for i in range((self.numfile * 2) + 1, (self.numfile * 2) + 1 + self.numtarget):
            self.targets.append(data.iloc[i, 0].split())

        server = np.matrix([[0 for x in range(self.numserver)] for x in range(self.numfile)])
        restriction = np.matrix([[0 for x in range(self.numserver)] for x in range(self.numfile)])

        server, restriction = self.backtracking(server, restriction)

    def check(self, server, restriction, file, sux, dependecy):
        dep = False
        if sux != 0 and dependecy[0][0] != 0:
            for i in range(0, sux, -1):
                for j in range(0, len(server)):
                    if server[i][j] == file:
                        dep = True

        if file in self.targets:
            ind = self.file.index(file)

    def finish(self, server):
        temp = 0
        return False

    def backtracking(self, server, restriction):
        if self.finish(server):
            return server, restriction
        else:
            for i in range(0, len(server)):
                for j in range(0, len(server[0])):
                    if server[i, j] == 0:
                        sux = i
                        suy = j
                        break
                else:
                    continue
                break

            for x in range(0, self.numfile):
                if self.check(server, restriction, self.file[x][0], sux, self.dependecy[x]):
                    server[sux, suy] = self.file[x][0]


if __name__ == "__main__":
    data = pd.read_csv("./final_round_2019.in/a_example.in", header=None)
    Esamination(data)
