class DFSUnlimited:
    def __init__(self, initial_state, actions, result, goal_test):
        self.f = []
        self.e = []
        self.res = []
        self.res2 = []
        self.visited = []
        self.initial_state = initial_state
        self.actions = actions
        self.result = result
        self.goal_test = goal_test
        self.max_memory = 0

    def search(self, start):
        self.max_memory = max(self.max_memory, len(self.f) + len(self.e))

        for act in self.actions(start):
            v = self.result(start, act)
            if self.goal_test(v):
                self.res2.append(act)
                self.res.append(v)
                self.res.append(start)
                self.visited.append(v)
                return True
            elif (v not in self.e) and (v not in self.f):
                self.f.append(v)
                self.visited.append(v)
                r = self.search(v)
                if r:
                    self.res.append(start)
                    self.res2.append(act)
                    return True
        self.f.remove(start)
        self.e.append(start)
        return False

    def search_dfs(self):
        start = self.initial_state()
        self.f = [start]
        self.e = []
        self.res = []
        self.visited = []
        self.search(start)
        if not self.res:
            print("there is no path")
        else:
            print("path found: ")
            for i in reversed(self.res2):
                print(i,  end=' ', flush=True)
            # print("--------")
            # for r in self.res:
            #     print(r)
            print()
            print("num visited: ", len(self.visited))
            print("num closed list: ", len(self.e))
            print("max memory use: ", self.max_memory)

