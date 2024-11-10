# EXPLORING DATA
# Viewing & Summarizing data from multiple angles.

#Filtering
# Apply multiple filters by using the '&' and '|' operators (AND/OR)
    #Example 1:
    # df.loc[(tea.type == 'herbal') | (tea.temp >= 200)] - .loc is only necessary when you are filtering on rows and SPECIFIC columns. If not, you do not need to include it. In other words, you can always include it.
    #Example 2:
    # df.loc[(tea.type == 'herbal') | (tea.temp >= 200), ['Price_Dollars', 'Inventory']]. The .loc is necessary here bcs you are filtering on rows and SPECIFIC columns.

#Sorting
# df.sort_values()
# tea.sort_values(['name','price'],ascending=False)

#Grouping
# df.groupby(col)[col].agg(['min','max','count', 'mean', 'sum']).rename('June Purchases').to_frame().reset_index()

# (col): column(s) to group by
# [col]: column(s) to apply the calculation to the column
# aggregation: .mean(), .sum(), .min(), .max(), .count(), nunique()
# .rename(''): Give a name to the new column created
# to_frame(): create a data frame which is needed for further changes
# reset_index(): To make a separate column for the first one
#In addition to aggregating grouped data, you can also use the .head() and .tail() methods to return the first or last 'n' records for each group.
    #Example:
    #(groceries [['Category', 'Item', 'Price_Dollars']].sort_values('Price_Dollars', ascending = False).groupby('Category').head(1))

#Pivot data
# (df.pivot(index='Customer',
#           columns ='Genre',
#           values = '# Songs')
#           .fillna(0)
#           .reset_index())

#index: rows
#columns: columns
#values: values
#.fillna(0): to switch NaN values to 0
#.reset_index()

# -------------------------------------------------------------
# VISUALIZING DATA

#Before visualizing, you should sort the data
#Horizontal and Vertical Bar Chart
#df.plot.barh(x='year', y='happiness_score')
#df.plot.bar(x='year', y='happiness_score')

#Line Chart
#df.plot.line(x='year', y='happiness_score')
    #example:
    #(happiness[happiness.country_name.isin(['Canada', 'Mexico','United States'])]).iloc[:, :3].pivot(index='year', columns='country_name', values ='happiness_score'.plot.line())


#Pair plots (only for numerical data)
#import seaborn as sns
#sns.pairplot(student_data)
#plt.show()

#Scatter plots
# sns.scatterplot(data = df, x='x axis column', y = 'y axis column')

#Distribution: Shows all the possible values in a column and how often each occurs. It can be shown in two ways (Frequency table or Histogram)

#Frequency tables: .value_counts().sort_index()
#example: df['tempo'].round(-1).value_counts().sort_index()
#histogram: sns.histplot(df['Cups of Coffee'], bins =10)

#For continuous data (contains decimals), you should convert to integers by using the .round() function. Then you will be able to use the value_counts() or histogram

# -------------------------------------------------------------
# COMMON DISTRIBUTION
#1 Normal distribution (continuous data such as the height of women)
    #The empiral rule outlines where most values fall in a normal distribution: 68% within 1 standard deviation from the mean, 95% within 2 standard deviations from the mean and 99.7% fall within 3 standard deviations from the mean
#2 Uniform distribution (if you roll a die 500 times, the chances of getting any of the 6 numbers is the same)
#3 Binomial distribution (DISCRETE DATA: Knowing that 10% of all ad views result in a click, these are the clicks you'll get if you show an ad to 20 customers)
# Poisson distribution (DISCRETE DATA: Knowing that you typically get 2 cancellations each day, these are the number of cancellations you will see on any given day)

#SKEW: represents the asymetry of a normal distribution around its mean. There are techniques that can deal with the skewed data, such as taking the log of the data set, to turn it into normally distributed data


# -------------------------------------------------------------
# CORRELATION (does not imply causation)
# -1: This is a negative correlation
# 0: This has no correlation
# 1: This a perfect positive correlation

#use the df.corr()
# A correlation under 0.5 is weak, between 0.5 and 0.8 is moderate, and over 0.8 is strong