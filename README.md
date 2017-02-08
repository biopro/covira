#CoVIRA: Consensus by Voting with Iterative Re-weighting based on Agreement

##About

CoVIRA (Consensus by Voting with Iterative Re-weighting based on  Agreement) is an algorithm to generate a consensus prediction based on the results from independent binary predictors by using an unsupervisioned and iterative weighted-voting system. Different from supervisioned ensemble learning methods, such as AdaBoost, CoVIRA doesn't require a dataset of training, as it is based on the measure of the "agreement" between the predictor. As we have no prior knownledge of accuracy of each predictor, we assume that the most accurate will be confirmed more times than those with smaller accuracy, requiring that the degree of accuracy in the set of predictors must be uniform. 

**Table 1.**Example of a dataset with results from three different predictions for the same protein. 

|Protein ID | Predictor 1 | Predictor 2 | Predictor 3 |
|:---------:|:-----------:|:-----------:|:-----------:|
|LIC10010   |	          1 |           0 |           0 |
|LIC10011   |	          0 |           1 |           0 |
|LIC10024	  |           1 |           1 |           0 |
|LIC10125   |           1 |           0 |           0 |
|LIC10307   |           1 |           0 |           0 |
|LIC10371   |           1 |           0 |           0 |
|LIC10468   |           1 |           0 |           0 |
|LIC10647   |           1 |           0 |           1 |


In this example it is possible to see that the results from the Predictor 1 were confirmed by the Predictors 2 and 3 only for a few proteins. Therefore, it is expected that its weight in the final voting might be relatively smaller than the weights of the other programs. When running CoVIRA whith this dataset set, the weight calculated for each predictor is:

- Predictor 1: 0.1875
- Predictor 2: 0.375
- Predictor 3: 0.4375

|Protein ID  | Predictor 1 | Predictor 2 | Predictor 3 | CoVIRA score |
|:----------:|:-----------:|:-----------:|:-----------:|:------------:|
|LIC10010    |	         1 |           0 |           0 | 0.1875       |
|LIC10011    |	         0 |           1 |           0 | 0.375        |
|**LIC10024**|        **1**|        **1**|        **0**|**0.5625**    |
|LIC10125    |           1 |           0 |           0 | 0.1875       |
|LIC10307    |           1 |           0 |           0 | 0.1875       |
|LIC10371    |           1 |           0 |           0 | 0.1875       |
|LIC10468    |           1 |           0 |           0 | 0.1875       |
|**LIC10647**|        **1**|        **0**|        **1**|**0.625**     |

##Using

CoVIRA takes as argument the name of the. The input must be a tab-delimited text file where the first field is an unique identifier of the entry (eg: protein ID), and the others are predictions generated by independent programs. The `test` directory contains some examples of inputs. 

`$ python covira.py dataset.txt`
