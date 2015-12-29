# -*- coding: utf-8 -*-
"""
@author: David R Hagen
@license: MIT
"""

from scipy.stats import norm

from general_setup import smooth_data,median_over_months,sum_over_patterns,plot_me
from load_data import good_XXth_data,bad_XXth_data,bad_nth_data

# Good medians
good_XXth_medians = median_over_months(good_XXth_data)
good_XXth_medians_smooth = smooth_data(good_XXth_medians, 5)

# The day of interest
only_11th = good_XXth_data[['year'] + [col for col in good_XXth_data.columns[1:] if col.split(' ')[1] == '11th']]
only_11th_medians_smooth = good_XXth_medians_smooth[['year','11th']]

# Bad sums
sum_bad_XXth = sum_over_patterns(bad_XXth_data, new_name='badth')

# Sum of good and bad
sum_bad_XXth_and_11th = sum_over_patterns(only_11th.merge(bad_XXth_data, on='year'), new_name='allth')
sum_bad_XXth_and_11th_medians = median_over_months(sum_bad_XXth_and_11th)
sum_bad_XXth_and_11th_medians_smooth = smooth_data(sum_bad_XXth_and_11th_medians, 5)

# Difference between good and sum of bad and good (not necessarily equal to sum of bad alone)
sum_XXth_minus_bad_medians = sum_bad_XXth_and_11th_medians.copy()
sum_XXth_minus_bad_medians.columns = ['year', 'diffth']
sum_XXth_minus_bad_medians['diffth'] = sum_bad_XXth_and_11th_medians['allth'] - good_XXth_medians['11th']
sum_XXth_minus_bad_medians_smooth = smooth_data(sum_XXth_minus_bad_medians)

# Sum of good and nth
sum_bad_11th_and_nth = sum_over_patterns(only_11th.merge(bad_nth_data, on='year'), new_name='allth')
sum_bad_11th_and_nth_medians = median_over_months(sum_bad_11th_and_nth)
sum_bad_11th_and_nth_medians_smooth = smooth_data(sum_bad_11th_and_nth_medians, 5)

# Difference between good and sum of bad and good (not necessarily equal to sum of bad alone)
sum_minus_bad_nth_medians = sum_bad_11th_and_nth_medians.copy()
sum_minus_bad_nth_medians.columns = ['year', 'diffth']
sum_minus_bad_nth_medians['diffth'] = sum_bad_11th_and_nth_medians['allth'] - good_XXth_medians['11th']
sum_minus_bad_nth_medians_smooth = smooth_data(sum_minus_bad_nth_medians)

# Sum of good and bad and nth
sum_bad_XXth_and_11th_and_nth = sum_over_patterns(sum_bad_XXth_and_11th.merge(bad_nth_data, on='year'), new_name='allth')
sum_bad_XXth_and_11th_and_nth_medians = median_over_months(sum_bad_XXth_and_11th_and_nth)
sum_bad_XXth_and_11th_and_nth_medians_smooth = smooth_data(sum_bad_XXth_and_11th_and_nth_medians, 5)

# Narrow down to a single error
#only_llth = bad_XXth_data[['year'] + [col for col in bad_XXth_data.columns[1:] if col.split(' ')[1] == 'llth']]
#only_llth_medians = median_over_months(only_llth)
#only_llth_medians_smooth = smooth_data(only_llth_medians, 5)

#sum_11th_llth = sum_over_patterns(only_11th.merge(only_llth, on='year'), new_name='11llth')
#sum_11th_llth_medians = median_over_months(sum_11th_llth)
#sum_11th_llth_medians_smooth = smooth_data(sum_11th_llth_medians, 5)

# Histogram over 2000-2008
medians_over_decade = good_XXth_medians[2000-1800:2008-1800+1].median()
del medians_over_decade['year']

mean_ordinal = medians_over_decade.mean()
std_ordinal = medians_over_decade.std()

pvalue_ordinals = [min(norm.cdf([element], loc=mean_ordinal, scale=std_ordinal)) for element in medians_over_decade]

ax = medians_over_decade.hist(bins=35, grid=False, color='blue', figsize=(7,4.5))
ax.set_xlim(xmin=0)
ax.set_xlabel('frequency')
ax.set_ylabel('count')
ax.text(5.5e-8, 1.2, '1st')
ax.text(3.4e-8, 1.2, '15th')
ax.text(1.1e-8, 1.2, '11th')

# Mean over 2000-2008
#ax = plot_me(good_XXth_medians_smooth, years=(2000,2008))
#ax.text(2004, 6.2e-8, '1st')
#ax.text(2005, 1.3e-8, '11th')
#ax.text(2001, 3.3e-8, '15th')

# Plot raw data
# This is a total mess
#plot_me(good_XXth_data)

# Plot good medians
ax = plot_me(good_XXth_medians_smooth)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['11th'], 'b-', linewidth=4)
ax.text(1935, 4e-7, '1st')
ax.text(1925, 4.5e-8, '11th')
ax.text(1920, 2.58e-7, '31st')

# Plot good and xxth together
ax = plot_me(good_XXth_medians_smooth, sum_bad_XXth_and_11th_medians_smooth)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['11th'], 'b-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_bad_XXth_and_11th_medians_smooth['allth'], 'b-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_XXth_minus_bad_medians_smooth['diffth'], 'b-', linewidth=4)
ax.text(1925, 4.5e-8, '11th')
ax.text(1927, 10e-8, 'sum')
ax.text(1895, 2.5e-8, 'xxth')

# Plot good and nth together
ax = plot_me(good_XXth_medians_smooth, sum_bad_11th_and_nth_medians_smooth)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['11th'], 'b-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_bad_11th_and_nth_medians_smooth['allth'], 'b-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_minus_bad_nth_medians_smooth['diffth'], 'b-', linewidth=4)
ax.text(1920, 10e-8, '11th')
ax.text(1938, 15e-8, 'sum')
ax.text(1889, 5e-8, 'nth')

# Plot good and bad and nth together
ax = plot_me(good_XXth_medians_smooth, sum_bad_XXth_and_11th_and_nth_medians_smooth)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['11th'], 'b-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_bad_XXth_and_11th_and_nth_medians_smooth['allth'], 'b-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_XXth_minus_bad_medians_smooth['diffth'], 'b-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_minus_bad_nth_medians_smooth['diffth'], 'b-', linewidth=4)
ax.text(1920, 10e-8, '11th')
ax.text(1940, 15e-8, 'total')
ax.text(1889, 5e-8, 'nth')
ax.text(1895, 2.5e-8, 'xxth')
