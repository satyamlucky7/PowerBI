import pandas as pd
import seaborn as sns
import numpy as nm
import matplotlib.pyplot as plt
#dataset = pd.read_csv('FXData.csv')

# Creating dummy variables for Month
Months = pd.get_dummies(dataset['Month'])
Months.drop(['Dec'], axis=1)
dataset = pd.concat([dataset,Months],axis=1)

# Creating DataFrames for each country
dataset1 = dataset.loc[dataset['Country'] == "UK"]
dataset2 = dataset.loc[dataset['Country'] == "Germany"]
dataset3 = dataset.loc[dataset['Country'] == "Japan"]
dataset4 = dataset.loc[dataset['Country'] == "Australia"]



# Performing linear regression for UK/dataset1
X = dataset1[['ADR','FX','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]
Y = dataset1['Nights']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.4, random_state = 101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, Y_train)
intercept = lm.intercept_
lm.coef_
X_train.columns
cdataset = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff'])
ADR1 = cdataset.iloc[0,0]
FX1 = cdataset.iloc[1,0]
Jan1 = cdataset.iloc[2,0]
Feb1 = cdataset.iloc[3,0]
Mar1 = cdataset.iloc[4,0]
Apr1 = cdataset.iloc[5,0]
May1 = cdataset.iloc[6,0]
Jun1 = cdataset.iloc[7,0]
Jul1 = cdataset.iloc[8,0]
Aug1 = cdataset.iloc[9,0]
Sep1 = cdataset.iloc[10,0]
Oct1 = cdataset.iloc[11,0]
Nov1 = cdataset.iloc[12,0]
Intercept1 = intercept

# Performing linear regression for Germany/dataset2
X = dataset2[['ADR','FX','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]
Y = dataset2['Nights']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.4, random_state = 101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, Y_train)
intercept = lm.intercept_
lm.coef_
X_train.columns
cdataset = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff'])
ADR2 = cdataset.iloc[0,0]
FX2 = cdataset.iloc[1,0]
Jan2 = cdataset.iloc[2,0]
Feb2 = cdataset.iloc[3,0]
Mar2 = cdataset.iloc[4,0]
Apr2 = cdataset.iloc[5,0]
May2 = cdataset.iloc[6,0]
Jun2 = cdataset.iloc[7,0]
Jul2 = cdataset.iloc[8,0]
Aug2 = cdataset.iloc[9,0]
Sep2 = cdataset.iloc[10,0]
Oct2 = cdataset.iloc[11,0]
Nov2 = cdataset.iloc[12,0]
Intercept2 = intercept


# Performing linear regression for Japan/dataset3
X = dataset3[['ADR','FX','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]
Y = dataset3['Nights']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.4, random_state = 101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, Y_train)
intercept = lm.intercept_
lm.coef_
X_train.columns
cdataset = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff'])
ADR3 = cdataset.iloc[0,0]
FX3 = cdataset.iloc[1,0]
Jan3 = cdataset.iloc[2,0]
Feb3 = cdataset.iloc[3,0]
Mar3 = cdataset.iloc[4,0]
Apr3 = cdataset.iloc[5,0]
May3 = cdataset.iloc[6,0]
Jun3 = cdataset.iloc[7,0]
Jul3 = cdataset.iloc[8,0]
Aug3 = cdataset.iloc[9,0]
Sep3 = cdataset.iloc[10,0]
Oct3 = cdataset.iloc[11,0]
Nov3 = cdataset.iloc[12,0]
Intercept3 = intercept

# Performing linear regression for Australia/dataset4
X = dataset4[['ADR','FX','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]
Y = dataset4['Nights']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.4, random_state = 101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train, Y_train)
intercept = lm.intercept_
lm.coef_
X_train.columns
cdataset = pd.DataFrame(lm.coef_, X.columns, columns = ['Coeff'])
ADR4 = cdataset.iloc[0,0]
FX4 = cdataset.iloc[1,0]
Jan4 = cdataset.iloc[2,0]
Feb4 = cdataset.iloc[3,0]
Mar4 = cdataset.iloc[4,0]
Apr4 = cdataset.iloc[5,0]
May4 = cdataset.iloc[6,0]
Jun4 = cdataset.iloc[7,0]
Jul4 = cdataset.iloc[8,0]
Aug4 = cdataset.iloc[9,0]
Sep4 = cdataset.iloc[10,0]
Oct4 = cdataset.iloc[11,0]
Nov4 = cdataset.iloc[12,0]
Intercept4 = intercept


# Appending all coefficients i one dataframe
FinalData = pd.DataFrame({'Country': ['UK','Germany', 'Japan', 'Australia'], 'ADR': [ADR1, ADR2, ADR3, ADR4], 'FX': [FX1, FX2, FX3, FX4],
'Jan': [Jan1, Jan2, Jan3, Jan4], 
'Feb': [Feb1, Feb2, Feb3, Feb4],'Mar': [Mar1, Mar2, Mar3, Mar4], 'Apr': [Apr1, Apr2, Apr3, Apr4], 'May': [May1, May2, May3, May4], 'Jun': [Jun1, Jun2, Jun3, Jun4],
'Jul': [Jul1, Jul2, Jul3, Jul4], 'Aug': [Aug1, Aug2, Aug3, Aug4], 'Sep': [Sep1, Sep2, Sep3, Sep4], 'Oct': [Oct1, Oct2, Oct3, Oct4], 'Nov': [Nov1, Nov2, Nov3, Nov4],

'Intercept': [Intercept1, Intercept2, Intercept3, Intercept4]})


FinalData['Equation'] = FinalData['Intercept'].map(str) + '+' + FinalData['ADR'].map(str) + '-' + FinalData['FX'].map(str)  + '-' + FinalData['Jan'].map(str) + '-' + FinalData['Feb'].map(str)  + '-' + FinalData['Mar'].map(str)  + '-' + FinalData['Apr'].map(str)  + '-' + FinalData['May'].map(str) + '-' + FinalData['Jun'].map(str) + '-' + FinalData['Jul'].map(str)  + '-' + FinalData['Aug'].map(str)  + '-' + FinalData['Sep'].map(str) + '-' + FinalData['Oct'].map(str)  + '-' + FinalData['Nov'].map(str) 
# FinalData.to_csv (r'C:\Users\Satyam.Anand\Desktop\PE Coef\CoefDataSet.csv', index = False, header=True)
FinalData
