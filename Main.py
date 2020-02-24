import numpy as np
from copy import deepcopy
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

        server = [[0 for x in range(self.numserver)] for x in range(self.numfile)]
        restriction = [[0 for x in range(self.numserver)] for x in range(self.numfile)]

        server, restriction = self.backtracking(server, restriction)

    def check(self, server, restriction, file, sux, suy, dependec):
        timetotal = 0
        targ = False
        totaldependecy = 0

        # Pick up the time deadline
        for x, sublist in enumerate(self.targets):
            for y, s in enumerate(sublist):
                if file in s:
                    targ = True
                    deadline = int(self.targets[x][1])
                    goalpoints = int(self.targets[x][2])
                    break
            else:
                continue
            break

        # Control if there is already the same file in the server
        for i in range(0, len(server)):
            if server[i][suy] == file:
                return False

        # Get the total time of the dipendency
        if sux != 0 or dependec[0] != 0:
            numdependecy = int(dependec.pop(0))
            for k in dependec:
                for i in range(0, sux):
                    for j in range(0, len(server[0])):
                        temp = server[i][j]
                        if server[i][j] == k:
                            for x, sublist in enumerate(self.file):
                                for y, s in enumerate(sublist):
                                    if k in s:
                                        timecompiler = int(self.file[x][1])
                                        timereplicate = int(self.file[x][2])
                                        break
                                else:
                                    continue
                                break
                            totaldependecy += 1
                            if j == suy:
                                timetotal += timecompiler
                            else:
                                timetotal += (timecompiler + timereplicate)

            if totaldependecy < numdependecy:
                return False
            if targ:
                if timetotal > deadline:
                    return False

            return True

    def finish(self, server):
        count = 0
        for i in range(0, len(server)):
            for j in range(0, len(server[0])):
                if server[i][j] != 0:
                    count += 1

        if count == self.numfile:
            return True
        else:
            return False

    def backtracking(self, server, restriction):
        dep = deepcopy(self.dependecy)
        #vedere come piazzare i file
        if self.finish(server):
            return server, restriction
        else:
            for i in range(0, len(server)):
                for j in range(0, len(server[0])):
                    if server[i][j] == 0:
                        sux = i
                        suy = j
                        break
                else:
                    continue
                break

            for x in range(0, self.numfile):
                if self.check(server, restriction, self.file[x][0], sux, suy, dep[x]):
                    server[sux][suy] = self.file[x][0]
                    self.backtracking(server, restriction)

            server[sux][suy] = 0


if __name__ == "__main__":
    data = pd.read_csv("./final_round_2019.in/a_example.in", header=None)
    Esamination(data)
