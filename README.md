# Programming and scripting project 2020

This repository is used for the final project given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.

Detailed project description can be found on [GitHub](https://github.com/ianmcloughlin/project-pands-2020/blob/master/project.pdf) from the lecturer Ian McLoughlin.


## Table of contents
* [Iris dataset information](#iris-dataset)
    * [Iris dataset history](#iris_dataset_history)
    * [Iris dataset file](#iris_dataset_file)
* [Python code](#python_code)
    * [Imported libraries and modules](#imported_libraries_and_modules)
        * [Libraries cheat sheets](#libraries_cheat_sheets)
    * [Dataset import](#dataset_import)
    * [Dataset summary](#dataset_summary)
* [References](#references)
    * [Worthy mentions](#worthy-mentions)

# **Iris dataset**

## **Iris dataset history**

Iris flower data, also known as Fisher's Iris dataset was introduced by British biologist and statistitian Sir Ronald Aylmer Fisher. In 1936, Sir Fisher published a report titled [“The Use of Multiple Measurements in Taxonomic Problems”](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x) in the journal Annals of Eugenics. Sir Fisher didn’t collect these data himself. Credits for the data source go to Dr. Edgar Anderson, who collected the majority of the data at the Gaspé Peninsula.\
In this article, Fisher developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers. It was the first time that the sepal and petal measures of the three Iris species as mentioned above appeared publicly. [01]

Iris flower difference in species is pictured below. [02]

![alt text](https://github.com/sandraelekes/pands-project-2020/blob/master/iris-species.png "Iris flower species")


## **Iris dataset file**

This Iris dataset contains a set of 150 records which represent three iris species (*Iris setosa*, *Iris versicolor* and *Iris virginica*) with 50 samples each. 

The columns that represent records mentioned above are :

* Id
* SepalLengthCm
* SepalWidthCm
* PetalLengthCm
* PetalWidthCm
* Species


Iris dataset [03] used in this analysis can be found among files in this repository as [Iris_dataset.csv](https://github.com/sandraelekes/pands-project-2020/blob/master/Iris_dataset.csv).

# **Python code**

## **Imported libraries and modules**

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sys

***NumPy*** is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.\
Shorter definition is thah *NumPy* is the fundamental package for scientific computing in Python. [04]\
Geeksforgeeks.com has an interesting two part tutorial on *NumPy*. [05][06]\


***pandas*** is a Python package for data science; it offers data structures for data manipulation and analysis. [07]\
In this project *pandas* is used for creating a summary of the dataset from a .csv file.\
More useful information about *pandas* can be found on [Towards data science](https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673), [Real python.com](https://realpython.com/pandas-dataframe/) and [Pandas.pydata.org](https://pandas.pydata.org/docs/#).


***Matplotlib*** is a comprehensive visualisation library in Python, built on NumPy arrays, for creating static, animated and interactive 2D plots or arrays. [08][09]\
*matplotlib.pyplot* is a state-based interface to *matplotlib*. It provides a MATLAB-like way of plotting. *pyplot* is mainly intended for interactive plots and simple cases of programmatic plot generation. [10]

***Seaborn*** is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures. [11]\
Working with DataFrames is a bit easier with the Seaborn because the plotting functions operate on DataFrames and arrays that contain a whole dataset. [12]\
[Elite data science](https://elitedatascience.com/python-seaborn-tutorial) has interesting tutorial on *seaborn* presented on a famous Pokemon cartoon based dataset.

***sys*** module represents system-specific parameters and functions and provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. [13]
Interesting tutorial on *sys* can be found on [Python programming](https://pythonprogramming.net/sys-module-python-3/) and [Data Flair](https://data-flair.training/blogs/python-sys-module/).


### **Libraries cheat sheets**

List of usefull cheat sheets for libraries used in this project:
* [NumPy 1](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
* [NumPy 2](https://s3.amazonaws.com/dq-blog-files/numpy-cheat-sheet.pdf)
* [pandas](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
* [Matplotlib](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)
* [Seaborn](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)

## Dataset import 

    ifds = pd.read_csv("dataset.csv", index_col="Id")

This line of code is used for reading the .csv file into DataFrame and storing it as a variable *ifds* (iris flower dataset) for further analysis and manipulation.\
Since *pandas* is using zero-based integer indices in the DataFrame,  *index_col="Id"* was used to make the Id column an index column while reading the file. [14]

## Dataset summary

    def summary_to_file():
        sys.stdout = open ("analysis_summary.txt","w")
        print ("\n")
        print ("Overview of the whole dataset:")
        print ("\n")
        print(ifds)
        print ("\n")
        print ("Summary of numeric values: ")
        print ("\n")
        print (ifds.describe())
        print ("\n")
        print ("Number of samples of each type:")
        print ("\n")
        print (ifds.info())
        print ("\n")
        print("Number of occurances of each of the species:")
        print ("\n")
        print (ifds["Species"].value_counts())
        sys.stdout.close()

Dataset summary is not shown while starting the program, but rather stored in [analysis_summary.txt](https://github.com/sandraelekes/pands-project-2020/blob/master/analysis_summary.txt).

Function *summary_to_file()* is created for making the summary and writing it into the file at the same time.

Writing outputs of the summary into a file is achieved with use of *sys* module and it's attribute *stdout*. *stdout* (standard output stream) is simply a default place to send a program’s text output.[15][16]\
Initial idea was to create a function with outputs of summary and write that output into a .txt file. After a long research and "trial and error technique" it seemed to complicated to code and this approach is chosen over writing in file with the help of .write(), because code is simpler and any *print* operation will write it's output to a .txt file, where .write() function only takes string value as an input(). [17][18][19]



# Technologies used

* Visual Studio Code - version 1.44.2
* cmder - version 1.3.14.982
* python - version 3.7.4.final.0
* Anaconda3 - 2019.10
* Notepad++ - version 7.8.5
* Mozzila Firefox 75.0 (64-bit)

# References

[01] [Towards data science. The Iris dataset - A little bit of history and biology](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)\
[02] [The Good Python. Iris dataset.](https://thegoodpython.com/iris-dataset/)\
[03] [Kaggle. UCI Machine learning. Iris dataset download.](https://www.kaggle.com/uciml/iris/download)\
[04] [Numpy.org. What is Numpy?](https://numpy.org/devdocs/user/whatisnumpy.html)\
[05] [Geeksforgeeks. Introduction](https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/)\
[06] [Geeksforgeeks. Advanced](https://www.geeksforgeeks.org/numpy-python-set-2-advanced/?ref=lbp)\
[07] [Datacamp. Pandas tutorial](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python)\
[08] [Geeksforgeeks. Introduction mathplotlib](https://www.geeksforgeeks.org/python-introduction-matplotlib/)\
[09] [Matplotlib.org](https://matplotlib.org/)\
[10] [Matplotlib.org. Matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)\
[11] [Seaborn. Introduction.](https://seaborn.pydata.org/introduction.html)\
[12] [Datacamp. Seaborn Python tutorial](https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#sm)\
[13] [Python.org. Sys](https://docs.python.org/3/library/sys.html)\
[14] [Real python. Python csv.](https://realpython.com/python-csv/)\
[15] [Lutz, M. (2009)."Learning Python", pg. 303](https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf)\
[16] [StackOverflow.Sys.stdout](https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print)\
[17] [Real Python. Read Write files Python](https://realpython.com/read-write-files-python/)\
[18] [Geeksforgeeks. Reading and writing text files](https://www.geeksforgeeks.org/reading-writing-text-files-python/)\
[19] [StackOverflow. Python writing function output to a file.](https://stackoverflow.com/questions/28356648/python-writing-function-output-to-a-file)\
[20] 


## Worthy mentions

This is the list of sources that have not been used in analysis or summary of the Iris dataset but rather for better understanding of requirements for the project, researching how to edit the readme file and also interesting sources worth of reading.

* [Fisher, R. A. (1936). “The Use of Multiple Measurements in Taxonomic Problems”](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)
* [Github. Deleting files.](https://help.github.com/en/github/managing-files-in-a-repository/deleting-files)
* [Towards data science. Introduction to pandas.](https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673)
* [Real python. Pandas DataFrame](https://realpython.com/pandas-dataframe/)
* [Pandas.pydata.org](https://pandas.pydata.org/docs/#)
* [Elite data science. Seaborn tutorial.](https://elitedatascience.com/python-seaborn-tutorial)
* [Python programming. Sys module.](https://pythonprogramming.net/sys-module-python-3/)
* [Data Flair. Python sys module](https://data-flair.training/blogs/python-sys-module/)

## Dataset analysis approach by others

* https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/
* https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
* https://www.kaggle.com/aschakra/iris-data-visualization-using-python