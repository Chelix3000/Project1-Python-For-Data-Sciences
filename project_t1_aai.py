# -*- coding: utf-8 -*-
"""Project_T1_AAI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WegUmoaudmfZcNCoGl2WApX_8qm84qyj
"""

# Team 1 : Python for Data Science (Kelas Siska Anggraeni)
# Studi Independen Kampus Merdeka - IBM Advance AI - Infinite Learning (Batam, Indonesia)

# This project aims to unveil the potential insights of the service industry from the given dataset.
# And to predict the nuances of tipping behavior within the restaurant realm using several machine learning algorithms:
# 1. Linear Regression
# 2. Random Forest
# 3. Decision Tree
# 4. Naive Bayes
# 5. SVM

# The dataset can be accessed via this link: https://www.kaggle.com/datasets/vishakhdapat/waiter-tip-
# The code program can be accessed via this link: https://www.kaggle.com/code/mrsimple07/waiter-tip-analysis-prediction

# Package installation

import gdown
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset

url = 'https://drive.google.com/uc?id=1dR6t0bgPR765Mz7lOXW0SevTHTx-mXgD'
output = 'tips.csv'
gdown.download(url, output, quiet=False)
df = pd.read_csv(output)

# Read CSV as dataframe (df)
df.head()

# Dataset pre-processing: Gaining dataset information

df.info()

df.describe()

df.isnull().sum()

# Exploratory Data Analysis (EDA):
# Total tips based on smoking.

sns.barplot(x = df['smoker'], y = df['total_bill'])
plt.title('Total tips based on smoking')
plt.show()

# Exploratory Data Analysis (EDA):
# Total tips based on days.

sns.barplot(x = df['day'], y = df['total_bill'])
plt.title('Total tips based on days')
plt.show()

# Exploratory Data Analysis (EDA):
# Total tips based on sex.

sns.barplot(x = df['sex'], y = df['total_bill'])
plt.title('Total tips based on sex')
plt.show()

# Exploratory Data Analysis (EDA):
# Correlation matrix of the features.

correlation_matrix = df[['total_bill','tip', 'size']].corr()
sns.heatmap(correlation_matrix, annot = True)
plt.show()

# Exploratory Data Analysis (EDA):
# Histogram plot: Distribution of Total Bill and Tip

sns.histplot(df['total_bill'], bins=20, kde=True, color='blue', label='Total Bill')
sns.histplot(df['tip'], bins=20, kde=True, color='orange', label='Tip')
plt.title('Distribution of Total Bill and Tip')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Exploratory Data Analysis (EDA):
# Boxplot: Total bill by day.

sns.boxplot(x='day', y='total_bill', data=df, palette='viridis')
plt.title('Boxplot of Total Bill by Day')
plt.show()

# Exploratory Data Analysis (EDA):
# Average tips by sex

sns.barplot(x='sex', y='tip', data=df, palette='pastel')
plt.title('Average Tip by Sex')
plt.show()

# Machine Learning: Model Training and Evaluation
# One - Hot encoding

df= pd.get_dummies(df, columns = ['sex', 'smoker', 'day','time'], drop_first =True)
df.head()

# Prediction Model using Linear Regression

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

X, y = df.drop(['tip'], axis=1), df['tip']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R²:", r2)

plt.plot(y_pred, label='Predicted')
plt.plot(y_test.values, label='Actual')
plt.legend()
plt.show()

# Prediction model using Random Forest

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import matplotlib.pyplot as plt

X, y = df.drop(['tip'], axis=1), df['tip']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R²:", r2)

plt.plot(y_pred, label='Predicted')
plt.plot(y_test.values, label='Actual')
plt.legend()
plt.show()

#Prediction Model using Decision Tree

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

X, y = df.drop(['tip'], axis=1), df['tip']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regressor = DecisionTreeRegressor()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("RMSE:", rmse)
print("MAE:", mae)
print("R²:", r2)

plt.plot(y_pred, label='Predicted')
plt.plot(y_test.values, label='Actual')
plt.legend()
plt.show()

#Classification Model using Naive Bayes

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score

X, y = df.drop(['tip'], axis=1), df['size']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelnb = GaussianNB()
nbtrain = modelnb.fit(X_train, y_train)

y_pred = nbtrain.predict(X_test)

# Evaluation metrics for classification
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

#Classification using SVM

import pandas as pd
from sklearn import metrics
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score

X, y = df.drop(['tip'], axis=1), df['size']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

#Evaluation metrics for classification
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))