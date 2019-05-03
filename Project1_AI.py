import numpy as np
import pandas as pd
import pickle
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import preprocessing
from collections import OrderedDict as Dict
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.tree import export_graphviz
import graphviz

# Loads a CSV file into the program
def load_csv_file():
    try:
        # Reads in csv file and drops unnecessary data
        csv = input("Enter file name")
        data = pd.read_csv(csv).dropna()
        return(data)
    
    except:
        print("CSV file not found please try again")
        load_csv_file()  
        
# Gets the target column from the user
def get_target_column(data):
    try:
        print("Choose target column:")
        print(list(data))
        target_column = input(">> ")
        while target_column not in list(data):
            print(list(data))
            target_column = input(">> ")
        return(target_column)
    
    except:
        print("An error occured while selecting your target column plese try again")
        get_target_column(data)
        
# Retrieves the attributes    
def get_attributes(data, target_column):
    try:
        data.drop(target_column, axis=1).copy()
        # Puts the data into an Ordered Dictionary makingit easier to work with
        attributes = Dict()
        for column in data.columns:
            if data[column].dtype != object:
                attributes[column] = [data[column].min(), data[column].max()]
            else:
                attributes[column] = list(data[column].unique())
        return(attributes)
    
    except:
        print("An error occured whiile obtaining attributes")
        get_attributes(data)
    
# Processes the data to make it easier to read    
def procces_data(target_column, data, attributes):
    Y = data[target_column]
    if data[target_column].dtype == object:
        LE.fit(data[target_column])
        data[target_column] = LE.transform(data[target_column])
        
    data = pd.get_dummies(data)
    return (attributes, data, targetCol)

def get_depth():
    depth = input(" Enter Max Depth, or -1 to use none\n>> ")

def create_decision_tree(attributes, data, target_column):
    try: 
        
        while not depth.isnumeric() and not depth[1:].isnumeric():
            depth = get_depth()
        if int(depth) > 0:
            tree_clf = DTC(max_depth = int(depth), random_state = 42)
        else:
            tree_clf = DTC(random_state = 42)
        
        tree_clf.fit(X, y)
        return(tree_clf)
        
    except:
       print("Tree build failed")
        return -1
    
# Saves the Decision Tree
def save(tree_clf):
    try:
        model_save_name = input('Enter model name for saving :')
        saved_tree = pickle.dump(tree_clf,open( str(model_save_name)+".p", "wb" ))
    except:
        print("failed to save tree")
        return -1
    
# Loads the Decison tree  
def load_tree():
    try:
        model_load_name = input('Enter model name for loading :')
        model_file = open(str(model_load_name)+".p",'rb')
        clf = pickle.load(model_file)
        return(clf)
    except:
        print("Failed to find file")
        load_tree()


        
   
