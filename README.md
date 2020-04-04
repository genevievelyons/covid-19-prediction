# covid-19-prediction

## To update the data

1. Clone this repository (`covid-19-prediction`) and the 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by Johns Hopkins CSSE (https://github.com/CSSEGISandData/COVID-19) to the same directory. 

2. Navigate to the directory that contains the two repositories and execute the load script: 

`./covid-19-prediction/load_covid_data.py`

This script will pull from both repos, load the data, manipulate it, and update the data file in the `covid-19-prediction` repo.

3. Push to this repo by executing the following:

`cd covid-19-prediction/; git add *; git commit -m "data update"; git push`

