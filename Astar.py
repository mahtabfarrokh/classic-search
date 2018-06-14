class AStar:
    def __init__(self, initial_state, actions, result, goal_test, get_cost, heuristic):
        self.f = []
        self.e = []
        self.res = []
        self.visited = []
        self.initial_state = initial_state
        self.actions = actions
        self.result = result
        self.goal_test = goal_test
        self.get_cost = get_cost
        self.heuristic = heuristic
        self.max_memory = 0

    def search(self):
        while self.f:
            self.max_memory = max(self.max_memory, len(self.f) + len(self.e))
            x = self.f[0]
            minv = x[1]
            path = x[0]
            udru = x[2]
            heur = x[3]
            for v in self.f:
                if v[1] + v[3] < minv + heur:
                    minv = v[1]
                    path = v[0]
                    udru = v[2]
                    heur = v[3]
            node = path[-1]
            for v in self.f:
                p = v[0]
                if p[-1] == node and v[1] + v[3] > minv + heur:
                    self.f.remove(v)

            if self.goal_test(node):
                return [udru, path, minv, heur]

            self.f.remove([path, minv, udru, heur])
            if node not in self.e:
                self.e.append(node)

            for act in self.actions(node):
                v = self.result(node, act)
                if v not in self.e:
                    c = self.get_cost(path[0], v) + minv
                    heur = self.heuristic(v)
                    path2 = []
                    for p in path:
                        path2.append(p)
                    path2.append(v)
                    udru2 = []
                    for m in udru:
                        udru2.append(m)
                    udru2.append(act)
                    self.f.append([path2, c, udru2, heur])
                    if v not in self.visited:
                        self.visited.append(v)

    def search_astar(self):
        start = self.initial_state()
        self.f = [[[start], 0, [], 0]]
        self.e = []
        self.res = []
        p = self.search()
        if not p:
            print("there is no path")
        else:
            print("path found: ")
            print(p[0])
            print("num visited: ", len(self.visited))
            print("num closed list: ", len(self.e))
            print("max memory use: ", self.max_memory)
            print("path cost : ", p[2]+ p[3])

