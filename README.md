# Programming and scripting project 2020

This repository is used for the final project given during the Programming and scripting module on Higher Diploma in Data Analytics course from GMIT.

Detailed project description can be found on [GitHub](https://github.com/ianmcloughlin/project-pands-2020/blob/master/project.pdf) from the lecturer Ian McLoughlin.


## Table of contents
* [Iris dataset information](#iris-dataset)
    * [Iris dataset history](#iris-dataset-history)
    * [Iris dataset file](#iris-dataset-file)
* [Dataset code and analysis](#dataset-code-and-analysis)
    * [Imported libraries and modules](#imported-libraries-and-modules)
        * [Libraries cheat sheets](#libraries-cheat-sheets)
    * [Dataset import](#dataset-import)
    * [Dataset summary](#datasetsummary)
        * [Summary of the values - describe()](#summary-of-the-values---describe())
        * [Samples of each type - info()](#samples-of-each-type---info())
* [Plots](#plots)
    * [Histograms](#histograms)
        * [Histogram code](#histogram-code)
    * [Scatterplots](#scatterplots)
* [References](#references)
    * [Worthy mentions](#worthy-mentions)
    * [Dataset analysis approach by others](#dataset-analysis-approach-by-others)

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

# **Dataset code and analysis**

In this section is explanation of the code for the imported libraries, dataset import and summary. Code used for plotting is explained in [Plots](#plots).

## **Imported libraries and modules**

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sys

***NumPy*** is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.\
Shorter definition is thah *NumPy* is the fundamental package for scientific computing in Python. [04]\
Geeksforgeeks. com has an interesting two part tutorial on *NumPy* referenced in [Worthy mentions](#worthy-mentions).


***pandas*** is a Python package for data science; it offers data structures for data manipulation and analysis. [05]\
In this project *pandas* is used for creating a summary of the dataset from a .csv file.\
More useful information about *pandas* can be found on [Towards data science](https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673), [Real python.com](https://realpython.com/pandas-dataframe/) and [Pandas.pydata.org](https://pandas.pydata.org/docs/#).


***Matplotlib*** is a comprehensive visualisation library in Python, built on NumPy arrays, for creating static, animated and interactive 2D plots or arrays. [06] [07]\
*matplotlib.pyplot* is a state-based interface to *matplotlib*. It provides a MATLAB-like way of plotting. *pyplot* is mainly intended for interactive plots and simple cases of programmatic plot generation. [08]

***Seaborn*** is a library for making statistical graphics in Python. It is built on top of matplotlib and closely integrated with pandas data structures. [09]\
Working with DataFrames is a bit easier with the Seaborn because the plotting functions operate on DataFrames and arrays that contain a whole dataset. [10]\
[Elite data science](https://elitedatascience.com/python-seaborn-tutorial) has interesting tutorial on *seaborn* presented on a famous Pokemon cartoon based dataset.

***sys*** module represents system-specific parameters and functions and provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. [11]
Interesting tutorial on *sys* can be found on [Python programming](https://pythonprogramming.net/sys-module-python-3/) and [Data Flair](https://data-flair.training/blogs/python-sys-module/).


### **Libraries cheat sheets**

List of usefull cheat sheets for libraries used in this project:
* [NumPy 1](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
* [NumPy 2](https://s3.amazonaws.com/dq-blog-files/numpy-cheat-sheet.pdf)
* [pandas](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
* [Matplotlib](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)
* [Seaborn](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf)

## **Dataset import**

    ifds = pd.read_csv("dataset.csv", index_col="Id")

This line of code is used for reading the .csv file into DataFrame and storing it as a variable *ifds* (iris flower dataset) for further analysis and manipulation.\
Since *pandas* is using zero-based integer indices in the DataFrame,  *index_col="Id"* was used to make the Id column an index column while reading the file. That means that the index column will not be taken into consideration while analysing the data. [12]

## **Dataset summary**

Part of the code for summary:

    def summary_to_file():
        sys.stdout = open ("analysis_summary.txt","w")
        ...
        print(ifds)
        ...
        print (ifds.describe())
        ...
        print (ifds.info())
        ...
        print (ifds["Species"].value_counts())
        ...
        print (((ifds["Species"].value_counts(normalize=True))*100))
        sys.stdout.close()

Dataset summary is not shown while starting the program, but rather stored in [analysis_summary.txt](https://github.com/sandraelekes/pands-project-2020/blob/master/analysis_summary.txt).

Function *summary_to_file()* is created for making the summary and writing it into the file at the same time.

Writing outputs of the summary into a file is achieved with use of *sys* module and it's attribute *stdout*. *stdout* (standard output stream) is simply a default place to send a program’s text output. [13] [14]\
Initial idea was to create a function with outputs of summary and write that output into a .txt file. After a long research and "trial and error technique" it seemed to complicated to code and this approach is chosen over writing in file with the help of .write(), because code is simpler and any *print* operation will write it's output to a .txt file, where .write() function only takes string value as an input(). [15] [16] [17]

*ifds* is giving the overview of the whole dataset loaded from the Iris_dataset.csv file.

### **Summary of the values - describe()**
*ifds.describe()* gives the summary of the numeric values in the given dataset. It shows the count of variables in the dataset which can point out to any possible missing values. It calculates the mean, standard deviation, minimum and maximum value, and also 1st, 2nd and 3rd percentile of the columns with numeric value. [18]

<details>
           <summary>Output</summary>
           <p>

           SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm
    count     150.000000    150.000000     150.000000    150.000000
    mean        5.843333      3.054000       3.758667      1.198667
    std         0.828066      0.433594       1.764420      0.763161
    min         4.300000      2.000000       1.000000      0.100000
    25%         5.100000      2.800000       1.600000      0.300000
    50%         5.800000      3.000000       4.350000      1.300000
    75%         6.400000      3.300000       5.100000      1.800000
    max         7.900000      4.400000       6.900000      2.500000

</p>
</details>

### **Samples of each type - info()**

*ifds. info()* prints information about given dataset including the index data type and column data types, non-null values and memory usage. [18]

<details>
           <summary>Output</summary>
           <p>

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 150 entries, 1 to 150
    Data columns (total 5 columns):
    SepalLengthCm    150 non-null float64
    SepalWidthCm     150 non-null float64
    PetlLengthCm     150 non-null float64
    PetalWidthCm     150 non-null float64
    Species          150 non-null object
    dtypes: float64(4), object(1)
    memory usage: 7.0+ KB
</p>
</details>



### **Number of occurances of each of the species**

Method *value_counts()* is used to count the number of desired columns. In this case, the column of interest is column *Species*. [19]\
With defining the parameter *normalise* to *True* (it is *False* by default), these values can be presented in percentile (or relative frequencies) as well. [20]  


<details>
           <summary>Output</summary>
           <p>

    Iris-virginica     50
    Iris-versicolor    50
    Iris-setosa        50
    Name: Species, dtype: int64

Or, viewed in percentile:

    Iris-setosa        33.333333
    Iris-versicolor    33.333333
    Iris-virginica     33.333333
    Name: Species, dtype: float64

</p>
</details>

# Plots

## Histograms

![alt text](https://github.com/sandraelekes/pands-project-2020/blob/master/Sepal-lenght.png "Sepal length in cm")

![alt text](https://github.com/sandraelekes/pands-project-2020/blob/master/Petal-lenght.png "Petal length in cm")

### Histogram code
Histograms are coded with the help of functions. There are 4 functions representing each histogram: Sepal Length, Sepal Width, Petal Length and Petal Width.

Example of part of the code:


    iris_s = ifds[ifds.Species == "Iris-setosa"]
    iris_vers = ifds[ifds.Species == "Iris-versicolor"]
    iris_virg = ifds[ifds.Species == "Iris-virginica"]

    def petal_length_hist():
        plt.figure(figsize=(9,9))
        sns.distplot(iris_s["PetalLengthCm"],  kde=False, label="Iris setosa", color="deeppink")
        sns.distplot(iris_vers["PetalLengthCm"],  kde=False, label="Iris versicolor", color="purple")
        sns.distplot(iris_virg["PetalLengthCm"],  kde=False, label="Iris virginica", color="navy")
        plt.title("Petal length in cm", size = 20)
        plt.xlabel("")
        plt.ylabel("Frequency", size = 16)
        plt.legend()
        plt.savefig("Petal-lenght.png")
        plt.show()


Variables *iris_s*, *iris_vers* and *iris_virg* are used for subsetting original dataframes for Iris setosa, Iris versicolor and Iris virginica, respectively. They are set outside of the functions for multiple use.[21]

Lot of parameters in codes are added for aesthetic purposes only. Example od that is adding size to title and labels text. [22]
*figsize* is defined as 9 by 9 inches so on the saved picture the legend wouldn't be positioned over the histogram. Important to notice - figure size must be defined before start of plotting. [23]

*distplot()* is a function used to flexibly plot a univariate distribution of observations. [24] \
Parameter *kde* (kernel density estimate) is set to False as it was unnecessary in this case.\
Parameter *color* was set for a better distinction between species of flowers and nicer picture. [25]\




## Scatterplots

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
[05] [Datacamp. Pandas tutorial](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python)\
[06] [Geeksforgeeks. Introduction mathplotlib](https://www.geeksforgeeks.org/python-introduction-matplotlib/)\
[07] [Matplotlib.org](https://matplotlib.org/)\
[08] [Matplotlib.org. Matplotlib.pyplot](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot)\
[09] [Seaborn. Introduction.](https://seaborn.pydata.org/introduction.html)\
[10] [Datacamp. Seaborn Python tutorial](https://www.datacamp.com/community/tutorials/seaborn-python-tutorial#sm)\
[11] [Python.org. Sys](https://docs.python.org/3/library/sys.html)\
[12] [Real python. Python csv.](https://realpython.com/python-csv/)\
[13] [Lutz, M. (2009)."Learning Python", pg. 303](https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf)\
[14] [StackOverflow.Sys.stdout](https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print)\
[15] [Real Python. Read Write files Python](https://realpython.com/read-write-files-python/)\
[16] [Geeksforgeeks. Reading and writing text files](https://www.geeksforgeeks.org/reading-writing-text-files-python/)\
[17] [StackOverflow. Python writing function output to a file.](https://stackoverflow.com/questions/28356648/python-writing-function-output-to-a-file)\
[18] [Towards Data Science. Getting started to data analysis with Python pandas](https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77)\
[19] [Medium. Exploratory data analysis.](https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d)\
[20] [Towards Data Science. Getting more value from the *pandas* value counts.](https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6)\
[21] [Cmdline tips. How to make histogram in python with pandas and seaborn.](https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/)\
[22] [StackOverflow. Text size of x and y axis and the title on matplotlib.](https://stackoverflow.com/questions/27350226/how-to-make-the-text-size-of-the-x-and-y-axis-labels-and-the-title-on-matplotlib/27350945)\
[23] [StackOverflow. Change size of figures drawn with matplotlib.](https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib)\
[24] [Seaborn.pydata. Seaborn.distplot](https://seaborn.pydata.org/generated/seaborn.distplot.html#seaborn.distplot)\
[25] [Python graph gallery](https://python-graph-gallery.com/196-select-one-color-with-matplotlib/)\



## Worthy mentions

This is the list of sources that have not been used in analysis or summary of the Iris dataset but rather for better understanding of requirements for the project, researching how to edit the readme file and also interesting sources worth of reading.

* [Fisher, R. A. (1936). “The Use of Multiple Measurements in Taxonomic Problems”](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)
* [Github. Deleting files.](https://help.github.com/en/github/managing-files-in-a-repository/deleting-files)
* [Towards data science. Introduction to pandas.](https://towardsdatascience.com/a-quick-introduction-to-the-pandas-python-library-f1b678f34673)
* [Geeksforgeeks. NumPy - Introduction](https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/)
* [Geeksforgeeks. NumPy - Advanced](https://www.geeksforgeeks.org/numpy-python-set-2-advanced/?ref=lbp)
* [Real python. Pandas DataFrame](https://realpython.com/pandas-dataframe/)
* [Pandas.pydata.org](https://pandas.pydata.org/docs/#)
* [Elite data science. Seaborn tutorial.](https://elitedatascience.com/python-seaborn-tutorial)
* [Python programming. Sys module.](https://pythonprogramming.net/sys-module-python-3/)
* [Data Flair. Python sys module](https://data-flair.training/blogs/python-sys-module/)
* [Python graph gallery](https://python-graph-gallery.com/)

## Dataset analysis approach by others

* https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/
* https://www.kaggle.com/abhishekkrg/python-iris-data-visualization-and-explanation
* https://www.kaggle.com/aschakra/iris-data-visualization-using-python