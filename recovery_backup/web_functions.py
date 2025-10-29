import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
from pathlib import Path
import os


@st.cache_data()

def load_data():
    # Resolve diabetes.csv relative to this file, then the project root.
    this_file = Path(__file__).resolve()
    candidates = [
        this_file.parent / 'diabetes.csv',                     # Tabs/web_functions next to csv (unlikely)
        this_file.parent.parent / 'diabetes.csv',              # project root
        this_file.parent.parent.parent / 'diabetes.csv',       # one level up
        Path(os.getcwd()) / 'diabetes.csv'                     # current working directory fallback
    ]

    csv_path = None
    for p in candidates:
        if p.exists():
            csv_path = p
            break

    if csv_path is None:
        raise FileNotFoundError(
            "diabetes.csv not found. Expected it in one of: {}".format(
                ", ".join(str(p) for p in candidates)
            )
        )

    df = pd.read_csv(csv_path)
    X = df[['HbA1c_level','Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
    y = df['Outcome']

    return df, X, y


@st.cache_data()

def train_model(X,y):
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, #Increases the amount of pruning, which reduces overfitting. 
        class_weight=None, #This parameter allows you to assign different weights to classes
        criterion='entropy', #This parameter determines the function to measure the quality of a split.
        max_depth=4, #A deeper tree can model more complex patterns but may lead to overfitting
        max_features=None, #This parameter controls the number of features to consider when looking for the best split
        max_leaf_nodes=None, #This parameter limits the maximum number of leaf nodes in the tree. Setting this parameter can help control overfitting.
        min_impurity_decrease=0.0, #If the impurity decrease from a split is less than this value, the split will not be performed.
        min_samples_leaf=1, #A smaller value allows the tree to create more leaves, which can lead to overfitting.
        min_samples_split=2, #If a node has fewer samples than this value, it will not be split
        min_weight_fraction_leaf=0.0, #This parameter controls the minimum weighted fraction of the total sum of weights 
        random_state=42, #Setting it to an integer ensures that the results are reproducible.
        splitter='best' #This parameter controls the strategy used to choose the split at each node.
        )
    
    model.fit(X,y)

    score = model.score(X,y)

    return model, score

def predict(X, y, features):
    model, score = train_model(X, y)
    
    # Reshape the features correctly
    features = np.array(features).reshape(1, -1)  # Reshape to (1, n_features)
    
    prediction = model.predict(features)
    
    return prediction, score

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
from pathlib import Path
import os


@st.cache_data()

def load_data():
    # Resolve diabetes.csv relative to this file, then the project root.
    this_file = Path(__file__).resolve()
    candidates = [
        this_file.parent / 'diabetes.csv',                     # Tabs/web_functions next to csv (unlikely)
        this_file.parent.parent / 'diabetes.csv',              # project root
        this_file.parent.parent.parent / 'diabetes.csv',       # one level up
        Path(os.getcwd()) / 'diabetes.csv'                     # current working directory fallback
    ]

    csv_path = None
    for p in candidates:
        if p.exists():
            csv_path = p
            break

    if csv_path is None:
        raise FileNotFoundError(
            "diabetes.csv not found. Expected it in one of: {}".format(
                ", ".join(str(p) for p in candidates)
            )
        )

    df = pd.read_csv(csv_path)
    X = df[['HbA1c_level','Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
    y = df['Outcome']

    return df, X, y


@st.cache_data()

def train_model(X,y):
    model = DecisionTreeClassifier(
        ccp_alpha=0.0, #Increases the amount of pruning, which reduces overfitting. 
        class_weight=None, #This parameter allows you to assign different weights to classes
        criterion='entropy', #This parameter determines the function to measure the quality of a split.
        max_depth=4, #A deeper tree can model more complex patterns but may lead to overfitting
        max_features=None, #This parameter controls the number of features to consider when looking for the best split
        max_leaf_nodes=None, #This parameter limits the maximum number of leaf nodes in the tree. Setting this parameter can help control overfitting.
        min_impurity_decrease=0.0, #If the impurity decrease from a split is less than this value, the split will not be performed.
        min_samples_leaf=1, #A smaller value allows the tree to create more leaves, which can lead to overfitting.
        min_samples_split=2, #If a node has fewer samples than this value, it will not be split
        min_weight_fraction_leaf=0.0, #This parameter controls the minimum weighted fraction of the total sum of weights 
        random_state=42, #Setting it to an integer ensures that the results are reproducible.
        splitter='best' #This parameter controls the strategy used to choose the split at each node.
        )
    
    model.fit(X,y)

    score = model.score(X,y)

    return model, score

def predict(X, y, features):
    model, score = train_model(X, y)
    
    # Reshape the features correctly
    features = np.array(features).reshape(1, -1)  # Reshape to (1, n_features)
    
    prediction = model.predict(features)
    
    return prediction, score


