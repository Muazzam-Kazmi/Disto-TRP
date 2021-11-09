# -*- coding: utf-8 -*-
"""
    #Created: Thu May 23 10:59:00 2019
    @author: Muazzam Ali
"""

# Load all the packages
import pandas as pd
import numpy as np

# Set Path    
WorkDir = "D:/PROJECT LAB/PAPERS/TRP-Channels/2. DATA/3.Feature sets/";

###############################################################################
# STEP 1 = READ ALL FEATURES
###############################################################################
# Features 1
#train
get_feature1_class1_train = pd.read_csv(WorkDir+"1.Alfafold_distogram/alfafold_distogram_train_class1.csv", encoding='utf-8', header=0);
#test
get_feature1_class1_test = pd.read_csv(WorkDir+"1.Alfafold_distogram/alfafold_distogram_test_class1.csv", encoding='utf-8', header=0);

# Features 2
#train
get_feature2_class1_train = pd.read_csv(WorkDir+"3.BERT_Large_Cased/2.Processed/bert_large_cased_train_class1.csv", encoding='utf-8', header=0);
#test
get_feature2_class1_test = pd.read_csv(WorkDir+"3.BERT_Large_Cased/2.Processed/bert_large_cased_test_class1.csv", encoding='utf-8', header=0);

# Set 2 proper indexes for searching in feature1
#train
get_feature1_class1_train.set_index(['identifier', 'class'], inplace=True); get_feature1_class1_train.update(get_feature1_class1_train);
#test
get_feature1_class1_test.set_index(['identifier', 'class'], inplace=True); get_feature1_class1_test.update(get_feature1_class1_test);


# Set 2 proper indexes for searching in feature1
#train
get_feature2_class1_train.set_index(['identifier', 'class'], inplace=True); get_feature2_class1_train.update(get_feature2_class1_train);
#test
get_feature2_class1_test.set_index(['identifier', 'class'], inplace=True); get_feature2_class1_test.update(get_feature2_class1_test);

# Merge 2 dataframe
#train
final_feature_class1_train = pd.merge(get_feature1_class1_train, get_feature2_class1_train, left_index=True, right_index=True)
#test
final_feature_class1_test = pd.merge(get_feature1_class1_test, get_feature2_class1_test, left_index=True, right_index=True)


# Reset index
#train
final_feature_class1_train.reset_index(inplace=True)
#test
final_feature_class1_test.reset_index(inplace=True)

# Output Path
OUTPUT_PATH_DIR = WorkDir+"7.Distogram+BERT_Large_Cased/";

# Store
#train
final_feature_class1_train.to_csv (OUTPUT_PATH_DIR+"distorgram_bert_large_cased_train_class1.csv", index = None, header=True) # Don't forget to add '.csv' at the end of the path
#test
final_feature_class1_test.to_csv (OUTPUT_PATH_DIR+"distorgram_bert_large_cased_test_class1.csv", index = None, header=True) # Don't forget to add '.csv' at the end of the path



