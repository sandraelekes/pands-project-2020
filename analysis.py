import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def summary_to_file():
    #idea for sys.stdout: https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
    sys.stdout = open ("analysis_summary.txt","w")
    print ("\n")
    print ("==============================================================================")
    print ("Overview of the whole dataset:")
    print ("\n")
    print(ifds)
    print ("\n")
    print ("==============================================================================")
    print ("Summary of numeric values: ")
    print ("\n")
    # reference for .describe() and .info(): https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77
    print (ifds.describe())
    print ("\n")
    print ("==============================================================================")
    print ("Number of samples of each type:")
    print ("\n")
    print (ifds.info())
    print ("\n")
    print ("==============================================================================")
    print("Number of occurances of each of the species:")
    print ("\n")
    #reference for idea: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
    print (ifds["Species"].value_counts())
    print ("\n")
    print("     In percentile:")
    print("\n")
    #reference for normalize=True: https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
    print (((ifds["Species"].value_counts(normalize=True))*100))
    print("\n")
    print ("==============================================================================")
    sys.stdout.close()

# variable ifds stands for iris flower dataset
# with read.csv() we are reading the .csv file into DataFrame and storing it as ifds variable for further use and manipulation
# index_col="Id" was used to make the Id column an index column
# reference for index_col: https://realpython.com/python-csv/
ifds = pd.read_csv("dataset.csv", index_col="Id")
summary_to_file()