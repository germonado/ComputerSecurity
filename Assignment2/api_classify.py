import json
import os,sys,random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler
# malware api sequence files
MALPATH = './API/1/'
MALFILES = os.listdir(MALPATH)
# normal api sequence files
NORMPATH = './API/0/'
NORMFILES = os.listdir(NORMPATH)

APIFILTER = './filtered_API.txt'

api_list = []
# load api function list
r = open(APIFILTER, mode='r', encoding='utf-8')
api_list = r.read().splitlines()

# for training X, y data preprocess
X = []
y = []
apilen = len(api_list)
mallen = len(MALFILES)
for i in range(1000):
	tmp = np.zeros(apilen)
	r = open(MALPATH+MALFILES[i], mode='r', encoding='utf-8')
	words = r.read().split()
	for j in api_list:
		tmp[api_list.index(j)] += 1
	
	X.append(list(tmp))
	y.append(1)

	tmp = np.zeros(apilen)
	r = open(NORMPATH+NORMFILES[i], mode='r', encoding='utf-8')
	words = r.read().split()
	for j in words:
		tmp[api_list.index(j)] += 1

	X.append(list(tmp))
	y.append(0)
	
X = np.array(X)
y = np.array(y)

x_train_all, x_test, y_train_all, y_test = train_test_split(X,y,stratify=y,test_size=0.2,random_state=42)
x_train, x_val, y_train, y_val = train_test_split(x_train_all,y_train_all,stratify=y_train_all,
                   test_size=0.2,random_state=42)

scaler = StandardScaler()   
scaler.fit(x_train) 
x_train_scaled = scaler.transform(x_train)
x_val_scaled = scaler.transform(x_val)  

# simple model
mlp = MLPClassifier(hidden_layer_sizes=(100,), activation='logistic', \
                    solver='lbfgs', alpha=0.01, batch_size=32, \
                    max_iter=500)

mlp.fit(x_train_scaled, y_train) 
print(mlp.score(x_val_scaled, y_val))
