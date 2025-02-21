import pandas as pd
import numpy as np
def initial_analysis(df):
    print(f'Head:\n{df.head()}')
    print(f'Tail:\n{df.tail()}')
    print(f'DataTypes of Columns\n{df.info()}')
    print(f'Categorical Columns:{df.select_dtypes(include=['object','category']).columns}')
    print(f'Numerical Columns:{df.select_dtypes(include=['number']).columns}')
    print(f'Description of Data:\n{df.describe()}')
def cat_unique_values(df):
    for i in df.select_dtypes(include=['object','category']).columns:
        print(f'Unique value of {i}:{df[i].unique()}')
class HandlingNullValues():
    def __init__(self,df):
        self.df=df
    def mean_method(self,col):
        self.df[col]=self.df[col].fillna(self.df[col].mean())
    def median_method(self,col):
        self.df[col] = self.df[col].fillna(self.df[col].median())
    def mode_method(self,col):
        self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
    def value_handling(self, col_name, value):
        self.df[col_name] = self.df[col_name].fillna(value)
    def display_null_values(self):
        print(f'NullValues:\n{self.df.isnull().sum()}')
    def filling_method(self,col,meth):
        if meth=='bfill':
            self.df[col]=self.df[col].fillna(method=meth)
        if meth=='ffill':
            self.df[col]=self.df[col].fillna(method=meth)
    def value_method(self,col,val):
        self.df[col].fillna(val,inplace=True)
    def random_method(self,col):
        choices=self.df[col].dropna().unique()
        self.df[col] = self.df[col].apply(lambda x: np.random.choice(choices) if pd.isna(x) else x )
def datatype_coversion(df,col,to_type):
    if to_type=='numeric':
        df[col]=pd.to_numeric(df[col],errors='coerce')
    elif to_type=='datetime':
        df[col]=pd.to_datetime(df[col],errors='coerce')
class Data_cleaning():
    def __init__(self,df):
        self.df=df
    def drop_method(self,val,col):
        self.df.drop(self.df[self.df[col]==val].index,inplace=True)
df_2=pd.read_csv('dirty_cafe_sales.csv')
initial_analysis(df_2)
dc=Data_cleaning(df_2)
dc.drop_method('ERROR','Item')
dc.drop_method('UNKNOWN','Item')
dc.drop_method('ERROR','Quantity')
dc.drop_method('UNKNOWN','Quantity')
dc.drop_method('ERROR','Price Per Unit')
dc.drop_method('UNKNOWN','Price Per Unit')
dc.drop_method('ERROR','Total Spent')
dc.drop_method('UNKNOWN','Total Spent')
dc.drop_method('ERROR','Payment Method')
dc.drop_method('UNKNOWN','Payment Method')
dc.drop_method('ERROR','Location')
dc.drop_method('UNKNOWN','Location')
datatype_coversion(df_2,'Quantity','numeric')
datatype_coversion(df_2,'Price Per Unit','numeric')
datatype_coversion(df_2,'Total Spent','numeric')
datatype_coversion(df_2,'Transaction Date','datetime')
hm=HandlingNullValues(df_2)
hm.display_null_values()
hm.mode_method('Quantity')
hm.mean_method('Price Per Unit')
hm.mean_method('Total Spent')
hm.filling_method('Transaction Date','ffill')
hm.mode_method('Item')
hm.value_method('Payment Method','Cash')
hm.random_method('Location')
hm.display_null_values()
df_2.to_csv('Cleaned Data.csv',index=False)
df_3=pd.read_csv('Cleaned Data.csv')
print(df_3.columns)
df_3=df_3.drop(['Transaction ID','Transaction Date'],axis=1)
grp1=df_3.groupby(['Item','Quantity'])
print(grp1.sample(100))
print(grp1.count())
print(grp1['Total Spent'].mean())
print(grp1['Price Per Unit'].cumsum())
piv1=df_3.pivot(columns=['Item'])
print(piv1.sample(100))
df1=pd.read_csv('athlete_events.csv')
df2=pd.read_csv('noc_regions.csv')
df3=pd.concat([df1,df2],axis=0)
df4=pd.merge(df1,df2,on='NOC',how='left')
df5=pd.merge(df1,df2,on='NOC',how='right')
df6=pd.merge(df1,df2,on='NOC',how='inner')
print(df3)
print(df4)
print(df5)
print(df6)