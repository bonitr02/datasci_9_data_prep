import pandas as pd
import numpy as np

#----------------Dataset #1 ---------------
# Load the dataset
maternal_data = pd.read_csv('datasets/Maternal_Sepsis_by_Select_Risk_Factors__SPARCS__2016-2018.csv')

# Display the first few rows of the dataframe
maternal_data.head()

#Display # of data rows and columns
maternal_data.shape #585 rows and 16 columns

# Check for missing values in the dataset
missing_values_mat = maternal_data.isnull().sum()

# Output the number of missing values per column
missing_values_mat[missing_values_mat > 0]
# Any Sepsis p-vale: 253
# Severe Sepsis p-value: 253

#column names
maternal_data.columns
'''
Index(['Year(s) of Live Birth', 'Maternal Window', 'Data Source',
       'Risk Factor Type', 'Risk Factor', 'Risk Factor Strata',
       'Live Births (N)', 'Live Births (%)', 'Any Sepsis Incidence (N)',
       'Any Sepsis Incidence per 100,000 Live Births',
       'Any Sepsis Crude Odds Ratio (95% CI)', 'Any Sepsis p-value',
       'Severe Sepsis Incidence (N)',
       'Severe Sepsis Incidence per 100,000 Live Births',
       'Severe Sepsis Crude Odds Ratio (95% CI)', 'Severe Sepsis p-value'],
      dtype='object')
'''
#value types
maternal_data.dtypes
'''
Year(s) of Live Birth                               object
Maternal Window                                     object
Data Source                                         object
Risk Factor Type                                    object
Risk Factor                                         object
Risk Factor Strata                                  object
Live Births (N)                                      int64
Live Births (%)                                    float64
Any Sepsis Incidence (N)                             int64
Any Sepsis Incidence per 100,000 Live Births       float64
Any Sepsis Crude Odds Ratio (95% CI)                object
Any Sepsis p-value                                  object
Severe Sepsis Incidence (N)                          int64
Severe Sepsis Incidence per 100,000 Live Births    float64
Severe Sepsis Crude Odds Ratio (95% CI)             object
Severe Sepsis p-value                               object
'''
# drop duplicates
maternal_data.drop_duplicates(inplace=True)

#drop rows with missing values
maternal_data = maternal_data.dropna()

#Display # of data rows and columns
maternal_data.shape #332 rows and 16 columns after dropping rows with missing data

#Export cleaned dataset to csv
maternal_data.to_csv('datasets/clean_maternal.csv')


# ------------- Dataset #2-----------------

# Load the dataset
flu_data = pd.read_csv('datasets/Influenza_Vaccination_Coverage_for_All_Ages__6__Months_.csv')

# Display the first few rows of the dataframe
flu_data.head()

#Display # of data rows and columns
flu_data.shape #204077 rows and 11 columns

# Check for missing values in the dataset
missing_values_flu = flu_data.isnull().sum()

# Output the number of missing values per column
missing_values_flu[missing_values_flu > 0]
#95% CI (%)       126
#Sample Size    20271

#column names
flu_data.columns
'''
Index(['Vaccine', 'Geography Type', 'Geography', 'FIPS', 'Season/Survey Year',
       'Month', 'Dimension Type', 'Dimension', 'Estimate (%)', '95% CI (%)',
       'Sample Size']
'''
#value types
flu_data.dtypes
'''
Vaccine                object
Geography Type         object
Geography              object
FIPS                    int64
Season/Survey Year     object
Month                   int64
Dimension Type         object
Dimension              object
Estimate (%)           object
95% CI (%)             object
Sample Size           float64
'''
# drop duplicates
flu_data.drop_duplicates(inplace=True)

#drop rows with missing values
flu_data = flu_data.dropna()

#Display # of data rows and columns
flu_data.shape #183680 rows and 11 columns after dropping rows with missing data

#Export cleaned dataset to csv
flu_data.to_csv('datasets/clean_influenza.csv')