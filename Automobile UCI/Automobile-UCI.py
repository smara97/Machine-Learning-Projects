#Dataset automobile from UCI , workshops superdatasceience

#import lips
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score   # for mean ,vairance and diff from pred and actual
from sklearn.metrics import accuracy_score
#import data set
df=pd.read_csv('F:\AI\Dataset\imports-85.csv')
df.head()
df.gas.isnull()   
"""
 print bool if any  index in train set have null value every rows 
 = df['gas'].isnull()
 df.gas.isnull().any() print if exist at least one value is null 
"""
df.isnull().any()  # for every colum print bool if exist at least one value is null

df.dtypes  # print every data type in data set object rep ---> string not int , not float

col=['symboling','normalized_losses','make','fuel_type','aspiration','num_of_doors','body_style','drive_wheels','engine_locatio','wheel_base'
     ,'length','width','height','curb_weight','engine_type','num_of_cylinders','engine_size','fuel_system'
     ,'bore','stroke','compression_ratio','horsepower','peak_rpm','city_mpg','highway_mpg','price']

df.index
df=pd.read_csv('F:\AI\Dataset\imports-85.csv',header =-1,na_values='?',names=col) # header -1 remove header na_values='?' replace  ? by NAN and add cloum(names) to headrer

df.head()

df.isnull().any()
#df.columns[df.isnull().any]   print columns that has misssing data "NAN"
df[df.columns[df.isnull().any()]].isnull().sum() # print the summation if train points has missing values
df[df.isnull().any(axis=1)][df.columns[df.isnull().any()]] # print every missing data with her column and row 

df.dtypes

df.drop(['make','symboling','normalized_losses'],axis=1,inplace=True)   #drop un unsed values in data 
df.head()

#### missing data and change it by good value to predict perfect  

df[df.num_of_doors.isnull()] # print missing values bt row , column in num_of_doors
df.num_of_doors[df.body_style=='sedan'].value_counts()   #take value of another attribute and get high count of num_of_doors 
df.loc[27,'num_of_doors']='four'   #change the value of missing data to the highest value predict in another attribute of data
df.loc[63,'num_of_doors']='four'

df[df.bore.isnull()]
df.bore.fillna(df.bore.mean(),inplace=True) #replave the missing data by mean of bore by using fillna method

df[df.stroke.isnull()]         #the change missing data to depenent data only not to y
 
df.stroke.fillna(df.stroke.mean(),inplace=True)

df.horsepower.fillna(df.horsepower.mean(),inplace=True)

df.peak_rpm.fillna(df.peak_rpm.mean(),inplace=True)

df.drop(df[df.price.isnull()].index,axis=0,inplace=True)      #if exist any missing data in Y delte it and delet trainging point all

df[df.columns[df.isnull().any()]].isnull().sum() #this line to check if exist any missing data or not



#   Encoding the text 'Categorical values'   

#first method by your hand
df.num_of_cylinders.value_counts()      #for num_of_cylinders
df.loc[df.num_of_cylinders=='two','num_of_cylinders']=2
df.loc[df.num_of_cylinders=='four','num_of_cylinders']=4
df.loc[df.num_of_cylinders=='five','num_of_cylinders']=5
df.loc[df.num_of_cylinders=='six','num_of_cylinders']=6
df.loc[df.num_of_cylinders=='seven','num_of_cylinders']=7
df.loc[df.num_of_cylinders=='eight','num_of_cylinders']=8
df.loc[df.num_of_cylinders=='twelve','num_of_cylinders']=12
df.loc[df.num_of_cylinders=='three','num_of_cylinders']=3

df.dtypes



#second method
col=['body_style','drive_wheels','engine_locatio','engine_type','fuel_system','num_of_doors','aspiration',
     'fuel_type']
df=pd.get_dummies(df,columns=col,drop_first=True)


#divide trainging set to train and test
train,test=train_test_split(df,test_size=0.2,random_state=0)

y_train=train.price
y_test=test.price
train.drop('price',axis=1,inplace=True)
test.drop('price',axis=1,inplace=True)

# make LinearRegression
regressor=LinearRegression()
regressor.fit(train,y_train)

y_pred=regressor.predict(test)

actual_data=np.array(y_test)
for i in range(len(y_pred)):
    expl=((actual_data[i]-y_pred[i])/actual_data[i])*100.0
    print('Actual Value ${:,.2f},Predicted value ${:,.2f} (%{:,.2f})'.format(actual_data[i],y_pred[i],expl))

#calc perforamnce of Data in train and test
r_square=r2_score(y_test,y_pred)*100.0  #in LinearRegression not exist accuracy exist the r2_square to calc diff**2 between predict and actual 
r_train=r2_score(y_train,regressor.predict(train))*100.0
print('Accuracy of Test,Predict  Data  is %{:,.2f}'.format(r_square))
print('Accuracy of Train Data is %{:,.2f}'.format(r_train))

#plotting data
plt.scatter(y_pred,y_test,color='blue')
plt.title('Automobile Data set represntation')
plt.show()
