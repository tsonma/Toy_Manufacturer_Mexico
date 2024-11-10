# -------------------------------------------------------------
# DATA PREP FOR MODELING

#The goal is to transform the data into a structure and format that can be used as a direct input for machine learning algorithm.

# You can prepare your data for modeling by:
# 1. Creating a single table
# 2. Setting the correct row granularity
# 3. Ensuring each column is non null and numeric
# 4. Engineering features for the model

# -------------------------------------------------------------
# CREATING A SINGLE TABLE

#Appending Data
# The columns for the DataFrames must be identical. Once you append data, it is best practice to reset the index
# pd.concat([df_1,df_2], axis=0).reset_index(drop = True)
# pd.concat([df_1,df_2], axis=1).reset_index(drop = True)

#Joining Data (if you want to replace blanks with 0 add the .fillna(0))
# (left_df.merge(right_df,
#                how='left,
#                left_on='store',
#                right_on='store')).fillna(0)

# -------------------------------------------------------------
# PREPARING ROWS (ROW GRANULARITY)
# To prepare rows for modeling, you need to think about the question you're trying to answer and determine what one row (observation) of your table will look like

# Total_Spend = april_may_purchases.groupby('Customer ID')['Price'].agg('sum').rename('april_may_purchases').rename('Total Spend').to_frame().reset_index()


# model_df = Total_Spend.merge(june_purchases,
#                      how = 'left',
#                      on='Customer ID').fillna(0)

# -------------------------------------------------------------
# PREPARING COLUMNS

#All values should be non-null

# Use d.info() or df.isna() to identify null values and either remove them, impute them, or resolve them based on your domain expertise

#All values should be numeric
#Turn text fields to numeric fields using dummy variables
#Turn datetime fields to numeric fields using datetime calculations

#Dummy Variable: A field that only contains zeros and ones to represent the presence (1) or absence(0) of a value, also known as one-hot encoding 

#STEP 1 GET DUMMIES
#pd.get_dummies(column_name, drop_first=True).astype(int)
#pd.get_dummies(column_name).astype(int)

#STEP 2 APPEND DATA with the table that contains the dummies
# pd.concat([df_1,df_2], axis=1)

#STEP 1 and 2 combined
#pd.get_dummies([['column name','column name']], drop_first=True).astype(int)
#Example: pd.get_dummies(april_may_purchases[['Customer ID', 'Has School Aged Children']], drop_first=True).astype(int).rename(columns = {'Has School Aged Children_Yes':'Has Kids'})

#STEP 3 GROUP BY
# categories = pd.concat([df_1,df_2], axis=1).
# df.groupby(col)[col].agg(['min','max','count', 'mean', 'sum']).to_frame().reset_index()
# df.groupby(col)[col].agg(['min','max','count', 'mean', 'sum']).reset_index()

#STEP 4 Add categories to the mode dataframe
#model_df = model_df.merge(categories, how='left', on='customer')

#STEP 5 PREPARE DATETIME columns

#OPTION 1: Using dummy variables to prepare a date column for modeling
#pd.get_dummies(column_name, drop_first=True)

#OPTION 2: Using the days from 'Today' to prepare a date column for modeling.

# Group by customer to get their latest purchase date
    #last_purchase = purchases.groupby('customer').max()

# Assume today is the max purchase date
    #today = purchases.purchase_date.max()

# Calculate the days passed between today and their latest purchase
    #last_purchase['days_passed'] = (today - last_purchase.purchase_date).dt.days

#OPTION #3: Using the average time between dates to prepare a date column for modeling
    #purchases['days_between'] = purchases.groupby('customer').diff(1)
    #purchases['days_between'] = purchases['days_between'].dt.days.purchases.groupby('customer')['days_between'].mean().head()

#A variation of .diff is .shift(), which will shift all the rows of a column up or down

# -------------------------------------------------------------
# FEATURE ENGINEERING (TRANSFORMING< SCALING, PROXY VARIABLES)

# Feature engineering is the process of creating columns that you think will be helpful inputs for improving a model (help predict, segment, etc.)
    # When preparing rows & columns for modeling you're already feature engineering

# Other feature engineering techniques
#TRANSFORMATIONS
    # Log transforms turn skewed data into more normally-distributed data
    # You can use the np.log() function to apply a log transform to a series


#SCALING (normalization & standardization)
#Scaling, as its name implies, requires setting all input features on a similar scale

#NORMALIZATION
    # Normalization transforms all values to be between 0 and 1 (or between -1 and 1)
    # Calculation to normalize: (x-x_min)/(x_max - x_min)
    # Normalization is typically used when the distribution of the data is unknown
  
# Normalization with sklearn
# from sklearn.preprocessing import MinMaxScaler
# mm_scaler = MinMaxScaler()
# normalized =mm_scaler.fit_transform(model_df_subset)
# pd.DataFrame(normalized, columns = model_df_subset.columns)


#STANDARDIZATION
    #Standardization transforms all values to have a mean of 0 and a standard deviation of 1
    # (x -x_mean)/x_std
    # .StandardScaler() function from the sklearn library
    #Standardization is typically used when the data is normally distributed (bell curve)

# Standardization with sklearn (standardizes all columns)
# from sklearn.preprocessing import StandardScaler
# std_scaler = StandardScaler()
# standardized =std_scaler.fit_transform(model_df_subset)
# pd.DataFrame(standardized, columns = model_df_subset.columns)

#PROXY VARIABLES
# A proxy variable is a feature meant to approximately represent another
# They are used when a feature is either difficult to gather or engineer into a new feature

# -------------------------------------------------------------
# FEATURE ENGINEERING (TRANSFORMING< SCALING, PROXY VARIABLES)

#1 Relevant features are what makes a great model
#2 You want your data to be long not wide (many rows, few columns)
#3 If you are working with customer data, a popular marketing technique is to engineer features related to the recency, frequency, and monetary value (RFM) of a customer's transactions
#4 Once you start modeling, you are bound to find things you missed during the data prep and will continue to engineer features and gather, clean, explore, and visualize the data
#5 Use your intuition and think about the goal for your analysis - which features would do the best job predicting/segmenting/etc.
#6 Start simple with perhaps 2-3 features for your model, then assess the results, and continue to make the model more complex and assess


# -------------------------------------------------------------
# PREVIEW: MODELING
