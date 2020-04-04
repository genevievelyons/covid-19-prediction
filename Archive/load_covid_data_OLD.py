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
import os

pd.set_option('display.max_columns', None)

################
## Pull from Git Repos
################

#pwd
os.chdir("AC209B - Data Science II/Final Project")

#Update the data
git_dir = 'COVID-19/'
g = git.cmd.Git(git_dir)
g.pull()

#Update the current 
git_dir = 'covid-19-prediction/'
g = git.cmd.Git(git_dir)
g.pull()

################
## Load the data
################

#File list
files = os.listdir("COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/")
files = [f for f in files if f.endswith(".csv") ]

#Read in the files
df_list = [pd.read_csv("COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/" + f, dtype = str) for f in files]

#Add the filename 
for dataframe, f in zip(df_list, files):
  dataframe['date'] = f.replace(".csv","")
  
#Fix the column names
for df in df_list:
    #Standardize column names
    df.rename(columns = {'Province/State': 'province_state', 'Country/Region': 'country_region',\
                         'Last Update': 'last_update', 'Lat': 'latitude',\
                         'Long_': 'longitude','Admin2': 'county',\
                         }, inplace = True)
    #all lowercase
    df.columns = map(str.lower, df.columns)
    
#Combine the data
data = pd.concat(df_list, axis = 0, ignore_index=True, sort = False)

data['date']= pd.to_datetime(data['date'])
    
data.shape #(48552, 13)

################
## Fix the US Counties and FIPS Codes
################

#Load the FIPS lookup table
fips_lu = pd.read_csv("COVID-19/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv", dtype = str)
fips_lu
data[data.country_region == 'US']

data[(data.country_region == 'US') & (data.date >= '3/22/2020')]
data[(data.country_region == 'US') & (data.date < '3/22/2020')]

data[(data.country_region == 'US') & (data.date >= '3/22/2020') & (data.combined_key == 'New York City, New York, US')]
data[(data.country_region == 'US') & (data.date == '3/21/2020')]

#Fips starts being produced on 3/22

#Set combined key 
data.loc[(data.date < '3/22/2020'),'combined_key'] = \
    (data[(data.date < '3/22/2020')]['province_state'] + ", " ).fillna('') + \
    data[(data.date < '3/22/2020')]['country_region']

#Set county name
    
#Set FIPS code for US
    
