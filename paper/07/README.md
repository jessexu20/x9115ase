## Reading Assignment 7
#####Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Preetham Mahishi Srinath(preems)[student ID: pmahish]

- Shiqian Xu(jessexu20)[student ID: sxu11]

#### i. References:
Siegmund, Norbert, et al. "Predicting performance via automated feature-interaction detection." Proceedings of the 34th International Conference on Software Engineering. IEEE Press, 2012.
#### ii Keywords:
#####ii1. User-selectable features: 
Most of the programs provide a features where a user can tailor the program to the application scenario and customize it to his requirements. These customizable  feature set is called user-selectable program.
##### ii2. Feature Interaction:
A feature interaction occurs when a combination of user-selected features has an unexpected influence of the performance of the program. Two or more features are involved in a feature interaction. It will also include features which are necessary for the features involved in the interaction to work.
##### ii3. Hot-Spot Features:
These are a subset of available features that interact with many features causing a feature interaction. Most of the features in a program will interact with at least one of the Hot-spot features. Identifying hot-spot features from the rest of the features is an important step for calculating the heuristics.
##### ii4. Implication Graph
An implication graph is a graph in which nodes represent features and directed edges denote implications between features. Such a graph will help in calculating the heuristics required for performance prediction.
#### iii Artifacts
##### iii1.  Motivational Statements
As of today, developers can only detect the feature detection only by analyzing the source code and the flow of the program. They should also be able understand the specifications and the use case of each features. This will require substantial domain knowledge, exhaustive analysis capabilities and is subjected to the availability of the source code. Authors of the paper wanted to solve this problem.
##### iii2. Sampling procedures 
For evaluating the procedure, the authors have selected 6 programs. Three of them are customizable  programs and the remaining three are Software Program Lines. They have code bases of different sizes and are implemented in different languages. They are industrial programs already used by a vast number of people.
##### iii3. Related work
There are many related works aimed at predicting the performance of a customizable program or a Software Program Line generated program, many of them can be categorized into three types,  model-based, measurement-based and mixed.  In model based linear and multiple regression models the relationship between input parameters and performance as output.
##### iii4. Results
The below table shows the results of the experiment containing the 6 different programs when used with 3 different heuristics namely Pair-Wise Interactions (PW), Higher-Order Interactions(HO) and Hot-Spot Features(HS).
![results](result.jpg)
#### iv. Ways to improve the paper
 - iv1. There is no theoretical proof for the 95% accuracy that is claimed in the paper. Only experiments report 95% accuracy
 - iv2.    The authors should have also selected programs not only from complied and static typed languages, but also from dynamic typed languages like Python and JavaScript. 
 

