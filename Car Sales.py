import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import locale

locale.setlocale(locale.LC_ALL, '')

# PATH TO DATA
filepath = 'C:/Users/marce/Documents/Python/'

# READ IN DATA
cars = pd.read_excel(filepath + 'SWD/Car Sales/Car Sales.xlsx', sheet_name='Data2')
cars['timeperiod'] = cars['timeperiod'].str.replace(' ', '\n')

# CREATE NEW DATAFRAME OF JUST SALES NUMBERS
cars2 = cars.drop('timeperiod', axis=1)

# CALCULATE THE SUM OF EACH COLUMN
column_sums = cars2.sum()

# SORT COLUMNS BASED ON SUM IN DESCENDING ORDER
sorted_columns = column_sums.sort_values(ascending=False)

# REARRANGE THE COLUMNS IN THE DATAFRAME
cars2 = cars2[sorted_columns.index]

# CREATE SERIES OF JUST THE TIME PERIODS
cars3 = cars.filter(['timeperiod'])

# JOIN THE TIME PERIOD COLUMN TO THE ARRANGED COLUMNS
cars = cars3.join(cars2)

# ADJUST CANVAS SIZE
plt.figure(figsize=(11, 8.5))

# CREATE COLOR PALETTE
palette = plt.get_cmap('tab20b')

# PLOT MULTIPLE LINES
num = 0
for column in cars.drop('timeperiod', axis=1):
    if column != "REGIONAL AVG":
        num += 1

        # CHOOSE THE CORRECT SUBPLOT LOCATION
        plt.subplot(5, 3, num)

        # PLOT ALL GROUPS
        for v in cars.drop('timeperiod', axis=1):
            plt.plot(cars['timeperiod'], cars[v], marker='', color='grey', linewidth=0.6, alpha=0.3)

        # PLOT THE HIGHLIGHTED LINE
        plt.plot(cars['timeperiod'], cars['REGIONAL AVG'], marker='', color='red', linewidth=1.4, alpha=0.3)
        plt.plot(cars['timeperiod'], cars[column], marker='', color=palette(num), linewidth=2.4, alpha=0.9,
                 label=column)

        # SET TICK STEP AND FONT
        plt.xticks(np.arange(0, 11, step=10), fontsize=6, fontweight='bold')
        plt.yticks(np.arange(0, 151, step=75), fontsize=6, fontweight='bold')
        plt.tick_params(left=False, bottom=False)

        # INDIVIDUAL GRAPH TITLES
        plt.title(column, loc='left', fontsize=10, fontweight='bold', color=palette(num))
        plt.title(' (' + str(locale.format_string("%d", sum(cars[column]), grouping=True)) + ' vehicles)',
                  loc='right', fontsize=6, fontweight='bold', color=palette(num))

# MAIN TITLES
plt.figtext(0.435, 0.96, "Car Sales by Location Compared to the", fontsize=14, fontweight='bold',
            color='black', ha='right')
plt.figtext(0.44, 0.96, "Regional Average", fontsize=14, fontweight='bold',
            color='red', ha='left', alpha=0.54)
plt.figtext(0.05, 0.93, "(most total sales to least total sales)", fontsize=10, color='black', ha='left')

# ADJUST SPACING
plt.subplots_adjust(wspace=0.80, hspace=1,
                    top=0.86, bottom=0.10,
                    left=0.05, right=0.95)

# plt.subplot(5, 3, 15).text(0.10, 0.75, "TEST")
# plt.subplot(5, 3, 15).axis('off')

plt.show()
