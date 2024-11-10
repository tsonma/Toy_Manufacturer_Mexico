# -------------------------------------------------------------
# BEST PRACTICE
# When filtering through your dataframe (Table) and wanting to reduce the size of your data frame, you should add .copy() to avoid any issues later down the line (Lesson 139 of Maven Analytics Python Data Science: Data Prep & EDA with Python)
#IT IS BEST PRACTICE TO CREATE A COPY .copy() OF THE DATASET YOU IMPORT

# -------------------------------------------------------------
#TRANSFORMING DATA TYPE
# To look at the data type
#df.dtypes or df.info()

# Converting to datetime
# pd.to_datetime(date_column, format = '%y-%m-%d') --This is when the year is 2 digits
# pd.to_datetime(date_column, format = '%Y-%m-%d') --This is when the year is 4 digits

#You can always consult python documentation
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# Converting to numeric
# pd.to_numeric(column)

# To remove non-numeric characters ($,%,etc.) use str.replace()
# example: clean_income = df.Income.str.replace('$','').str.replace(',','')
#          df.Income = pd.to_numeric(clean_income)

#There is another way to convert data and it is astype() to convert more specific data types like 'int','float','object' and 'bool', but pd.to_numeric() can handle missing values (NaN), while Series.astype() cannot

import pandas as pd

run_times = pd.read_excel('Data_Prep_Course/Data/Run Times.xlsx',sheet_name ='Sheet1')
run_times.info()
run_times

#Changing the data type of the 'Fee' column
run_times.Fee = pd.to_numeric(run_times.Fee.str.replace('$',''))

#Changing the data type of the 'Warm Up Time' column
#In this specific example, we had to use .astype('str') prior to doing a str.replace() or else it will give us NaN values.
run_times['Warm Up Time'] = pd.to_numeric(run_times['Warm Up Time'].astype('str').str.replace(' min',''))

#Changing the 'Rain' column from boolean to integer. 1 = True and 0=False
run_times['Rain'].astype('int')

# -------------------------------------------------------------
#IDENTIFYING MISSING VALUES
# Identifying the number of missing values
# df.isna().sum()

# Identifying all the rows of a column with missing values
# df[df.column_name.isna()]

# Identifying the rows of missing values
# df[df.isna().any(axis=1)]

#Identifying the number of missing values in a column
# df.Column_name.value_counts(dropna=False)

# np.NaN - Numpy's NaN is the most common representation (values are stored as floats)
# pd.NA - Panda's NA is a newer missing data type (values can be stored as integers)
# None - Base Python's default missing data type (does not allow numerical calculations)

# -------------------------------------------------------------
#HANDLING MISSING VALUES

#1st way - Keep the missing data as is

#2 Remove and entire row or column with missing data

#this will drop rows with NaN values
# df.dropna()

#This will drop rows that only have missing values
# df.dropna(how="all")

#The following is an example of dropping rows if missing values that have missing values in either Student or Class columns. inplace = True is the same as doing 
# df = df.dropna(subset=['Student','Class'])
# df.dropna(subset=['Student','Class'], inplace = True)

#This will drop rows that don't have at least "n" values. In other words, if there is only one column that has a value and all other colomns for that same row is NaN, it will be dropped.
# df.dropna(thresh=2)

#3 Keep non-missing data
# df[df["City"].notna()]

#4 Impute missing numerical data with a 0 or a substitute like the average, mode, etc
#Part A
# .fillna() method imputes missing data with an appropriate value
# Example: df["Income"] = df["Income"].fillna(df["Income"].median())

#Part B
# This will replace missing values by Freshman in the Year column, and keep current values if it is no blank
# np.where(df.Year.isna(), 'Freshman', df.Year)

#5 Resolve missing data with domain expertise
# df.loc[10,"State"] = "FL"

# -------------------------------------------------------------
#IDENTIFYING INCONSISTENT TEXT & TYPOS

# For CATEGORICAL data, you can look at unique values in the column
# df["Class"].value_counts()

# This will look at rows with the following conditions for the "Class" column
# df[df["Class"].isin(['Exploratory Data Analysis', 'EDA'])]

# For NUMERICAL data, you can look at the descriptive stats of the column
# df["Age"].describe()

#FIXING INCONSISTENT TEXT & TYPOS
# .loc[] to update a value at a particular location
# np.where(condition, if_true, if_false) to update values in a column based on a conditional statement
# .map() to map a set of values to another set of values
# String methods like str.lower(), str.strip(), str.replace() to clean text data

# -------------------------------------------------------------
#DUPLICATE DATA
# use df.duplicated() to identify duplicated rows of data
# df.duplicated().sum() to idenify the number of duplcated data
# df[df.duplicated(keep=False)] to return all duplicated rows
# use df.drop_duplicates(inplace = True) or df = df.drop_duplicates() to remove duplicate rows of data
# you can also do df[~df.duplicated()] to exclude duplicate rows
# use df.reset_index(drop = True, inplace=True) to reset the index

# -------------------------------------------------------------
#FINDING OUTLIERS
import seaborn as sns
import matplotlib.pyplot as plt

#HISTOGRAMS (more of a visual way to quickly identify)
# Method 1 using seaborn and matplotlib
#step 1: sns.histplot(df['column_name']) or sns.histplot(df['column_name'], binwidth = 1)
#step 2: plt.show()

# Method 2 using only matplotlib
# df['age'].hist() or df['age'].hist(bins = 3)
# if you want to determine the number of bins, you can do the max of a column - the minimum of that column
#  df['age'].max() - df['age'].min() 

#BOXPLOTS ()
#sns.boxplot(x=df['Column_name'])
# q25, q50, q75 = np.percentile(df['age'], (25,50,75))
# iqr = q75 - q25
# min_age = q25 - 1.5*iqr
# max_age = q75 + 1.5*iqr
# min_age, q25, q50, q75, max_age

#STANDARD DEVIATION
# The standard deviation is a measure of the spread of a data set from the mean. Values at least 3 standard deviations away from the mean are considered outliers. This is meant for normally distributed, or bell shaped data

#1 mean = np.mean(df['column_name'])
#2 sd = np.std(df['column_name'])
#3 mean, sd
#4 [x for x in df.['column_name'] if (grade < mean - 3*sd) or (grade > mean +3*sd)]

# -------------------------------------------------------------
#HANDLING OUTLIERS
#1st way - Keep the missing data as is

#2 Remove and entire row or column with missing data

#The following keeps rows following a certain criteria
#df[df['column_name']>x]

#3 Impute missing numerical data with a 0 or a substitute like the average, mode, etc
#Part A
# .fillna() method imputes missing data with an appropriate value
# In this example, you want to replace outliers by a specific value
    # min_grade = df[df.Grade >= 60].Grade.min()
    # min_grade = df[df.Grade >= 60]['Grade'].min()
    # min_grade
    # df.Grade = np.where(df.Grade < 60, min_grade, df.Grade)
#  Example 1: df["Income"] = df["Income"].fillna(df["Income"].median())
#  Example 2: df["Income"] = df["Income"].fillna(0)

#4 Changing specific data based on domain expertise
# df.loc[37, 'Grade'] = 74

# -------------------------------------------------------------
#DATA ISSUES CHECK (SUMMARY OF ALL PREVIOUS STEPS)

# Identifying the rows of missing values
# df[df.isna().any(axis=1)]

# For CATEGORICAL data, you can look at unique values in the column
# df["Class"].value_counts()

# For NUMERICAL data, you can look at the descriptive stats of the column
# df["Age"].describe()

# Identify duplicated rows of data
#  df[df.duplicated()]

#Identify Outliers
# df.describe()

# -------------------------------------------------------------
# CREATING NEW COLUMNS
# after cleaning data types & issues, you may still not have the exact data that you need, so you can create new columns from existing data to aid your analysis

# Method 1: to calculate a percentage, you can set up two columns with the numerator and denominator values and then divide them. You can also multiply by 100 if desired.

    #example:
    # shopping_list['Total Spend'] = shopping_lis['Price'].sum()
    # shopping_list['Percent Spend'] = shopping_lis['Price']/ total_spend *100

# Method 2: using np.where

    #example:
    # run_times['Fee with Tax'] = np.where(run_times.Location == 'gym', run_times.Fee *1.08, run_times.Fee)

# -------------------------------------------------------------
# EXTRACTING DATETIME COMPONENTS (CREATING NEW COLUMNS)
# dt.component to extract a component from a datetime value (day, month, etc.)

    #example
    # run_times['Run Date'].dt.days
    # run_times['run_DOW'] = run_times['Run Date'].dt.dayofweek
    # run_times['Run Date'].dt.time
    # run_times['Run Date'].dt.month
    # run_times['Run Date'].dt.year
    # run_times['Run Date'].dt.date

# Calculate the difference between two dates
    #example: run_times['Race Date'] - run_times['Run Date']

# Adding two weeks to the race date
    #example: run_times['Race Date'] + pd.to_timedelta(2, unit='W')
    #example: run_times['Race Date'] + pd.to_timedelta(2, unit='D')

# Creating a mapping for each day of the week number
#dow_mapping = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thuesday', 4: 'Friday'. 5: 'Saturday', 6: 'Sunday'}

# Linking the DOW with the mapping
# run_times['DOW'] = run_times['run_DOW'].map(dow_mapping)

#creating a condition with the DATETIME
#run_times['DOW'] = np.where(groceries.Category == 'Produce: Fruit', groceries.Next_Scheduled_Shipment + pd.to_timedelta(1,'D'), groceries.Next_Scheduled_Shipment)

# -------------------------------------------------------------
# BINNING VALUES FOR DATA MODELLING
#The purpose of bins is that you don't want a day of the week of a month to be 'worth' more than other periods

# EXAMPLE #1
# For instance to separate days of the week and weekend, you can create a column called 'weekend'.
# model_df['Weekend'] = np.where(customers['Sign UP DOW'].isin([5,6]),1,0)

# EXAMPLE #2
# The same can be done with the age of individuals. If you have customers between the ages of 0 and 90, you can group them under 3 categories. Kids betweeen 0-18, adults between 19-65 and elderly >65


# -------------------------------------------------------------
# EXTRACTING TEXT (CREATING NEW COLUMNS)

#Extracting Text
# df.str[start:end]

#Splitting into multiple columns
#groceries[['Category','Subcategory']] = pd.DataFrame(groceries.Category.str.split(':').to_list())

#Finding patterns

# df.str.contains()
#run_notes['Contains final'] = run.notes.str.lower().str.contains('great|congrats', regex =True)

# reorder columns
# groceries_with_new_columns = groceries[['Product_ID','Product_ID_Num','Category', 'Subcategory', 'Item', 'Organic',etc.]]



