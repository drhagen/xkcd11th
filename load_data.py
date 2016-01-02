# -*- coding: utf-8 -*-
"""
@author: David R Hagen
@license: MIT
"""

from pandas import DataFrame

# Load good XXth data
good_XXth_data = DataFrame.from_csv('good_XXth_data.csv', index_col=None)
n_years = len(good_XXth_data.index)

# Load good XX data
good_XX_data = DataFrame.from_csv('good_XX_data.csv', index_col=None)

# Load bad XXth data
bad_XXth_data = DataFrame.from_csv('bad_XXth_data.csv', index_col=None)

# Load bad nth data
bad_nth_data = DataFrame.from_csv('bad_nth_data.csv', index_col=None)

# Load bad XX data
bad_XX_data = DataFrame.from_csv('bad_XX_data.csv', index_col=None)

# Load old-style data
old_style_data = DataFrame.from_csv('old_style_data.csv', index_col=None)
