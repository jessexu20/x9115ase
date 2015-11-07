# Reading Assignment 8
## Strategies for Product-Line Verification: Case Studies and Experiments
#### Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Preetham Mahishi Srinath(preems)[student ID: pmahish]

- Shiqian Xu(jessexu20)[student ID: sxu11]

#### i. References:
Detection of feature interactions using feature-aware verification 

#### ii. Keywords:
##### ii1. Model-checking technology:
Given a model of a system, exhaustively and automatically check whether this model meets a given specification. Typically, one has hardware or software systems in mind, whereas the specification contains safety requirements such as the absence of deadlocks and similar critical states that can cause the system to crash. Model checking is a technique for automatically verifying correctness properties of finite-state systems. 
##### ii2. Product-Line Verification
Product-line verification refers to analysis and verification techniques which is used to ensure correctness, reliability, and security of product-line technologies. In this paper, it discusses three popular ways which are being used nowadays, which are product-based strategy, sample-based strategy and family-based strategy.
##### ii3. feature interaction
Feature interaction is a situation when two or more features are combined into one behavior that cannot be simply deduced from the behavior of the individual involved features. 
##### ii4.  tool chain
A toolchain is a set of distinct software development tools that are linked (or chained) together by specific stages such as GCC, binutils and glibc. Alternatively, a toolchain may contain other tools such as a Debugger or a Compiler for a specific programming language. In this paper, it refers to the SPLVERIFIER, which consists a number of tools:  FEATUREHOUSE(feature composition), CPACHECKER(model checking for C) and JAVA PATHFINDER (model checking for Java). Both of the model checking tools support the verification of safety properties by means of explicit-state and symbolic model checking.

#### iii. Artifacts:
##### iii1. Motivation
Although there are many researchers start to discuss and research on the strengths and weaknesses of sample-based and family-based strategies, each in comparison to the product-based strategy. However, there is no work that compares the sample-based strategy with the family-based strategy systematically in a controlled setting. Therefore, authors thinks about the they can work on this to provide a case study to get rid of the lack of case studies and experiments in this field. They are going to collect and prepare existing and implement further case-study product lines, as well as to develop a model-checking tool chain.

##### iii2. New results
Based on the experiments, the authors have revisited the discussion of the strengths and weaknesses of sample-based and family-based strategies. They have created an analytical model to decribe the trade-offs of the individual verfication strategies. And they found out that the family-based strategy outperforms the sample-based strategy in terms of defect-detection efficiency. They also noticed that triple-wise outperformed pair-wise sampling for sample-based strategy.

##### iii3. Related work
In related work section, they talked a lot about the sampling heuristics done by researches in feature-interaction detection. Also there are other case studies which did studies on sample-based strategy using pair-wise methods. Furthermore, they talked about researches on family-based strategy and feature-based verfication, however the related paper fails to cover the performance regarding to family-based strategy.
##### iii4. 

#### iv. Improvements:

 
