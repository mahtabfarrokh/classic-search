from DFS_Unlimited import DFSUnlimited
from uniform_cost import UniformCost
from bidirectional import Bidirectional
from Astar import AStar


class Problem1:
    def __init__(self, path=None):
        self.m = 0
        self.n = 0
        self.num_wall = 0
        self.walls = []
        self.start = [1, 1]
        self.goal = [self.m, self.n]
        self.path = path
        self.u = [0, -1, 'u']
        self.d = [0, 1, 'd']
        self.r = [1, 0, 'r']
        self.l = [-1, 0, 'l']
        self.move = [self.u, self.d, self.r, self.l]
        if not path:
            self.path = 'test1.txt'
        self.initial_state()

    def actions(self, state):
        x = state[0]
        y = state[1]
        res = []
        for m in self.move:
            r = [x + m[0], y + m[1]]

            if 0 < r[0] and 0 < r[1] and r[0] <= self.m and r[1] <= self.n:

                t1 = [x, y, x + m[0], y + m[1]]
                t2 = [x + m[0], y + m[1], x, y]
                if (t1 not in self.walls) and (t2 not in self.walls):
                    res.append(m[2])
        return res

    def open_file(self):
        f = open(self.path)
        lines = f.read()
        f.close()
        counter = 0
        lines = lines.split("\n")
        for line in lines:
            num = line.split(" ")
            if counter == 0:
                self.m = int(num[0])
                self.n = int(num[1])
                counter += 1
            elif counter == 1:
                self.num_wall = int(num[0])
                counter += 1
            else:
                a1 = int(num[0])
                a2 = int(num[1])
                a3 = int(num[2])
                a4 = int(num[3])
                self.walls.append([a1, a2, a3, a4])

        self.goal = [self.m, self.n]

    def initial_state(self):
        self.open_file()
        return self.start

    def goal_test(self, state):
        x = state[0]
        y = state[1]
        if x == self.m and y == self.n:
            return True
        return False

    def result(self, state, action):
        if action == 'u':
            return [state[0], state[1] - 1]
        if action == 'd':
            return [state[0], state[1] + 1]
        if action == 'r':
            return [state[0] + 1, state[1]]
        if action == 'l':
            return [state[0] - 1, state[1]]

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
        d = (self.goal[1] - state[1])*(self.goal[1] - state[1]) +\
            (self.goal[0] - state[0]) * (self.goal[0] - state[0])
        return d**(1/2.0)

    def call_dfs_unlimited(self):
        dfs = DFSUnlimited(self.initial_state, self.actions, self.result, self.goal_test)
        dfs.search_dfs()

    def call_uniform_cost(self):
        uc = UniformCost(self.initial_state, self.actions, self.result, self.goal_test, self.get_cost)
        uc.search_uniform()

    def call_bidirectional(self):
        bd = Bidirectional(self.initial_state, self.actions, self.result, self.goal_test, self.get_cost,
                           self.get_reverse_Action)
        bd.search_bidirection(self.goal)

    def call_astar(self):
        astar = AStar(self.initial_state, self.actions, self.result, self.goal_test, self.get_cost, self.heuristic)
        astar.search_astar()

p = Problem1()
# p.call_dfs_unlimited()
# p.call_uniform_cost()
# p.call_bidirectional()
p.call_astar()