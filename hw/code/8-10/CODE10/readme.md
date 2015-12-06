
# Report of Code 10

#####Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Shiqian Xu (jessexu20)[student ID: sxu11]

- Preetham Mahishi Srinath(preems)[student ID: pmahish]

### Introduction

#### Overview

 - **Optimization** is the main frame of this Code. Our task is to find best decisions to achieve highest objectives.
 - **Multi-objective Optimization**: we have more than one objectives. Optimal decisions need to be taken in the presence of trade-offs between two or more conflicting objectives.
 - **Tuning**: use another optimization algorithm to optimize the magic parameters of the optimizer.

#### Algorithm

 - **Genetic Algorithm**: an optimization algorithm. 
 
 ```
 1. Initialization
 2. Selection (generate the pareto frontier by comparing each candidates)
 3. Crossover (use parents from pareto frontier to make babies)
 4. Mutate (change a small amount of the newly born babies randomly)
 5. go back to 2. repeat until maximum generation is reached or early termination criteria is met.
 ```
 
 - **Differential Evolution**: another optimization algorithm. 

 ```
 1. Initialization
 2. For each candidate X in the population, create a new candidate N (by mixing X and 3 other random candidates). If the new candidate dominate X, replace X with N.
 3. go back to 2. repeat until maximum generation is reached or early termination criteria is met.
 ```

#### Three Betters
 
 - **Binary Domination**: you can only say Solution A is better than Solution B when all the objectives of A is not worth than those of B and at least one of the decision of A is better than that of B. In such a case, we say A binary-dominate B. Binary domination is performed between candidates.
 - **Better Generation**: the second Better is performed whenever a new generation is generated. Every candidates in the pareto frontier of the new generation will be tested to see if it binary-dominates any candidate in the Best Pareto Frontier. If yes, replace the dominated one with the new one. The new generation is considered as a better one if any of its candidate is selected into the Best Pareto Frontier. This Better Generation is used to determine early termination.
 - **Better Algorithm**: hypervolumn of the Best Pareto Frontier is used as a score of the algorithm (will be 0-1). The higher the hypervolumn, the better the algorithm.

#### Models

 - **DTLZ**: models built specifically to stress the optimization algorithms. For more details, see [DTLZ1,3,5,7](http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf)

### Experiment

#### Setup

##### Default Setup for GA

 - GA on 4 different models: DTLZ1,3,5,7
 - with decision numbers 10, 20, 40
 - and objective numbers 2, 4, 6, 8
 - repeat 20 times for each (with seeds 0-19)
 - mutation rate: 0.05
 - crossover: one point
 - number of candidates: 100
 - number of maximum generations: 1000
 - early termination: life = 5, each new generation, if not better, life=life-1; else, life = 5. Terminate when life = 0.

##### Tuning Setup

- Use DE to tune GA
- Decisions of DE: mutation rate (0.01-0.5), number of candidates (10-1000), early termination lifes (1-10).
- Objective of DE: hypervolumn of GA's Best Pareto Frontier
- Number of Candidates of DE: 10
- Number of Maximum Generations: 10

#### Runing Instruction

 - Run GA.py first, results will be dumped into data/hypervolumn.pickle. Then run visualize.py to read from data/hypervolumn.pickle and generate the table.

#### Results

 - results of hypervolumn
 
```
model: DTLZ1
                                  10                     20       40
2_tuned    0.99989±8.25000000001e-05                1.0±0.0  1.0±0.0
2_untuned           0.9974±0.0043925           1.0±0.001135  1.0±0.0
4_tuned                0.99997±2e-05          1.0±0.0001225  1.0±0.0
4_untuned         0.999255±0.0009325  1.0±1.00000000001e-05  1.0±0.0
6_tuned             0.99998±2.25e-05                1.0±0.0  1.0±0.0
6_untuned           0.999625±0.00025                1.0±0.0  1.0±0.0
8_tuned           0.999985±0.0010325                1.0±0.0  1.0±0.0
8_untuned         0.996875±0.0067525          1.0±0.0001175  1.0±0.0
model: DTLZ3
                                   10                 20       40
2_tuned            0.999795±0.0001925  0.999995±0.001815  1.0±0.0
2_untuned          0.996745±0.0040625        1.0±0.00032  1.0±0.0
4_tuned             0.999935±8.25e-05            1.0±0.0  1.0±0.0
4_untuned          0.998205±0.0015575            1.0±0.0  1.0±0.0
6_tuned    0.999975±9.99999999995e-06            1.0±0.0  1.0±0.0
6_untuned            0.9993±0.0011325            1.0±0.0  1.0±0.0
8_tuned                0.999985±4e-05            1.0±0.0  1.0±0.0
8_untuned            0.998965±0.01063            1.0±0.0  1.0±0.0
model: DTLZ5
                           10                 20                  40
2_tuned    0.748045±0.0160075    0.75183±0.01333     0.7482±0.027145
2_untuned    0.703595±0.02929  0.708935±0.028495   0.710645±0.033835
4_tuned    0.576325±0.0084675   0.647845±0.01889   0.649185±0.012565
4_untuned      0.5113±0.05437   0.55531±0.042765   0.54127±0.0261175
6_tuned    0.226215±0.0192875  0.354485±0.130075   0.46885±0.0286575
6_untuned  0.168795±0.0318475  0.16545±0.0358025  0.174085±0.0358175
8_tuned      0.08471±0.017395  0.11049±0.0121675    0.086565±0.00736
8_untuned    0.05214±0.018005  0.06296±0.0149375    0.046425±0.00845
model: DTLZ7
                           10                  20                  40
2_tuned    0.936445±0.0561325    0.8323±0.1046375     0.769075±0.0248
2_untuned    0.8831±0.0683425   0.705995±0.036265   0.67543±0.0255925
4_tuned      0.70704±0.019695   0.66882±0.0229925  0.612485±0.0143625
4_untuned    0.55833±0.080545   0.530155±0.060775   0.45886±0.0475925
6_tuned      0.55281±0.029755  0.511575±0.0272125  0.458155±0.0174675
6_untuned   0.35057±0.0662875  0.311005±0.0661525   0.25454±0.0498875
8_tuned      0.379115±0.02508   0.32447±0.0179175      0.31177±0.0282
8_untuned  0.164135±0.0430325   0.12915±0.0330625   0.12552±0.0266325

```

 - whether tuning is better or the same
 
```
model: DTLZ1
      10     20     40
2  False  False  False
4  False  False  False
6  False  False  False
8  False  False  False

model: DTLZ3
      10     20     40
2  False  False  False
4  False  False  False
6  False  False  False
8  False  False  False

model: DTLZ5
     10    20    40
2  True  True  True
4  True  True  True
6  True  True  True
8  True  True  True

model: DTLZ7
     10    20    40
2  True  True  True
4  True  True  True
6  True  True  True
8  True  True  True

```

### Conclusions

 - performance (measured by hypervolumn) is already excellent on DTLZ1,3, tuning does no better on DTLZ1,3.
 - performance (measured by hypervolumn) is ugly without tuning on DTLZ5,7, tuning improves the performance significantly on DTLZ5,7
 - number of candidates influence the performance the most. 600 candidates provide much better performance on DTLZ5,7.
 - usually it takes less than 10 generations for DE to terminate.

### Validity Threats

 - **Conclusion Validity**: quite reliable since 20 repeats are taken for each result.
 - **Credibility**: not that confident since hypervolumn is questionable as a performance metric. But we cannot find better metrics for multi-objective problems. Also, only 10 candidates are in the generation of DE, a better tuning performance may be provided given larger number of candidates.
 
### Future Work

 - Try different parameters of DE. 
 - Make it run faster.
 
