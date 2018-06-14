from BFS import BFS
from DFS_iterative import DFSIterative
from DFS_Limited import DFSLimited


class Problem3:
    def __init__(self, path=None):
        self.start = []
        self.path = path
        self.move = ['T','RC', 'TC', 'F', 'FC', 'R']
        if not path:
            self.path = 'test3.txt'
        self.initial_state()

    def actions(self, state):
        return self.move

    def open_file(self):
        f = open(self.path)
        lines = f.read()
        f.close()
        self.start = lines.split(" ")

    def initial_state(self):
        self.open_file()
        return self.start

    def goal_test(self, state):
        for i in range(0, 6):
            if not(state[0 + i*4] == state[1 + i*4] and state[0 + i*4] == state[2 + i*4]):
                return False
            if not state[0 + i * 4] == state[3 + i * 4]:
                return False
        return True

    def result(self, state, action):
        res = []
        for i in state:
            res.append(i)
        if action == 'RC':
            res[1] = state[13]
            res[3] = state[15]
            res[5] = state[1]
            res[7] = state[3]
            res[9] = state[5]
            res[11] = state[7]
            res[13] = state[9]
            res[15] = state[11]

            res[20] = state[22]
            res[21] = state[20]
            res[22] = state[23]
            res[23] = state[21]
            return res
        if action == 'R':
            res[1] = state[5]
            res[3] = state[7]
            res[5] = state[9]
            res[7] = state[11]
            res[9] = state[13]
            res[11] = state[15]
            res[13] = state[1]
            res[15] = state[3]

            res[20] = state[21]
            res[21] = state[23]
            res[22] = state[20]
            res[23] = state[22]
            return res
        if action == 'T':
            res[16] = state[4]
            res[17] = state[5]
            res[14] = state[16]
            res[15] = state[17]
            res[21] = state[14]
            res[20] = state[15]
            res[4] = state[20]
            res[5] = state[21]

            res[0] = state[2]
            res[1] = state[0]
            res[2] = state[3]
            res[3] = state[1]
            return res
        if action == 'TC':
            res[20] = state[4]
            res[21] = state[5]
            res[5] = state[17]
            res[4] = state[16]
            res[17] = state[14]
            res[16] = state[15]
            res[15] = state[20]
            res[14] = state[21]
            res[0] = state[1]
            res[1] = state[3]
            res[2] = state[0]
            res[3] = state[2]
            return res
        if action == 'F':
            res[2] = state[19]
            res[3] = state[17]
            res[20] = state[2]
            res[22] = state[3]
            res[9] = state[20]
            res[8] = state[22]
            res[19] = state[9]
            res[17] = state[8]
            res[4] = state[6]
            res[5] = state[4]
            res[6] = state[7]
            res[7] = state[5]
            return res
        if action == 'FC':
            res[2] = state[20]
            res[3] = state[22]
            res[20] = state[9]
            res[22] = state[8]
            res[9] = state[19]
            res[8] = state[17]
            res[19] = state[3]
            res[17] = state[3]
            res[4] = state[5]
            res[5] = state[7]
            res[6] = state[4]
            res[7] = state[6]
            return res
        return

    def get_cost(self, state1, state2):
        return 1

    def call_dfs_limited(self):
        dfs = DFSLimited(self.initial_state, self.actions, self.result, self.goal_test)
        dfs.search_dfs(9)

    def call_dfs_iter(self):
        dfs = DFSIterative(self.initial_state, self.actions, self.result, self.goal_test)
        dfs.search_dfs()

    def call_bfs(self):
        dfs = BFS(self.initial_state, self.actions, self.result, self.goal_test, self.get_cost)
        dfs.search_bfs()



p = Problem3()
# p.call_bfs()
# p.call_dfs_iter()
p.call_dfs_limited()