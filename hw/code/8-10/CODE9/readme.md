
# Report of Code 9

#####Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Shiqian Xu (jessexu20)[student ID: sxu11]

- Preetham Mahishi Srinath(preems)[student ID: pmahish]

### Introduction

#### Overview

 - **Optimization** is the main frame of this Code. Our task is to find best decisions to achieve highest objectives.
 - **Multi-objective Optimization**: we have more than one objectives. Optimal decisions need to be taken in the presence of trade-offs between two or more conflicting objectives.

#### Algorithm

 - **Genetic Algorithm**: an optimization algorithm. 
 
 ```
 1. Initialization
 2. Selection (generate the pareto frontier by comparing each candidates)
 3. Crossover (use parents from pareto frontier to make babies)
 4. Mutate (change a small amount of the newly born babies randomly)
 5. go back to 2. repeat until maximum generation is reached or early termination criteria is met.
 ```

#### Three Betters
 
 - **Binary Domination**: you can only say Solution A is better than Solution B when all the objectives of A is not worth than those of B and at least one of the decision of A is better than that of B. In such a case, we say A binary-dominate B. Binary domination is performed between candidates.
 - **Better Generation**: the second Better is performed whenever a new generation is generated. Every candidates in the pareto frontier of the new generation will be tested to see if it binary-dominates any candidate in the Best Pareto Frontier. If yes, replace the dominated one with the new one. The new generation is considered as a better one if any of its candidate is selected into the Best Pareto Frontier. This Better Generation is used to determine early termination.
 - **Better Algorithm**: hypervolumn of the Best Pareto Frontier is used as a score of the algorithm (will be 0-1). The higher the hypervolumn, the better the algorithm.

#### Models

 - **DTLZ**: models built specifically to stress the optimization algorithms. For more details, see [DTLZ1,3,5,7](http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf)

### Experiment

#### Setup

 - GA on 4 different models: DTLZ1,3,5,7
 - with decision numbers 10, 20, 40
 - and objective numbers 2, 4, 6, 8
 - repeat 20 times for each (with seeds 0-19)
 - mutation rate: 0.05
 - crossover: one point
 - number of candidates: 100
 - number of maximum generations: 1000
 - early termination: life = 5, each new generation, if not better, life=life-1; else, life = 5. Terminate when life = 0.

#### Runing Instruction

 - Run GA.py first, results will be dumped into data/hypervolumn.pickle. Then run visualize.py to read from data/hypervolumn.pickle and generate the table.

#### Results

 - results of hypervolumn

```
model: DTLZ1
                   10               20       40
2   0.99735±0.0038975  0.99997±0.00151  1.0±0.0
4  0.999355±0.0008775     1.0±0.001065  1.0±0.0
6  0.999755±0.0002525        1.0±8e-05  1.0±0.0
8   0.997975±0.006725          1.0±0.0  1.0±0.0
model: DTLZ3
                   10                     20       40
2  0.996565±0.0065725          1.0±0.0003675  1.0±0.0
4   0.99823±0.0017425                1.0±0.0  1.0±0.0
6  0.998905±0.0012675  1.0±2.50000000002e-06  1.0±0.0
8   0.99923±0.0106125                1.0±0.0  1.0±0.0
model: DTLZ5
                  10                  20                  40
2       0.7056±0.027    0.709405±0.04436  0.696185±0.0420025
4     0.53194±0.0437   0.561815±0.035305   0.52345±0.0298175
6   0.1276±0.0258575     0.13945±0.03227    0.159955±0.02961
8  0.045255±0.015465  0.048835±0.0122725     0.05619±0.00892
model: DTLZ7
                   10                  20                 40
2    0.8976±0.0414725    0.691695±0.03826     0.66486±0.0266
4     0.55817±0.07932  0.542845±0.0625125   0.434825±0.04526
6  0.338195±0.0661025    0.328275±0.06863  0.27895±0.0556825
8   0.16422±0.0431325   0.13579±0.0359625   0.131885±0.02719

```

### Conclusions

 - performance (measured by hypervolumn) is excellent on DTLZ1,3, but ugly on DTLZ5,7.
 - performance (measured by hypervolumn) increases as number of decisions increase.
 - performance (measured by hypervolumn) decreases as number of objectives increase.
 - usually it takes less than 20 generations to terminate.

### Validity Threats

 - **Conclusion Validity**: quite reliable since 20 repeats are taken for each result.
 - **Credibility**: not that confident since hypervolumn is questionable as a performance metric. But we cannot find better metrics for multi-objective problems. Also, early termination seems strict in this experiment, GA may perform better on DTLZ5,7 when taking more generations.
 
### Future Work

 - tune the magic parameters in GA to see what happens.
 
