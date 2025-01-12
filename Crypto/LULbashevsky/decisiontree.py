from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, precision_score
from sklearn.utils import resample, shuffle
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import metrics

train = pd.read_csv('S2G\Crypto\LULbashevsky\\train.csv')
test = pd.read_csv('S2G\Crypto\LULbashevsky\\test.csv')


scaler = StandardScaler()


T_total = 1000

X_train = train[train.columns[:-1]]
y_train = train[train.columns[-1]]


X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

colors = {0: 'blue', 1: 'orange'}

X_test = test[test.columns[:-1]]
y_test = test[test.columns[-1]]
y_train = np.array(y_train)
X_train = np.array(X_train)
for i in range(2):
    plt.hist(X_train[i], color=colors[y_train[i]], alpha=0.5, bins=30, edgecolor='black')
plt.show()