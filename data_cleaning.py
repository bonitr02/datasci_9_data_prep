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
maternal_data.replace(" ", pd.NA, inplace=True)
maternal_data = maternal_data.replace(',', '', regex=True)
maternal_data = maternal_data.dropna()

#Display # of data rows and columns
maternal_data.shape #332 rows and 16 columns after dropping rows with missing data

# Based on data, the dependent variable (y) is Live Births (%) and dependent variables(x) are Risk Factor, Risk Factor Strata, Any Sepsis Incidence (N), 
# Any Sepsis Incidence per 100,000 Live Births 

#Rename columns
maternal_cleaned = maternal_data.rename(columns={"Live Births (%)":"live_births_percent","Risk Factor":"risk_factor","Risk Factor Strata":"risk_factor_strata","Any Sepsis Incidence (N)":"any_sepsis_incidence_number","Any Sepsis Incidence per 100,000 Live Births":"any_sespsis_100000_live_births"})

#Form new dataset with selected columns
new_maternalDF = maternal_cleaned[['live_births_percent','risk_factor','risk_factor_strata', 'any_sepsis_incidence_number', 'any_sespsis_100000_live_births']]

# Check distribution of numerical variables
# mean is much lower than the max, indicating possible outliers
new_maternalDF.describe()
'''
       live_births_percent  any_sepsis_incidence_number  any_sespsis_100000_live_births
count           332.000000                   332.000000                       332.00000
mean              4.302651                    42.111446                       828.39750
std               6.953414                    62.640558                      2390.46511
min               0.000000                     0.000000                         0.00000
25%               0.110000                     3.000000                       107.50750
50%               1.090000                    15.000000                       176.35500
75%               4.960000                    53.250000                       412.28000
max              39.400000                   437.000000                     17280.45000
'''
new_maternalDF['risk_factor'].value_counts()
'''
risk_factor
Region of Residence                       27
Race/Ethnicity                            18
Education                                 15
Trimester Beginning Prenatal Care          9
Age Group                                  6
                                          ..
Conversion of cardiac rhythm               2
Disseminated intravascular coagulation     2
Eclampsia                                  2
Episiotomy                                 2
'''

#Export cleaned dataset to csv
new_maternalDF.to_csv('datasets/clean_maternal.csv')

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
flu_data.replace(" ", pd.NA, inplace=True)
flu_data = flu_data.replace(',', '', regex=True)
flu_data = flu_data.dropna()

#Display # of data rows and columns
flu_data.shape #167457 rows and 11 columns after dropping rows with missing data
flu_data['Month'] = flu_data['Month'].apply(str)
flu_data['Estimate (%)'] = flu_data['Estimate (%)'].apply(float)
# Based on data, the dependent variable (y) is Estimate(%) and dependent variables(x) are Geography, Season/Survey Year, Month, and Dimension 

#Rename columns
cleaned_flu = flu_data.rename(columns={"Estimate (%)":"estimated_vax_percent","Season/Survey Year":"season_survey_year", "Geography":"geography", "Month":"month", "Dimension":"dimension"})

#Form new dataset with selected columns
new_flu = cleaned_flu[['estimated_vax_percent','season_survey_year','geography', 'month', 'dimension']]

# Check distribution of numerical variables
new_flu.describe()
'''
       estimated_vax_percent
count          167457.000000
mean               35.628022
std                18.695661
min                 0.000000
25%                24.100000
50%                37.900000
75%                47.900000
max                97.900000                  16221              22164           2876   19118                11215
'''

# value counts for the categorical variables

new_flu['season_survey_year'].value_counts()
'''
max                97.900000
>>> new_flu['season_survey_year'].value_counts()
season_survey_year
2009-10    20349
2020-21    13616
2017-18    12318
2022-23    12304
2021-22    12291
2019-20    12221
2018-19    11916
2014-15    11338
2016-17    11076
2015-16    11026
2013-14    10864
2012-13     9662
2011-12     9302
2010-11     9174
'''
new_flu['geography'].value_counts()
'''
geography
United States          2868
Region 4               2780
Region 5               2775
Region 3               2742
Region 6               2738
                       ... 
TX-Rest of state        271
IL-Rest of state        258
PA-Rest of state        258
NY-Rest of state        251
U.S. Virgin Islands     132
'''
new_flu['month'].value_counts()
'''
month
1     19003
2     17002
4     16997
5     16994
3     16994
12    16973
11    16955
10    16783
9     15256
8     10687
7      3813
'''
new_flu['dimension'].value_counts()
'''
dimension
6 Months - 17 Years                                        10935
≥18 Years                                                  10347
≥6 Months                                                  10275
≥65 Years                                                  10071
White Non-Hispanic                                         10035
Hispanic                                                    9377
50-64 Years                                                 9329
Other or Multiple Races Non-Hispanic                        9057
5-12 Years                                                  8887
6 Months - 4 Years                                          8868
Black Non-Hispanic                                          8690
18-49 Years at High Risk                                    8535
13-17 Years                                                 8476
18-64 Years                                                 8462
18-49 Years                                                 8220
18-64 Years at High Risk                                    7950
18-49 Years not at High Risk                                7497
18-64 Years not at High Risk                                6492
Asian Non-Hispanic                                          1327
American Indian or Alaska Native Non-Hispanic               1134
Medical Setting                                              510
Non-Medical Setting                                          509
Pharmacy/Store                                               498
6 Months - 64 Years at High Risk (Initial Target Group)      496
25-64 Years not in Initial Target Group                      495
25-64 Years at High Risk                                     494
Workplace                                                    312
School                                                       179
'''

#Export cleaned dataset to csv
new_flu.to_csv('datasets/clean_influenza.csv')