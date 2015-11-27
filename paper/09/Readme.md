# Reading Assignment 9
## Scalable Analysis of Variable Software
####Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Preetham Mahishi Srinath(preems)[student ID: pmahish]

- Shiqian Xu(jessexu20)[student ID: sxu11]

#### i. References:
Detection of feature interactions using feature-aware verification 

#### ii. Keywords:
##### ii1. Software Product Lines
Software product lines are software engineering methods, tools and techniques for creating a collection of similar software systems from a shared set of software assets using a common means of production. The definition by CMU is as follows, a set of software-intensive systems that share a common, managed set of features satisfying the specific needs of a particular market segment or mission and that are developed from a common set of core assets in a prescribed way.(wiki)
##### ii2. Variablity-aware Type Checking
The standard type-checking algorithm for C is to traverses the abstract syntax trees and then collects declarations in a symbol table, after that it attempts to assign proper types to all expressions by calling getType function.(Map[Name,Type]!Expr!Type)). 
In this paper, variability-aware type checker works in a similar way, however in order to cover all variants, it must be aware of variability in each of the following three steps.
- a symbol (variable, function, etc.) may only be declared in some variants, or it may even have alternative types in different variants.
- during expression typing, we assign a variable type to each expression where already looking up a name in a symbol table may return a variable type.
- we can use the variability model of a system to filter all type errors that occur only in invalid variants.

##### ii3. Liveness Analysis
Liveness analysis is a traditional data-flow analysis to compute whether variables are live, which may be read before being written again for a given statement. Its result can be used to conservatively detect dead code, useless code. The computation of liveness is a fixpoint algorithm that uses two functions, in and out, which compute variables that are live at respectively after the current statement.
##### ii4.  Variability Analysis
Variability Analysis, also known as family-based analysis,is not to generate and analysis variants separately but to directly analyse the variable code base by utilizing some configuration knowledge. It requires more effort than traditional analysis of a single system as all local variants are considered into the analysis. It could avoid analysing the common code by taking advantage of similarities among variants.
#### iii. Artifacts:
##### iii1. Motivation:
In this paper, the authors argue that although there are serveral proposals in variablity-aware analyses, none of them has been applied to large-scale, real-world systems so far. Most of them are limited to academic case studies only. Therefore, the authors think it might be a good way to analyse whether variablity-aware analysis scales to large systems, as it should consider all code and all variations of a system simutaneously.
##### iii2. Related Work:
The authors said in the paper that their implementations of variability-aware type checking and liveness analysis are inspired by earlier work in two fields. First is their previous paper's output, which includes Featherweight Java, Lightweight Java, the lambda calculus, and other dialects of Java. Second is other researchers' variability-aware approaches for data-flow analysis.
##### iii3. New Results:
In this paper, authors purposed a practical, scalable, variability-aware and sampling-based analysis for real-world, large-scale systems written in C. They also did experiments on large-scale system including Linux Kernel and found out that the performance of variability-aware analysis outperforms some of the sampling heuristics and still being complete. They also found out some limitations on pair-wise, sampling heuristics.
##### iii4. Future Work:
Other than pair-wise sampling heuristics, they could also experimenting with other sampling heuristics and studing other large-scale systems and to find out whether the conclusion is still true, such as three-wise sampling heuristics. They could also work on something like how to set up an automated and incremental checking system for producing bug reports.
#### iv. Improvements:
##### iv1.
Future work is a little bit weak, instead of just saying setting up an automated system, authors could also say something about if there are some relevant works could be improved as this is a trend to set up automated systems for producing bug reports.
##### iv2.
Conclusion should be more concrete by listing some of the results got from the comparison and emperical study.
##### iv3.
A small suggestion would also be something like a section on how this paper is structured could be given at the first place so that reader could get a clear mind when going through the paper.
 
