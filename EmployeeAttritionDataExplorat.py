import pandas as pd

df = pd.read_csv("/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv")

#printing the names of the columns
print("names of the columns are:")
print(df[:0])

#checking if there are nulls in the data
#note that in pandas documentation the NULL or NaN data is called as Missing data
"""While checking for NULL values in a dataframe, we use the isnull() function on the data frame.
If we want to check if there are 'any' missing values, then we use the chained function isnull().any()
If we want to retrieve the count of missing values across the entire data frame, we need to use the chained function, isnull().sum().sum()
Note: in isnull().sum().sum() --> the first chained sum() is going to give the number of missing values in each row in dataframe.
the second sum() will add the values returned by the previous sum() function"""

print('\n***************checking for null values in the data frame***************\n')
if df.isnull().sum().sum() == 0:
    print('NO NULLS')
else:
    print(df.isnull().sum().sum())

#Exploring the data
#Age of employee who are considered Attrition=Yes
df_attrition_yes = df[df['Attrition'] =='Yes']
print(df_attrition_yes[['Age']].mean())

#analyzing relationship between age and years at company
print(df_attrition_yes[['Age','YearsAtCompany']].head(10))

#checking the number of records in the data frame for Attrition = yes
print('The number of rows are: ',len(df_attrition_yes.index))

"""the same can be done using the following code"""
print('The number of rows are: ',df_attrition_yes.shape)
print('The number of rows are: ',df_attrition_yes['Age'].count())