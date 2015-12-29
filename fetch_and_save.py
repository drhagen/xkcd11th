# -*- coding: utf-8 -*-
"""
@author: David R Hagen
@license: MIT
"""

# Note: Google will cut you off if you try to run all this at once!

from general_setup import fetch_all_data,good_XXth_days_year,good_XX_days_of_year,bad_XXth_days_of_year,bad_nth_days_of_year,bad_XX_days_of_year

# Fetch good XXth data
good_XXth_data = fetch_all_data(good_XXth_days_year)
good_XXth_data = good_XXth_data[['year'] + good_XXth_days_year] # Reorder columns because Google sorts them funny
n_years = len(good_XXth_data.index)
good_XXth_data.to_csv('good_XXth_data.csv', index=False)

# Fetch good XX data
good_XX_data = fetch_all_data(good_XX_days_of_year)
good_XX_data = good_XX_data[['year'] + good_XX_days_of_year]
good_XX_data.to_csv('good_XX_data.csv', index=False)

# Fetch bad XXth data
bad_XXth_data = fetch_all_data(bad_XXth_days_of_year)
bad_XXth_data = bad_XXth_data[['year'] + [col for col in bad_XXth_days_of_year if col in bad_XXth_data.columns]]
bad_XXth_data.to_csv('bad_XXth_data.csv', index=False)

# Fetch bad nth data
bad_nth_data = fetch_all_data(bad_nth_days_of_year)
bad_nth_data = bad_nth_data[['year'] + [col for col in bad_nth_days_of_year if col in bad_nth_data.columns]]
bad_nth_data.to_csv('bad_nth_data.csv', index=False)

# Fetch bad XX data
bad_XX_data = fetch_all_data(bad_XX_days_of_year)
bad_XX_data = bad_XX_data[['year'] + [col for col in bad_XX_days_of_year if col in bad_XX_data.columns]]
bad_XX_data.to_csv('bad_XX_data.csv', index=False)
