from DFS_Unlimited import DFSUnlimited
from uniform_cost import UniformCost
from bidirectional import Bidirectional
from Astar import AStar


class Problem2:
    def __init__(self, path=None):
        self.start = []
        self.goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        self.path = path
        self.u = [0, -1, 'u']
        self.d = [0, 1, 'd']
        self.r = [1, 0, 'r']
        self.l = [-1, 0, 'l']
        self.move = [self.u, self.d, self.r, self.l]
        if not path:
            self.path = 'test2.txt'

    def actions(self, state):
        res = []
        for m in self.move:
            for i in range(0, 3):
                for j in range(0, 3):

                    k = state[i]
                    if k[j] == 0:
                        if m[2] == 'u' and i + 1 < 3:
                            res.append(m)
                        if m[2] == 'd' and i - 1 >= 0:
                            res.append(m)
                        if m[2] == 'r' and j - 1 >= 0:
                            res.append(m)
                        if m[2] == 'l' and j + 1 < 3:
                            res.append(m)
        return res

    def open_file(self):
        f = open(self.path)
        lines = f.read()
        f.close()
        lines = lines.split("\n")
        for line in lines:
            num = line.split(" ")
            l = [int(num[0]), int(num[1]), int(num[2])]
            self.start.append(l)

    def initial_state(self):
        self.open_file()
        return self.start

    def goal_test(self, state):
        if state == self.goal:
            return True
        return False

    def result(self, state, action):
        res = []
        for i in range(0, 3):
            temp = []
            for j in range(0, 3):
                temp.append(state[i][j])
            res.append(temp)

        for i in range(0, 3):
            for j in range(0, 3):
                if state[i][j] == 0:
                    if action[2] == 'u':
                        res[i][j] = int(state[i + 1][j])
                        res[i + 1][j] = 0
                        return res
                    if action[2] == 'd':
                        res[i][j] = int(state[i - 1][j])
                        res[i - 1][j] = 0
                        return res
                    if action[2] == 'r':
                        res[i][j] = int(state[i][j - 1])
                        res[i][j - 1] = 0
                        return res
                    if action[2] == 'l':
                        res[i][j] = int(state[i][j + 1])
                        res[i][j + 1] = 0
                        return res

    def path_cost(self, c, state1, action, state2):
        return

    def get_cost(self, state1, state2):
        return 1

    def get_reverse_Action(self, action):
        if action == 'u':
            return 'd'
        if action == 'd':
            return 'u'
        if action == 'r':
            return 'l'
        if action == 'l':
            return 'r'

    def heuristic(self, state):
        x = 0
        for i in range(0, 3):
            for j in range(0, 3):
                a = state[i][j] / 3
                b = state[i][j] % 3
                x += ((a-i)**2 + (b-j)**2)**(1/2.0)
        return x

    def call_dfs_unlimited(self):
        dfs = DFSUnlimited(self.initial_state, self.actions, self.result, self.goal_test)
        dfs.search_dfs()

    def call_uniform_cost(self):
        uc = UniformCost(self.initial_state, self.actions, self.result, self.goal_test, self.get_cost)
        uc.search_uniform()

    def call_bidirectional(self):
        bd = Bidirectional(self.initial_state, self.actions, self.result, self.goal_test, self.get_cost, self.get_reverse_Action)
        bd.search_bidirection(self.goal)

    def call_astar(self):
        astar = AStar(self.initial_state, self.actions, self.result, self.goal_test, self.get_cost, self.heuristic)
        astar.search_astar()

p = Problem2()
# p.call_dfs_unlimited()
# p.call_uniform_cost()
# p.call_bidirectional()
p.call_astar()