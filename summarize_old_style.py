# -*- coding: utf-8 -*-
"""
@author: David R Hagen
@license: MIT
"""

from general_setup import merge_data,smooth_data,median_over_months,sum_over_patterns,filter_for_specific_day,plot_me
from load_data import good_XXth_data,old_style_data

# Good medians
good_XXth_medians = median_over_months(good_XXth_data)
good_XXth_medians_smooth = smooth_data(good_XXth_medians, 5)

# Old-style medians
old_style_medians = median_over_months(old_style_data)
old_style_medians_smooth = smooth_data(old_style_medians)

# Extract new-style days
only_2nd = filter_for_specific_day(good_XXth_data, '2nd')
only_3rd = filter_for_specific_day(good_XXth_data, '3rd')
only_22nd = filter_for_specific_day(good_XXth_data, '22nd')
only_23rd = filter_for_specific_day(good_XXth_data, '23rd')

# Extract old-style days
only_2d = filter_for_specific_day(old_style_data, '2d')
only_3d = filter_for_specific_day(old_style_data, '3d')
only_22d = filter_for_specific_day(old_style_data, '22d')
only_23d = filter_for_specific_day(old_style_data, '23d')

# Sum old and new style
sum_2nd_2d = sum_over_patterns(only_2nd.merge(only_2d, on='year'), new_name='2xx')
sum_3rd_3d = sum_over_patterns(only_3rd.merge(only_3d, on='year'), new_name='3xx')
sum_22nd_22d = sum_over_patterns(only_22nd.merge(only_22d, on='year'), new_name='22xx')
sum_23rd_23d = sum_over_patterns(only_23rd.merge(only_23d, on='year'), new_name='23xx')

# Merge data
sum_new_old = merge_data(sum_2nd_2d, sum_3rd_3d, sum_22nd_22d, sum_23rd_23d)
sum_new_old_medians = median_over_months(sum_new_old)
sum_new_old_medians_smooth = smooth_data(sum_new_old_medians)

# Plot new-style
ax = plot_me(good_XXth_medians_smooth)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['2nd'], 'g-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['3rd'], 'r-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['22nd'], 'c-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['23rd'], 'm-', linewidth=4)
ax.text(1878, 13.2e-8, '2nd', color='g')
ax.text(1889, 11.6e-8, '3rd', color='r')
ax.text(1902, 10.7e-8, '22nd', color='c')
ax.text(1916, 9.4e-8, '23rd', color='m')
ax.text(1935, 4e-7, '1st')
ax.text(1890, 2.58e-7, '4th')
ax.text(1933, 3.3e-8, '11th')
ax.text(1920, 2.58e-7, '31st')

# Plot old-style
ax = plot_me(good_XXth_medians_smooth)
ax.plot(good_XXth_medians_smooth['year'], old_style_medians_smooth['2d'], 'g-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], old_style_medians_smooth['3d'], 'r-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], old_style_medians_smooth['22d'], 'c-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], old_style_medians_smooth['23d'], 'm-', linewidth=4)
ax.text(1869, 13e-8, '2d', color='g')
ax.text(1866, 10.4e-8, '3d', color='r')
ax.text(1863, 8e-8, '22d', color='c')
ax.text(1860, 5.4e-8, '23d', color='m')

# Plot sum
ax = plot_me(good_XXth_medians_smooth)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['2nd'], 'g-', linewidth=2)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['3rd'], 'r-', linewidth=2)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['22nd'], 'c-', linewidth=2)
ax.plot(good_XXth_medians_smooth['year'], good_XXth_medians_smooth['23rd'], 'm-', linewidth=2)
ax.plot(good_XXth_medians_smooth['year'], old_style_medians_smooth['2d'], 'g-', linewidth=2)
ax.plot(good_XXth_medians_smooth['year'], old_style_medians_smooth['3d'], 'r-', linewidth=2)
ax.plot(good_XXth_medians_smooth['year'], old_style_medians_smooth['22d'], 'c-', linewidth=2)
ax.plot(good_XXth_medians_smooth['year'], old_style_medians_smooth['23d'], 'm-', linewidth=2)
ax.plot(good_XXth_medians_smooth['year'], sum_new_old_medians_smooth['2xx'], 'g-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_new_old_medians_smooth['3xx'], 'r-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_new_old_medians_smooth['22xx'], 'c-', linewidth=4)
ax.plot(good_XXth_medians_smooth['year'], sum_new_old_medians_smooth['23xx'], 'm-', linewidth=4)
ax.text(1872, 2.5e-7, '2xx', color='g')
ax.text(1872, 2.1e-7, '3xx', color='r')
ax.text(1869, 1.75e-7, '22xx', color='c')
ax.text(1869, 1.4e-7, '23xx', color='m')
