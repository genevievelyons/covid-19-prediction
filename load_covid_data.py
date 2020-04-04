#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:34:08 2020

@author: genevievelyons
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import git 
#import os 

pd.set_option('display.max_columns', None)

################
## Pull from Git Repos 
################

#pwd
#os.chdir("AC209B - Data Science II/Final Project/")

#Update the data
git_dir = 'COVID-19/'
g = git.cmd.Git(git_dir)
g.pull()

#Update the current 
git_dir = 'covid-19-prediction/'
g = git.cmd.Git(git_dir)
g.pull()

################
## Load the data - US Only
################

#Load data
confirmed = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv', dtype = str)  
deaths = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv', dtype = str)  

#List of keys
keys = confirmed.loc[:,"UID":"Combined_Key"]

#Columns
c = list(keys.columns)
c.append('confirmed')
c.append('deaths')
c.append('date')

data = pd.DataFrame(columns = c)

#Pivot the columns
for col in confirmed.columns[11:]:
    df = pd.concat([keys,confirmed.loc[:,col]], axis = 1)
    df.rename(columns = {col: 'confirmed'}, inplace = True)
    df = pd.concat([df, deaths.loc[:,col]], axis = 1)
    df.rename(columns = {col: 'deaths'}, inplace = True)
    df["date"] = col
    data = pd.concat([data, df], axis = 0, sort = False)

#Names
data.columns = map(str.lower, data.columns)
data.rename(columns = {'admin2':'county'}, inplace = True)

#Data types
data['date'] = pd.to_datetime(data['date'])
data['lat'] = pd.to_numeric(data['lat'])
data['long_'] = pd.to_numeric(data['long_'])
data['confirmed'] = pd.to_numeric(data['confirmed'])
data['deaths'] = pd.to_numeric(data['deaths'])



np.sum(data[(data.combined_key.str[0:10] == 'Unassigned') & (data.date > '3/22/2020')]['confirmed'])
np.sum(data[(data.combined_key.str[0:10] != 'Unassigned') & (data.date > '3/22/2020')]['confirmed'])

51835/1641575 #3.15% of cases are unassigned

#data.shape #(234216, 14)
#data

################
## Export Data - US Only
################

data.to_csv('covid-19-prediction/data/covid_data.csv', index = False)



################
## Load the data - Global
################

#Load data
confirmed = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', dtype = str)  
deaths = pd.read_csv('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', dtype = str)  

#List of keys
keys = confirmed.loc[:,"Province/State":"Long"]

#Columns
c = list(keys.columns)
c.append('confirmed')
c.append('deaths')
c.append('date')

data = pd.DataFrame(columns = c)

#Pivot the columns
for col in confirmed.columns[4:]:
    df = pd.concat([keys,confirmed.loc[:,col]], axis = 1)
    df.rename(columns = {col: 'confirmed'}, inplace = True)
    df = pd.concat([df, deaths.loc[:,col]], axis = 1)
    df.rename(columns = {col: 'deaths'}, inplace = True)
    df["date"] = col
    data = pd.concat([data, df], axis = 0, sort = False)

#Names
data.columns = map(str.lower, data.columns)
data.rename(columns = {'province/state':'province_state', 'country/region':'country_region'}, inplace = True)

#Data types
data['date'] = pd.to_datetime(data['date'])
data['lat'] = pd.to_numeric(data['lat'])
data['long'] = pd.to_numeric(data['long'])
data['confirmed'] = pd.to_numeric(data['confirmed'])
data['deaths'] = pd.to_numeric(data['deaths'])


#data.shape #(18834, 7)
#data


################
## Export Data - Global
################

data.to_csv('covid-19-prediction/data/covid_data_global.csv', index = False)

