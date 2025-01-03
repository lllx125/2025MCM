from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.problems import get_problem
from pymoo.termination import get_termination
from pymoo.optimize import minimize
import matplotlib.pyplot as plt

# ZDT1 is a standard 2-objective problem with a decision space of [0,1]^n
problem = get_problem("zdt1")

algorithm = NSGA2(
    pop_size=100,      # population size
    n_offsprings=20,   # number of offsprings to generate each iteration
)

termination = get_termination("n_gen", 200)

result = minimize(problem,
                  algorithm,
                  termination,
                  seed=1,      # for reproducibility
                  save_history=True,
                  verbose=False)

# result.X gives the decision variables of the final population
# result.F gives the objectives of the final population

pareto_front = result.F
print("Pareto Front (Objectives):")
print(pareto_front)

# Let's plot the Pareto front
plt.scatter(pareto_front[:, 0], pareto_front[:, 1],
            s=20, facecolors='none', edgecolors='blue')
plt.title("Approximation of the Pareto Front for ZDT1")
plt.xlabel("Objective 1")
plt.ylabel("Objective 2")
plt.show()
