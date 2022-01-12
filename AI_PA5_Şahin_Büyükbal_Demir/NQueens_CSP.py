import time
from simpleai.search import CspProblem, backtrack,MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE

class NQueenscsp(CspProblem):

    def __init__(self,variables,domains,constraints,n):
        super(NQueenscsp, self).__init__(variables,domains,constraints)
        
        
        

def createvariables(n):
        temp = []
        for i in range(1,n+1):
            temp.append((f"{i}"))
        mytuple = tuple(temp)
        return mytuple

def values(n):
        temp = []
        for i in range (1,n+1):
            temp.append(i)
        return temp
        
def lines_attacked(variables, values):
        return values[0] != values [1] 
        
                

def diagonal_attacked(variables, values):
        return abs(int(variables[0])- int(variables[1])) != abs(values[0]- values[1])

def createconstraints(n):
    constraints = []
    tuples = []
    for i in range (0, n+1):
        for j in range(i, n+1):
            tuples.append((str(i),str(j)))
    print(tuples)
    for _,b in zip(constraints, tuples):
            constraints.append((tuples(b), lines_attacked))
    for _,b in zip(constraints, tuples):
            constraints.append((tuples(b), diagonal_attacked))
    return constraints
    
              
variables = createvariables(9)
domains = dict((v,values(9)) for v in variables)
constraints = [
    (('1','2'),lines_attacked),
(('1','3'),lines_attacked),(('1','4'),lines_attacked),
(('1','5'),lines_attacked),(('1','6'),lines_attacked),
(('1','7'),lines_attacked),(('1','8'),lines_attacked),
(('1','9'),lines_attacked),
(('2','3'),lines_attacked),(('2','4'),lines_attacked),
(('2','5'),lines_attacked),(('2','6'),lines_attacked),
(('2','7'),lines_attacked),(('2','8'),lines_attacked),
(('2','9'),lines_attacked),
(('3','4'),lines_attacked),(('3','5'),lines_attacked),
(('3','6'),lines_attacked),(('3','7'),lines_attacked),
(('3','8'),lines_attacked),(('3','9'),lines_attacked),
(('4','5'),lines_attacked),
(('4','6'),lines_attacked),(('4','7'),lines_attacked),
(('4','8'),lines_attacked),(('4','9'),lines_attacked),
(('5','6'),lines_attacked),
(('5','7'),lines_attacked),(('5','8'),lines_attacked),
(('5','9'),lines_attacked),
(('6','7'),lines_attacked),(('6','8'),lines_attacked),
(('6','9'),lines_attacked),
(('7','8'),lines_attacked),(('7','9'),lines_attacked),
(('8','9'),lines_attacked),
#lines end
#diagonals start
(('1','2'),diagonal_attacked),
(('1','3'),diagonal_attacked),(('1','4'),diagonal_attacked),
(('1','5'),diagonal_attacked),(('1','6'),diagonal_attacked),
(('1','7'),diagonal_attacked),(('1','8'),diagonal_attacked),
(('1','9'),diagonal_attacked),
(('2','3'),diagonal_attacked),(('2','4'),diagonal_attacked),
(('2','5'),diagonal_attacked),(('2','6'),diagonal_attacked),
(('2','7'),diagonal_attacked),(('2','8'),diagonal_attacked),
(('2','9'),diagonal_attacked),
(('3','4'),diagonal_attacked),(('3','5'),diagonal_attacked),
(('3','6'),diagonal_attacked),(('3','7'),diagonal_attacked),
(('3','8'),diagonal_attacked),(('3','9'),diagonal_attacked),
(('4','5'),diagonal_attacked),
(('4','6'),diagonal_attacked),(('4','7'),diagonal_attacked),
(('4','8'),diagonal_attacked),(('4','9'),diagonal_attacked),
(('5','6'),diagonal_attacked),
(('5','7'),diagonal_attacked),(('5','8'),diagonal_attacked),
(('5','9'),diagonal_attacked),
(('6','7'),diagonal_attacked),(('6','8'),diagonal_attacked),
(('6','9'),diagonal_attacked),
(('7','8'),diagonal_attacked),(('7','9'),diagonal_attacked),
(('8','9'),diagonal_attacked)
] 
class TicToc:
    def __init__(self):
        self.t1 = 0
        self.t2 = 0

    def tic(self):
        self.t1 = time.time()

    def toc(self):
        self.t2 = time.time()
        return self.t2-self.t1
timer = TicToc()
a = timer.tic()
myproblem = NQueenscsp(variables, domains, constraints,9)
result = backtrack(myproblem)
print(f"\nSolution time:\n{timer.toc():.4f} seconds")
print("\nVariable Heuristic:-\nValue Heuristic: -")
print(result)