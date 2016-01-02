# -*- coding: utf-8 -*-
"""
@author: David R Hagen
@license: MIT
"""

from statistics import median,mean

import numpy as np
from functools import reduce
import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame
import getngrams

# Global options
plt.xkcd()
matplotlib.rcParams.update({'font.size': 18})

# General fetching function
def fetch_all_data(items):
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i+n]
        
    corpus = 'eng_2012'
    start_year = 1800 # earliest
    end_year = 2008 # latest
    smoothing = 0
    case_sensitivity = False
    
    # Google can only handle 12 simultaneous queries, so break up query into chunks
    each_data = []
    for chunk in chunks(items, 12):
        query = ','.join(chunk)
        
        # Drop first two arguments
        data_i = getngrams.getNgrams(query, corpus, start_year, end_year, smoothing, case_sensitivity)[2]
        each_data.append(data_i)
    
    # Combine all the data into a single data set
    data = reduce(lambda left, right: left.merge(right, on='year'), each_data)
    
    return data

# Joins data by year
def merge_data(*each_data):
    return reduce(lambda left, right: left.merge(right, on='year'), each_data)
    
# General smoothing function
def smooth_data(raw, smoothing=3):
    columns = [col for col in raw.columns if col != 'year']
    n_years = len(raw.index)
    n_days = len(columns)
    smooth = raw.copy()
    for i_year in range(n_years):
        smooth_over_indexes = [i for i in range(i_year-smoothing, i_year+smoothing+1) if i >= 0 and i < n_years]
        for i_day in range(0,n_days):
            smooth_value = mean(raw.ix[smooth_over_indexes, columns[i_day]])
            smooth.set_value(i_year, columns[i_day], smooth_value)
            
    return smooth

# Should be a standard library function
def unique(seq): 
   uni = []
   [uni.append(i) for i in seq if not uni.count(i)]
   return uni

# Median over months
def median_over_months(raw):
    n_years = len(raw.index)
    patterns = unique([date.split(' ')[1] for date in raw.columns[1:]])
    n_patterns = len(patterns)
    medians = DataFrame(np.zeros((n_years,1+n_patterns)), columns=['year']+patterns)
    medians['year'] = raw['year']
    for i_year in range(0, n_years):
        for i_pattern in range(0, n_patterns):
            columns_for_this_day = [col for col in raw.columns[1:] if col.split(' ')[1] == patterns[i_pattern]]
            medians.set_value(i_year, patterns[i_pattern], median(raw.iloc[i_year][columns_for_this_day]))
    return medians

# Sum over days
def sum_over_patterns(raw, new_name=None):
     n_years = len(raw.index)
     sums = DataFrame(np.zeros((n_years,1+12)), columns=['year']+months)
     sums['year'] = raw['year']
     for i_year in range(0, n_years):
         for i_month in range(0, 12):
             columns_for_this_month = [col for col in raw.columns[1:] if col.split(' ')[0] == months[i_month]]
             sums.set_value(i_year, months[i_month], sum(raw.iloc[i_year][columns_for_this_month]))
     
     if new_name != None:
         sums.columns = ['year'] +  [col+' '+new_name for col in sums.columns if col != 'year']
         
     return sums

# Extract only columns of particular days
def filter_for_specific_day(data, day):
    return data[['year'] + [col for col in data.columns[1:] if col.split(' ')[1] == day]]

def plot_me(*each_data, years=(1800,2008)):
    data = merge_data(*each_data)
    data = data[years[0]-1800:years[1]-1800+1]
    ax = data.plot(x='year', legend=False, figsize=(10,6), color='k')
    ax.ticklabel_format(useOffset=False)
    ax.yaxis.set_ticklabels([])
    ax.set_ylim(ymin=0)
    return ax

# Every day of the year
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
        '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th',
        '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th' , '30th',
        '31st']
n_days = len(days)

good_XXth_days_year = [months[i_month] + ' ' + days[i_day] 
                       for i_month in range(12) 
                       for i_day in range(n_days) 
                       if i_day < days_in_months[i_month]]
n_dates = len(good_XXth_days_year)

good_XX_days_of_year = [months[i_month] + ' ' + str(i_day+1)
                        for i_month in range(12) 
                        for i_day in range(n_days) 
                        if i_day < days_in_months[i_month]]

date_to_month_indexes = [months.index(day.split(' ')[0]) for day in good_XXth_days_year]

date_to_day_indexes = [days.index(day.split(' ')[1]) for day in good_XXth_days_year]

day_to_date_indexes = [[] for _ in range(n_days)]
for i_date in range(0, n_dates):
    day_to_date_indexes[date_to_day_indexes[i_date]].append(i_date)

# Bad forms of 11
bad_letters = '1Ilit'
bad_XXth_days = [i+j+'th' for i in bad_letters for j in bad_letters]
bad_XXth_days.remove('11th') # the 11th is not bad

# Bad XXth dates
bad_XXth_days_of_year = [months[i_month] + ' ' + bad_XXth_days[i_day] 
                         for i_month in range(12) 
                         for i_day in range(len(bad_XXth_days))]
n_bad_dates = len(bad_XXth_days_of_year)

# Bad nth dates
bad_nth_days_of_year = [months[i_month] + ' nth'
                         for i_month in range(12)]

# Bad XX dates
bad_XX_days = [i+j for i in bad_letters for j in bad_letters]
bad_XX_days.remove('11') # the 11 is not bad
bad_XX_days.remove('it') # Get rid of it because it pollutes the data

bad_XX_days_of_year = [months[i_month] + ' ' + bad_XX_days[i_day] 
                       for i_month in range(12) 
                       for i_day in range(len(bad_XX_days))]

# Old-style 2nd, 3rd, 22nd, 23rd
old_style_days = ['2d', '3d', '22d', '23d']
old_style_days_of_year = [months[i_month] + ' ' + old_style_days[i_day] 
                       for i_month in range(12) 
                       for i_day in range(len(old_style_days))]