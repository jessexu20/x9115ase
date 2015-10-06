## Reading Assignment 2
#####Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Preetham Mahishi Srinath(preems)[student ID: pmahish]

- Shiqian Xu(jessexu20)[student ID: sxu11]

##### i. Reference to the Paper
Classen, Andreas, Patrick Heymans, Pierre-Yves Schobbens, Axel Legay, and Jean-François Raskin. "Model checking lots of systems: efficient verification of temporal properties in software product lines." In Proceedings of the 32nd ACM/IEEE International Conference on Software Engineering-Volume 1, pp. 335-344. ACM, 2010.

##### ii. Most Important Keywords 

<b> ii1. Software product line</b>  
A set of software products that are distinguished in terms of features.

<b> ii2. Features </b>  
In SPLE, features are first-class abstractions that shape the reasoning of the engineers and other stakeholders [2]. 

<b> ii3. Feature diagrams</b>  
Diagrams used to model the variability of the software product line.

<b> ii4. Featured transition systems</b>  
A variant of transition systems designed to describe the combined behaviour of an entire system family.

##### iii. Brief notes on items 
<b> iii1. Motivational Statements</b>  
Authors mainly concentrate on two challenges that model based SPLE approaches need to address:
a) scalable modelling;
b) efficient verification of system behaviour.

<b> iii2. Hypotheses</b>  
Authors claim this paper lays the foundations for scalable modelling and efficient verification of software product lines. Also, the principal advantages of featured transition systems over existing work are
a) the modelling of variability as a first-class citizen, 
b) the ability to reason about the whole product line, or subsets of it, 
c) the ability to model very detailed behavioural variations, 
d) a running and freely available model checking tool, 
e) the ability to take feature dependencies and incompatibilities into account.

<b> iii3. Study instruments</b>  
Throughout this paper, a beverage vending machine is used as a running example. 
In its basic version, the vending machine takes a coin, returns change, serves soda, and eventually opens a compartment so that the customer can take her soda, before it closes it again.

<b> iii4. Future works</b>  
a) label each transition with a Boolean expression over the set of features in FTS;
b) define translations from high-level modelling languages, such as Statecharts and Promela, to FTS;
c) explore merging techniques, which create an FTS of the SPL based on the TS fragments of high-level features [3].

##### iv. Three ways the paper could be improved.  
<b> iv1. More case studies</b>  
Currently, there is only one model evaluated in their work. The conclusion they made can be much more convincing if more experiments are conducted on different models.

<b> iv2. Showing the improvements</b>  
It will be better if improvements are shown in tables or figures. Currently, there is only comparisons of time. I would like to see other scores that can evaluate the methods.

<b> iv3. Background knowledge</b>  
Authors assume that the reader is familiar with automata theory and has basic knowledge of formal verification. It could be better if more background knowledge is provided briefly.

##### References  
[1] [Classen, Andreas, Patrick Heymans, Pierre-Yves Schobbens, Axel Legay, and Jean-François Raskin. "Model checking lots of systems: efficient verification of temporal properties in software product lines." In Proceedings of the 32nd ACM/IEEE International Conference on Software Engineering-Volume 1, pp. 335-344. ACM, 2010.](http://dl.acm.org/citation.cfm?id=1806850)

[2] [Classen, Andreas, Patrick Heymans, and Pierre-Yves Schobbens. "What’s in a feature: A requirements engineering perspective." In Fundamental Approaches to Software Engineering, pp. 16-30. Springer Berlin Heidelberg, 2008.](http://link.springer.com/chapter/10.1007/978-3-540-78743-3_2)

[3] [Classen, Andreas, Patrick Heymans, Thein Than Tun, and Bashar Nuseibeh. "Towards safer composition." In Software Engineering-Companion Volume, 2009. ICSE-Companion 2009. 31st International Conference on, pp. 227-230. IEEE, 2009.](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5070988&tag=1)


