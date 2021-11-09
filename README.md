# Disto-TRP

## Introduction
In this study we proposed a method named as Disto-TRP, that utilized the structural information obtained from AlphaFold to effectively identifying Transient Receptor Potential (TRP) channels.

Understanding the structure of protein is quite important since it assist to understand the function of proteins. Prediction of protein structure is a challenging task from many decades. Recently, the DeepMind released the latest version of AlphaFold that attempts to predict the structure of proteins. 

A Distogram is a distance matrix that contains information about the distance between the pairs of amino acids. AlphaFold generates this distogram based on the represntations of the target protein sequence and the features of the corresponding muliple sequence alighment (MSA). We used Distogram as novel feature set to develop our method.

## Methodogoy
We combined the Distogram features with the features from various BERT models to construct a hybrid feature set and utilized the resultant composite feature set as input to the Support Vector Machine (SVM) Classifier to classify TRP channels from general channel proteins.

## Comparison of our method with exisiting techniques
We compared our method with different feature generation methods:
* Amino Acid Composition (AAC)
* Dipeptide Composition (DPC)
* Position Specific Scoring Matrices (PSSM)

We also compared our method with using various classifiers:
* Extra Trees Classifier (EXT)
* Random Forest Classifier (RFC)
* Support Vector Machine (SVM)

We also compared our method with our previous study
* TRP-BERT
* Disto-TRP

We further assess the performance of our method with composite features of Distogram with domain specific BERT models:
* BioBERT
* TAPE (Tasks Assessing Protein Embeddings) BERT




