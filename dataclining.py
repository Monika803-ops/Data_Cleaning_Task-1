import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('Titanic-Dataset.csv')
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop('Cabin', axis=1, inplace=True)
print(df.isnull().sum())
df['Sex']=df['Sex'].map({'male':0,'female':1})
df=pd.get_dummies(df,columns=['Embarked'],drop_first=True)
print(df.head())
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])
print(df[['Age','Fare']].head())
sns.boxplot(x=df['Age'])
plt.title('Boxplot of Age')
plt.show()
sns.boxplot(x=df['Fare'])
plt.title('Boxplot of Fare')
plt.show()
df=df[df['Fare']<300]
print(df.describe())
print(df.head())
df.to_csv('Cleaned_Titanic_Dataset.csv', index=False)
