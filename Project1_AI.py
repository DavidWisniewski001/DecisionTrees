import numpy as np
import pandas as pd
import pickle
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier

# Loads a CSV file into the program
def load_csv_file():
    try:
        data = input("Enter file name")
        csv = pd.read_csv(data)
        return(csv)
    except:
        print("CSV file not found please try again")
        load_csv_file()
def 