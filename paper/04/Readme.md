## Reading Assignment 4
###Group Members:

- Zhe Yu (azhe825)[student ID: zyu9]

- Zexi Chen (jay1204)[student ID: zchen22]

- Shiqian Xu(jessexu20)[student ID: sxu11]

### i. Reference to the Paper
Apel, Sven, Christian Kastner, and Christian Lengauer. "FEATUREHOUSE: Language-independent, automated software composition." In Proceedings of the 31st International Conference on Software Engineering, pp. 221-231. IEEE Computer Society, 2009.


### ii. Most Important Keywords

#### ii1. superimposition: 
the process of composing software artifacts by merging their correspond- ing substructures

#### ii2. feature structure tree(FST):
A general model of the structure of software artifacts,which are designed to represent any kind of artifact with a hierarchical structure and can represent the essential modular structure of a software artifact and abstracts from language-specific details.

#### ii3. software composition:
The process of constructing software systems from a set of software artifacts.

#### ii4. software artifacts: 
Any kind of information that is part of or related to software, e.g., code units (packages, classes, methods, etc.) or supporting documents (models, documentation, make- files, etc.)


#### ii5. FEATUREHOUSE: 
A general architecture of software composition supported by a framework and tool chain, which provides facilities for feature composi- tion based on a language-independent model of software artifacts and an automatic plug-in mechanism for the inte- gration of new artifact languages

### iii. Brief notes on items

#### iii1. Motivational Statements
The authors notice that even though there exist various tools that can support superimposition for code and non-code artifacts, most of the tools are different and dedicated to and embeded in host languages. They mention the integration of the tools should require great effort, which will hinder coordinated efforts to advance composition technology.

#### iii2. Related Work
The authors have read many related paper to investigate the existing work done by other researchers and found many existing tools. However, these tools are limited due to the single language limitation, therefore, they still think it is necessary to propose a general approach to software composition which will be applicable to different languages.

#### iii3. Baseline results
The authors compare the FEATUREHOUSE approach with the approach taken previously by FSTCOMPOSER, which respectively called generative way and manual way. They compare the two methods in various ways such as Granularity, Boilerplate code, Composition rules, Expenditure of time, Susceptibility to error. Based on the above, they are able to evaluate the system they built.

#### iii4. Future work

After they finishes this paper, they are still working on a formalization of the FST model and tools to be integrated into FEATUREHOUSE. They actually have given a very solid idea on features of the tool. They are also interested in integrating the XML much better with FST model and evaluating the possibility whether FEATUREBNF can be replaced by XML.

### iv. Three ways the paper could be improved.
#### iv1. More detailed Comparison
The authors only give narrative details on the new tool's performance. Maybe more visualized data set and graphs could make readers to understand the performance better.

#### iv2. More languages
The authors mention that superimposition is applicable to a wide range of languages including object-oriented languages, functional languages, imperative languages, document description languages, however, in most of cases on the dataset, they are using Java and C++. I am wondering if more diverse languages can be used for the test cases.

#### iv3. Structure Issue
It seems that the authors have not given a summary in the beginning of the paper on how the paper is composed. They should tell the reader about section summaries.

### v. Connection with other paper
In paper "An Overview of Feature-Oriented Software Development" by Apel, Sven, and Christian Kästner, Journal of Object Technology 8, no. 5 (2009): 49-84, the authors mentioned that the trend to explore the principles of feature modularity separate from a particular language. They mentions that the integration of new languages into the AHEAD tools suite was ad hoc and tedious. However, the FeatureHouse which this paper produced provides an easy-to-use plug-in mechanism for new languages, makeing many different languages prepared for implementing and composing features.

### References  
[1] [Apel, Sven, Christian Kastner, and Christian Lengauer. "FEATUREHOUSE: Language-independent, automated software composition." In Proceedings of the 31st International Conference on Software Engineering, pp. 221-231. IEEE Computer Society, 2009.](http://dl.acm.org/citation.cfm?id=1555038)
