## Reading Assignment 1
#####Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Zexi Chen (jay1204)[student ID: zchen22]

- Shiqian Xu(jessexu20)[student ID: sxu11]

##### i. Reference to the Paper
S. Apel, H. Speidel, P. Wendler, A. von Rhein, and D. Beyer,¡°Detection of feature interactions using feature-aware verification,¡±in ASE. IEEE, 2011, pp. 372¨C375.

##### ii. Most Important Keywords 

<b> ii1. Software product line</b>  
A set of software products that are distinguished in terms of features.

<b>ii2. Feature interactions</b>  
Situations in which the combination of features leads to emergent and possibly critical behavior.

<b> ii3. Feature-aware verification</b>  
The approach of verifying the absence (or detecting the presence) of feature interactions in feature-oriented product
lines.

<b> ii4. Variability encoding</b>  
The procedure of variability encoding is a modification of the regular composition process.
All feature modules are composed according to the total composition order. The resulting product simulator P can simulate the behavior of any product of the product line.

##### iii. Brief notes on items 
<b> iii1. Motivational Statements</b>  
Authors mainly concentrate on two challenges that arise in feature-oriented software product lines:
a) to detect feature interactions based on specifications that do not have global system knowledge;
b) to detect feature interactions without the need of generating and checking all individual products.

<b> iii2. Delivery tools</b>  
Authors have developed the tool chain SPLVERIFIER for featureaware verification and have used it in a case study ¡ªan e-mail client that was developed as a product line¡ª to investigate the potential of feature-aware verification for detecting feature interactions.
SPLVERIFIER and the case study are available on the project's [Web site](http://www.infosun.fim.uni-passau.de/spl/FAV/variability_encoding.html)

<b> iii3. Related works</b>  
In the literature, there are two approaches of product-line verification that can be used for the detection of feature
interactions: 
a) check features as far as possible in isolation; 
b) check the entire product line in a single pass.

Variability encoding is inspired by Post and Sinz's approach [3]. They propose the notion of configuration lifting to efficiently verify variable C code. The key idea is to replace each conditional preprocessor directive (e.g., #ifdef) by a corresponding if statement thus making it accessible to a software verification tool. 

<b> iii4. Data</b>  
The authors conducted their case study on the e-mail system of Hall [4]. It consists of 10 features that give rise to
27 feature interactions. It is divided into a client and a server.

##### iv. Three ways the paper could be improved.  
<b> iv1. More case studies</b>  
Currently, there is only one case study in their work. The conclusion they made can be much more convincing if more experiments are conducted on different data sets.

<b> iv2. Future works</b>  
The authors did not mention any deficiency or any possible improvement of their method. They can add something like this to  provide a clear guild line for future works in this area.

<b> iv3. The result of case study</b>  
The result of case study is shown in another paper [2]. Maybe it is because of the length limit of this paper, but I don't like it.


##### References  
[1] [S. Apel, H. Speidel, P. Wendler, A. von Rhein, and D. Beyer,¡°Detection of feature interactions using feature-aware verification,¡±in ASE. IEEE, 2011, pp. 372¨C375.](http://delivery.acm.org/10.1145/2200000/2190192/06100075.pdf?ip=152.7.76.41&id=2190192&acc=ACTIVE%20SERVICE&key=6ABC8B4C00F6EE47%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&CFID=541401806&CFTOKEN=45181877&__acm__=1440853073_70979f784f9d36da24953b41c85f2999)

[2] [Apel, Sven, Hendrik Speidel, Philipp Wendler, Alexander von Rhein, and Dirk Beyer. "Feature-Aware Verification." arXiv preprint arXiv:1110.0021 (2011).](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.444.5101&rep=rep1&type=pdf)

[3] [H. Post and C. Sinz. Configuration Lifting: Verification meets Software Configuration. In Proc. ASE, pages 347¨C350. IEEE, 2008.](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=4639338&tag=1)

[4] [Hall, Robert J. "Fundamental nonmodularity in electronic mail." Automated Software Engineering 12, no. 1 (2005): 41-79.](http://link.springer.com/article/10.1023/B:AUSE.0000049208.84702.84)