import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from math import exp

df = pd.read_csv('data.csv', index_col=0)
#X = df[['Make','Model','Year','Trim','Trips','City','Zip_Code','State','Transmission','Seats','Doors','Toll_Pass','MPG','Gas_Type','Rate','Miles_Allowed','Owner_Rating','month_joined','current_month','months_on_Turo','Response_Rate','Response_Time','car_type']]
df.head()

# Check for missing values
df.isnull().sum()
# Replace missing values with mean values
df['Response_Rate'].fillna(90,inplace=True)
df['Response_Time'].fillna(65,inplace=True)
df['Seats'].fillna(5,inplace=True)
df['Doors'].fillna(4,inplace=True)
df['Toll_Pass'].fillna(0,inplace=True)
df['MPG'].fillna(25,inplace=True)
df['Miles_Allowed'].fillna(1000,inplace=True)
# Check again
df.isnull().sum()

# Drop unnecessary variables
df.drop('Trim', axis=1, inplace=True)
#df.drop('Owner', axis=1, inplace=True)
df.drop('month_joined', axis=1, inplace=True)
df.drop('current_month', axis=1, inplace=True)

# Normalize trips
df['ntrips']=df['Trips'].divide(df['months_on_Turo'], axis='index')

# Summary Statistics
df.describe(percentiles=[.5]).transpose()

# Frequency distribution (like tab var, sort in Stata)
df['State'].value_counts()

# Drop States with low counts
g = df.groupby('State')
df = g.filter(lambda x: len(x) > 120)

## fit a OLS model with intercept on TV and Radio
df = sm.add_constant(df)

# Basic Regression
#est = sm.OLS(y, X, missing='drop').fit()

# Full OLS Regression
model = smf.ols(formula='ntrips ~  Year + C(State) * car_type + C(Transmission) + Seats + Doors + Toll_Pass + MPG + C(Gas_Type) + Rate + Miles_Allowed + Owner_Rating + Response_Rate + Response_Time', data=df)

# Export back to CSV for use in next step in project, if needed
#df.to_csv('seven_cities_mod.csv')

# Full Poisson Regression
fam = sm.families.Poisson()
#ind = sm.cov_struct.Exchangeable()
data=df
#model = smf.glm(formula="ntrips ~  Year + C(State) * car_type + C(Transmission) + Seats + Doors + Toll_Pass + MPG + C(Gas_Type) + Rate + Miles_Allowed + Owner_Rating + Response_Rate + Response_Time", data=data, family=fam)

result = model.fit()
print result
df['predictions'] = result.predict(df)
#print predictions[0:10]

results = result.summary()
print results
#results = dict(model.params)
#for key in results:
#    results[key] = exp(results[key])
#rdf = pd.DataFrame.from_dict(results, orient='index')
##print rdf
#

# Removing duplicates before creating rankings
df["model_year"] = df["Model"] + df["Year"].map(str)
df['rank'] = df.groupby('model_year')['predictions'].transform('mean')
df.sort_values(by='model_year', axis=0)

df2=df.drop_duplicates(["State","model_year"])
#print df2['State'].value_counts()
#Check if it worked by matching with original dataframe
#print df['State'].value_counts()
df2.to_csv('rank.csv')