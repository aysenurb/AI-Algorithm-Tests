from simpleai.search import SearchProblem, breadth_first
from simpleai.search.traditional import astar, breadth_first, depth_first, greedy, iterative_limited_depth_first, limited_depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer
import time

class NQueensProblem(SearchProblem):

    def __init__(self,initial_state,n):

        super(NQueensProblem,self).__init__(initial_state)
        self.n = n
    def actions(self, state):
        numbers =[]
        for i in range(1, self.n+1):
            numbers.append(i)
        actions = []
        state_list = list(state)
        for i in range(4):
            for j in numbers:
                if state_list[i] == str(j):
                    continue
                else:
                    actions.append((i, f"Move queen {i+1} to row {j}", j,))
        return actions


    def result(self, state, action):
        state = list(state)
        print(action[1])
        queen_number = action[0]
        value = str(action[2])
        state[queen_number] = value
        result = ''.join([str(elem) for elem in state])
        return result
        

    def cost(self, state, action, state2):
       
        return 1

    def is_goal(self, state):
        lines = 0
        diagonal = 0
        for i in range(0, len(state)):
            for j in range (i+1, len(state)):
                if state[i] == state[j]:
                    lines +=1
        for i in range(0, len(state)):
            for j in range (i+1, len(state)):
                p1 = int(state[i])
                p2 = int(state[j])
                if abs(p2-p1) == abs(i-j):
                    diagonal += 1
        total = lines + diagonal
        if total == 0:
            return True
        else:
            return False

    def heuristic(self, state):
        lines = 0
        diagonal = 0
        for i in range(0, len(state)):
            for j in range (i+1, len(state)):
                if state[i] == state[j]:
                    lines +=1
        for i in range(0, len(state)):
            for j in range (i+1, len(state)):
                p1 = int(state[i])
                p2 = int(state[j])
                if abs(p2-p1) == abs(i-j):
                    diagonal += 1
        total = lines + diagonal
        return total
    
class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2-self.t1

myViewer = BaseViewer()
problem = NQueensProblem("24152",5)
timer = TicToc()
a = timer.tic()
result = greedy(problem,viewer=myViewer,graph_search=True)
print("\nSolution Method: Greedy" )
print("\nGraph Search?: True" )
print(f"\nSolution time:\n{timer.toc():.4f} seconds" )
print(f"Solution path:\n{result.path()}")
print(f"Resulting state:\n{result.state}")
print(f"Total cost:\n{result.cost}")
print(f"Viewer stats:\n{myViewer.stats}")