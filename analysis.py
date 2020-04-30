import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def summary_to_file():
    # idea for sys.stdout: https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print
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
    # reference for idea: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
    print (ifds["Species"].value_counts())
    print ("\n")
    print("     In percentile:")
    print("\n")
    # reference for normalize=True: https://towardsdatascience.com/getting-more-value-from-the-pandas-value-counts-aa17230907a6
    print (((ifds["Species"].value_counts(normalize=True))*100))
    print("\n")
    print ("==============================================================================")
    sys.stdout.close()

# function for plotting histogram for sepal length
def sepal_length_hist():
     # reference for figsize: https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
    plt.figure(figsize = (9,9))
    
    # reference for plotting multiple histograms on one plot with different colors:
    # https://cmdlinetips.com/2019/02/how-to-make-histogram-in-python-with-pandas-and-seaborn/
    sns.distplot(iris_s["SepalLengthCm"],  kde = False, label = "Iris setosa", color = "deeppink", )
    sns.distplot(iris_vers["SepalLengthCm"],  kde = False, label = "Iris versicolor", color = "mediumorchid")
    sns.distplot(iris_virg["SepalLengthCm"],  kde = False, label = "Iris virginica", color = "navy")
    plt.title("Sepal length in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Sepal-lenght.png")
    plt.show()

#function for plotting a histogram for sepal width
def sepal_width_hist():
    plt.figure(figsize = (9,9))
    sns.distplot(iris_s["SepalWidthCm"],  kde = False, label = "Iris setosa", color = "deeppink")
    sns.distplot(iris_vers["SepalWidthCm"],  kde=False, label = "Iris versicolor", color = "mediumorchid")
    sns.distplot(iris_virg["SepalWidthCm"],  kde=False, label = "Iris virginica", color = "navy")
    plt.title("Sepal width in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Sepal-width.png")
    plt.show()

# function for plotting a histogram for petal length
def petal_length_hist():
    plt.figure(figsize = (9,9))
    sns.distplot(iris_s["PetalLengthCm"],  kde = False, label = "Iris setosa", color = "deeppink")
    sns.distplot(iris_vers["PetalLengthCm"],  kde = False, label = "Iris versicolor", color = "mediumorchid")
    sns.distplot(iris_virg["PetalLengthCm"],  kde = False, label = "Iris virginica", color = "navy")
    plt.title("Petal length in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Petal-lenght.png")
    plt.show()

# function for plotting a histogram for petal width
def petal_width_hist():
    plt.figure(figsize = (9,9))
    sns.distplot(iris_s["PetalWidthCm"],  kde = False, label = "Iris setosa", color = "deeppink")
    sns.distplot(iris_vers["PetalWidthCm"],  kde = False, label = "Iris versicolor", color = "mediumorchid")
    sns.distplot(iris_virg["PetalWidthCm"],  kde = False, label = "Iris virginica", color = "navy")
    plt.title("Petal width in cm", size = 20)
    plt.xlabel("")
    plt.ylabel("Frequency", size = 16)
    plt.legend()
    plt.savefig("Petal-width.png")
    plt.show()

# function for uniting all the functions for creating histograms
def histograms():
    sepal_length_hist()
    sepal_width_hist()
    petal_length_hist()
    petal_width_hist()

# function for plotting a scatterplot for sepal length and width
def sepal_length_width_scat():
    plt.figure(figsize = (9,9))
    # reference for scatterplot: https://honingds.com/blog/seaborn-scatterplot/
    # https://seaborn.pydata.org/generated/seaborn.scatterplot.html
    # reference for marker: https://matplotlib.org/3.1.1/api/markers_api.html
    # reference for scatter outline: https://seaborn.pydata.org/generated/seaborn.scatterplot.html
    # https://stackoverflow.com/questions/50706901/matplotlib-border-around-scatter-plot-points
    sns.scatterplot(x = "SepalLengthCm", y = "SepalWidthCm", data = ifds, marker = "o", hue = "Species", palette = ["deeppink","mediumorchid","navy"], edgecolor = "dimgrey")
    plt.title("Sepal length and Sepal width comparison", size = 20)
    plt.xlabel("Sepal length", size = 16)
    plt.ylabel("Sepal width", size = 16)
    plt.legend()
    plt.savefig("Sepal-length-width.png")
    plt.show()

# function for plotting a scatterplot for petal length and width
def petal_length_width_scat():
    plt.figure(figsize = (9,9))
    sns.scatterplot(x = "PetalLengthCm", y = "PetalWidthCm", data = ifds, marker = "o", hue = "Species", palette = ["deeppink","mediumorchid","navy"], edgecolor = "dimgrey")
    plt.title("Petal length and Petal width comparison", size = 20)
    plt.xlabel("Petal length", size = 16)
    plt.ylabel("Petal width", size = 16)
    plt.legend()
    plt.savefig("Petal-length-width.png")
    plt.show()

# function for uniting all the functions for creating scatterplots
def scatterplots():
    sepal_length_width_scat()
    petal_length_width_scat()

# function for plotting pairplot
def pairplot():
    sns.pairplot(ifds, hue = "Species", diag_kind = "hist", palette = ["deeppink","mediumorchid","navy"])
    plt.savefig("Iris-dataset-pairplot.png")
    plt.show()


# main part of the code

# index_col = "Id" was used to make the Id column an index column
# reference for index_col: https://realpython.com/python-csv/

ifds = pd.read_csv("Iris_dataset.csv", index_col = "Id")

summary_to_file()

iris_s = ifds[ifds.Species == "Iris-setosa"]
iris_vers = ifds[ifds.Species == "Iris-versicolor"]
iris_virg = ifds[ifds.Species == "Iris-virginica"]

histograms()
scatterplots()
pairplot()
