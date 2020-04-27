import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def write_to_file():

# variable ifds stands for iris flower dataset
# with read.csv() we are reading the .csv file and storing it into ifds variable for further use and manipulation
# with "index_col='Id'" I am eliminating the Id column as it is unnecessary in this case
# reference for index_col: https://realpython.com/python-csv/
    sys.stdout = open ("analysis_summary.txt","w")
    print ("\n")
    print(ifds)
    print ("\n")
    print (ifds.describe())
    print ("\n")
    print (ifds.info())
    print ("\n")

    #https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
    print (ifds["Species"].value_counts())
    sys.stdout.close()

ifds = pd.read_csv('dataset.csv', index_col='Id')
write_to_file()