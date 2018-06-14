class Bidirectional:
    def __init__(self, initial_state, actions, result, goal_test, get_cost, get_reverse):
        self.f1 = []
        self.e1 = []
        self.f2 = []
        self.e2 = []
        self.visited = []
        self.initial_state = initial_state
        self.actions = actions
        self.result = result
        self.goal_test = goal_test
        self.get_cost = get_cost
        self.max_memory = 0
        self.get_reverse = get_reverse

    def intersect(self):
        for x in self.f1:
            minv = x[1]
            path = x[0]
            udru = x[2]
            node = path[-1]
            for y in self.f2:
                p = y[0]
                m = x[1]
                u = x[2]
                if node == p[-1]:
                    return [path, minv, udru, p, m, u]
        return False

    def search(self):
        turn = False
        while self.f1 and self.f2:
            turn = not turn
            self.max_memory = max(self.max_memory, len(self.f1) + len(self.e1) + len(self.f2) + len(self.e2))
            if turn:
                x = self.f1[0]
                minv = x[1]
                path = x[0]
                udru = x[2]
                node = path[-1]
                inter = self.intersect()
                if inter:
                    return inter
                self.f1.remove([path, minv, udru])
                if node not in self.e1:
                    self.e1.append(node)
                for act in self.actions(node):
                    v = self.result(node, act)
                    if v not in self.e1:
                        c = self.get_cost(path[0], v) + minv
                        path2 = []
                        for p in path:
                            path2.append(p)
                        path2.append(v)
                        udru2 = []
                        for m in udru:
                            udru2.append(m)
                        udru2.append(act)
                        self.f1.append([path2, c, udru2])
                        if v not in self.visited:
                            self.visited.append(v)
            else:

                x = self.f2[0]
                minv = x[1]
                path = x[0]
                udru = x[2]
                node = path[-1]
                inter = self.intersect()
                if inter:
                    return inter
                self.f2.remove([path, minv, udru])

                if node not in self.e2:
                    self.e2.append(node)

                for act in self.actions(node):
                    v = self.result(node, act)
                    if v not in self.e2:
                        c = self.get_cost(path[0], v) + minv
                        path2 = []
                        for p in path:
                            path2.append(p)
                        path2.append(v)
                        udru2 = []
                        for m in udru:
                            udru2.append(m)
                        udru2.append(self.get_reverse(act))
                        self.f2.append([path2, c, udru2])
                        if v not in self.visited:
                            self.visited.append(v)

    def search_bidirection(self, end):
        start = self.initial_state()
        self.f1 = [[[start], 0, []]]
        self.e1 = []
        self.f2 = [[[end], 0, []]]
        self.e2 = []
        self.visited = []
        p = self.search()
        if not p:
            print("there is no path")
        else:
            print("path found: ")
            for x in p[2]:
                print(x)
            last = 0
            flag = False
            for x in reversed(p[3]):
                if flag:
                   for act in self.actions(last):
                        new = self.result(last, act)
                        if new == x:
                            print(act)
                            break
                flag = True
                last = x

            print("num visited: ", len(self.visited))
            e = len(self.e1) + len(self.e2)
            print("num closed list: ", e)
            print("max memory use: ", self.max_memory)
            print("path cost : ", p[1] + p[4])