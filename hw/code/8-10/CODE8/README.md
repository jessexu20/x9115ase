
# Report of Code 8

#####Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Shiqian Xu (jessexu20)[student ID: sxu11]

- Preetham Mahishi Srinath(preems)[student ID: pmahish]

### A comparison between Simulated Annealing, MaxWalkSat and Differential Evolution

#### I. Overview

The optimum solution for any model has to be chosen from a large pool of possible solutions. The size of the pool can be thousands and can grow exponential based on the number of parameters required for the optimization. Comparing all the possible solution candidates with other in a exponentially growing space will become impossible even with considerably small set of data. Algorithms like DE, MWS and SA will help us in skipping over many of those comparisons while still finding the most optimal solution. The purpose of the exercise is to rank the performance of each of these algorithms. The model we are using here is DTL27. We will statistical methods like t-knott, a12 and bootstrap to compare the candidate solutions.  
 
#### II. Background
##### Differential Evolution
Differentail Evolution borrows concepts from genetic algorithms. It solves an optimization problem by iteratively trying to improve the candidate solution with respect to some measure of quality of the solution. It is based on a heuristic and does not guarantee an optimal solution always. But the advantage here is that it starts giving good solutions quickly compared to other algorithms. In every iteration, the candidates are created from crossing over the candidates created from the previous iteration. If the new crossed over candidate is more efficient than the previous one, then it is replaced. The process continues until a threshold is reached.

##### Simulated Annealing
Simulated Annealing is a search optimization algorithm which is better than greedy hill climbing. It is designed to the avoid the local optima which the hill climbing can get stuck at. In the beginning, the algorithm randomly jumps around the whole search space from a random seed in search of better solutions. In each jump, it tries to find a better solution. There are chances that it can jump to the less optimal solutions which will help us to avoid the local optima. The probability of jumping to the lower solution decreases with the time as the random jumping reduces over the time and we will converge on the global optima by skipping the local optima. 

##### Max Walk Sat
Max walk Sat is similar to Simulated Annealing. It helps to find an optimal solution in a discrete solution space.  The algorithm starts with improving one dimension at a time instead of jumping around randomly. If it does not find a solution which is above a certain threshold in that dimension, it returns back to where it was and explores another dimension. It fixes a certain part of the solution and explores the rest of the solution to find the optimal ones. This algorithm understands the landscape and explores the solutions accordingly. 
 
#### III. Introduction
There are three main types of comparators namely type1,type2 and type3 comparators. The type 1 comparator is mainly used to compare two candidate solutions. It is used as part of the algorithm whenever a new solution is generated. Type 2 comparator is mainly used to compare two era of candidate solutions. This helps us to find out if there is a significant change in the new era generated by the algorithm. If the algorithm starts generating solutions where are not a significant improvement over the previous era, then we can terminate the algorithm. We use Vargha and Deleney's A12 statistic to find if there is a significant difference in the sets of solutions.
Type 3 comparator is run on all the eras generated from the different algorithms. This is run once all the algorithms are terminated.

#### IV. Process
We implement all the above mentioned 3 types of comparators. We use them in the three mentioned algorithms. We use the DTLZ model with 10 decision and 2 objective. We run the each of the optimizers 20 times with different baselines to generate a list of eras.

#### V.Threats to Validity
Even though it looks like that all the algorithms archives the same goal and any of them can be replaced by any other, it is a mistake to make such assumption. All the three algorithms have certain use cases where they excel at. We are not considering the time and amount of resources in this experiment. Differential Evolution is more suited in a environment where resources are constrain. We are also not considering the how much space is explored by the algorithms before terminating and we have not understood how does the algorithms react to changes in thresholds. Each of the algorithms works well at different kind of search space, but just using one model does not give the complete picture. 

#### VI. Future Work
The experiment was conducted only on one model. This can be expanded to multiple model which gives us the complete picture of where which algorithms performs best. We also want to have objectives other than finding the optimal solution like time taken and the amount of space explored. The amount of space explored will help us tune the right balance between exploration and exploitation which is very necessary for such search optimization problems.