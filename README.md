#CoVIRA: Consensus by Voting with Iterative Re-weighting based on Agreement

CoVIRA (Consensus by Voting with Iterative Re-weighting based on  Agreement) is an algorithm to generate a consensus prediction based on the results from independent binary predictors by using an unsupervisioned and iterative weighted-voting system. Different from supervisioned ensemble learning methods, such as AdaBoost, CoVIRA doesn't require a dataset of training, as it is based on the measure of the "agreement" between the predictor. In this case, those those predictors 

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

