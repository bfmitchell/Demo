# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?parameter=tavg&state=44&div=0&month=6&periods[]=6&year=2017



import requests
from lxml import objectify

# my variables
num_periods = 6
parameter = 'tavg'
state_id = 44
div = 0
month = 8
year = '2016'
myWMUsername = 'bfmitchell'

#create url
url = 'https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?parameter=%s&state=%s&div=%s&month=%s&periods[]=%s&year=%s'
insert_variables = (parameter, state_id, div, month, num_periods, year)
url = url % insert_variables

#get content from url
response = requests.get(url).content
root = objectify.fromstring(response)

#print information
print myWMUsername
print root.data.value
print root.data.twentiethCenturyMean
print root.data.lowRank
print root.data.highRank
