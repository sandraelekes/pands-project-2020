# Programming and scripting project 2020

This repository is used for the final project given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.

Detailed project description can be found on [GitHub](https://github.com/ianmcloughlin/project-pands-2020/blob/master/project.pdf) from the lecturer Ian McLoughlin.


## Table of contents
* [Iris dataset information](#iris-dataset)
    * [Iris dataset history](#iris_dataset_history)
    * [Iris dataset file](#iris_dataset_file)
* [Python code](#python_code)
    * [Libraries used](#libraries_used)
    * [Data import](#data_import)
    * [Data summary](#data_summary)
* [References](#references)
    * [Worthy reference mentions](#worthy-reference-mentions)

# Iris dataset

## **Iris dataset history**

Iris flower data, also known as Fisher's Iris dataset was introduced by British biologist and statistitian Sir Ronald Aylmer Fisher. In 1936, Sir Fisher published a report titled [“The Use of Multiple Measurements in Taxonomic Problems”](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x) in the journal Annals of Eugenics. Sir Fisher didn’t collect these data himself. Credits for the data source go to Dr. Edgar Anderson, who collected the majority of the data at the Gaspé Peninsula.\
In this article, Fisher developed and evaluated a linear function to differentiate Iris species based on the morphology of their flowers. It was the first time that the sepal and petal measures of the three Iris species as mentioned above appeared publicly. [1]

Iris flower difference in species is pictured below. [2]

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


Iris dataset [3] used in this analysis can be found among files in this repository as [Iris_dataset.csv](https://github.com/sandraelekes/pands-project-2020/blob/master/Iris_dataset.csv).

# Python code

## Libraries used

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sys

***NumPy*** is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.\
Shorter definition is thah *NumPy* is the fundamental package for scientific computing in Python. [4]\
Geeksforgeeks.com has an interesting two part tutorial on *NumPy*. [5][6]\
Also, there are two good cheetsheets for NumPy: [Data science cheetsheet](https://s3.amazonaws.com/dq-blog-files/numpy-cheat-sheet.pdf) and [Datacamp cheetsheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf).

***pandas*** is a Python package for data science; it offers data structures for data manipulation and analysis. [7]\
In this project *pandas* is used for creating a summary of the dataset from a .csv file.\
More useful information about *pandas* can be found on [Towards data science](https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673), [Real python.com](https://realpython.com/pandas-dataframe/) and [Pandas.pydata.org](https://pandas.pydata.org/docs/#).\
Very useful thing for quick check when working with *pandas* is [cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf).







## Data import 



## Data summary


# References

[1] [Towards data science. The Iris dataset - A little bit of history and biology](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5)\
[2] [The Good Python. Iris dataset.](https://thegoodpython.com/iris-dataset/)\
[3] [Kaggle. UCI Machine learning. Iris dataset download.](https://www.kaggle.com/uciml/iris/download)\
[4] [Numpy.org. What is Numpy?](https://numpy.org/devdocs/user/whatisnumpy.html)\
[5] [Geeksforgeeks. Introduction](https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/)\
[6] [Geeksforgeeks. Advanced](https://www.geeksforgeeks.org/numpy-python-set-2-advanced/?ref=lbp)\
[7] [Datacamp. Pandas tutorial](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python)\
[8]



## Worthy reference mentions

This is the list of sources that have not been used in analysis or summary of the Iris dataset but rather for better understanding of requirements for the project, researching how to edit the readme file and also interesting sources worth of reading.

* [Fisher, R. A. (1936). “The Use of Multiple Measurements in Taxonomic Problems”](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)

* [Github. Deleting files.](https://help.github.com/en/github/managing-files-in-a-repository/deleting-files)