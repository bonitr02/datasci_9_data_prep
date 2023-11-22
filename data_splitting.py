#pip install scikit-learn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# will need to encode the risk factor strata column from dataset 1
# everything but estimated % will need to be encoded from dataset 2

#----------------Dataset #1 ---------------

#load dataset
maternal_data = pd.read_csv('datasets/clean_maternal.csv')

# Display the first few rows of the dataframe
maternal_data.head()
'''
   Unnamed: 0  live_births_percent                       risk_factor risk_factor_strata  any_sepsis_incidence_number  any_sespsis_100000_live_births
0           1                 0.18                     Alcohol abuse                Yes                            5                          422.30
1           3                 6.82                            Asthma                Yes                           88                          201.60
2           5                 0.34          Cardiac valvular disease                Yes                           10                          458.09
3           7                 0.02  Chronic congestive heart failure                Yes                            2                         1408.45
4           9                 0.06    Chronic ischemic heart disease                Yes                            2                          518.13
'''
# Define the features and the target variable
X1 = maternal_data[['risk_factor','risk_factor_strata', 'any_sepsis_incidence_number', 'any_sespsis_100000_live_births']] # Features (all columns except live_births_percent)
y1 = maternal_data['live_births_percent']  # Target variable (live_births_percent)

#Error message - ValueError: could not convert string to float: 'Alcohol abuse' - so unable to scale for this dataset
 
# Creating a instance of label Encoder.
le = LabelEncoder()
 
# Using .fit_transform function to fit label
# encoder and return encoded label
label = le.fit_transform(X1['risk_factor'])

#drop old column and replace with encoded values column
X1.drop("risk_factor", axis=1, inplace=True)
X1['risk_factor'] = label
print(X1)
'''
array([ 9, 12, 17, 20, 21, 23, 25, 27, 31, 36, 37, 41, 49, 51, 53, 62, 64,
       65, 68, 74, 81, 83, 87, 90, 13, 16, 22, 24, 28, 29, 35, 42, 46, 47,
       48, 58, 59, 60, 61, 70, 72, 77, 79, 85, 93, 95,  8,  8, 38, 40, 44,
       44, 56, 57, 89, 89,  6,  6, 33, 33, 33, 33, 33, 75, 75, 75, 75, 75,
       75, 76, 76, 76, 76, 76, 76, 76, 76, 76,  2, 50, 50, 52, 52, 91, 91,
       91,  9, 12, 17, 20, 21, 23, 25, 27, 31, 36, 37, 41, 49, 51, 53, 62,
       64, 65, 68, 74, 81, 83, 87, 90, 13, 16, 22, 24, 28, 29, 35, 42, 46,
       47, 48, 58, 59, 60, 61, 70, 72, 77, 79, 85, 93, 95,  8,  8, 38, 40,
       44, 44, 56, 57, 89, 89,  6,  6, 33, 33, 33, 33, 33, 75, 75, 75, 75,
       75, 75, 76, 76, 76, 76, 76, 76, 76, 76, 76,  4,  0,  1,  2,  3,  5,
        7, 10, 11, 14, 15, 18, 19, 19, 26, 30, 32, 34, 39, 43, 45, 50, 50,
       52, 52, 54, 55, 55, 63, 66, 67, 69, 71, 73, 78, 91, 91, 91, 80, 82,
       84, 86, 88, 92, 94,  9, 12, 17, 20, 21, 23, 25, 27, 31, 36, 37, 41,
       49, 51, 53, 62, 64, 65, 68, 74, 81, 83, 87, 90, 13, 16, 22, 24, 28,
       29, 35, 42, 46, 47, 48, 58, 59, 60, 61, 70, 72, 77, 79, 85, 93, 95,
        8,  8, 38, 40, 44, 44, 56, 57, 89, 89,  6,  6, 33, 33, 33, 33, 33,
       75, 75, 75, 75, 75, 75, 76, 76, 76, 76, 76, 76, 76, 76, 76,  4,  0,
        1,  2,  3,  5,  7, 10, 11, 14, 15, 18, 19, 19, 26, 30, 32, 34, 39,
       43, 45, 50, 50, 52, 52, 54, 55, 55, 63, 66, 67, 69, 71, 73, 78, 91,
       91, 91, 80, 82, 84, 86, 88, 92, 94])
       '''

label2 = le.fit_transform(X1['risk_factor_strata'])
X1.drop("risk_factor_strata", axis=1, inplace=True)
X1['risk_factor_strata'] = label2
print(X1)


# Initialize the StandardScaler
scaler1 = StandardScaler()

# Fit the scaler to the features and transform
X1_scaled = scaler1.fit_transform(X1)

# Split the scaled data into training, validation, and testing sets (70%, 15%, 15%)
X1_train, X1_temp, y1_train, y1_temp = train_test_split(X1_scaled, y1, test_size=0.3, random_state=42)
X1_val, X1_test, y1_val, y1_test = train_test_split(X1_temp, y1_temp, test_size=0.5, random_state=42)

# Check the size of each set
(X1_train.shape, X1_val.shape, X1_test.shape)
'''
((232, 4), (50, 4), (50, 4))
'''

#----------------Dataset #2 ---------------

#load dataset
flu_data = pd.read_csv('datasets/clean_influenza.csv')

# Display the first few rows of the dataframe
flu_data.head()
'''
   Unnamed: 0  estimated_vax_percent season_survey_year    geography  month                 dimension
0           0                   49.0            2020-21  Connecticut      4  18-49 Years at High Risk
1           1                   52.8            2020-21  Connecticut      5  18-49 Years at High Risk
2           4                    0.1            2012-13  Connecticut      7               18-49 Years
3           5                   32.2            2011-12  Connecticut      5               18-49 Years
4           7                    3.7            2012-13  Connecticut      9               18-49 Years
'''
# Define the features and the target variable
X2 = flu_data[['season_survey_year','geography', 'month', 'dimension']] # Features
y2 = flu_data['estimated_vax_percent']  # Target variable (estimated_vax_percent)

#Error message when scaling- ValueError: could not convert string to float: '2020-21'
 
# Creating a instance of label Encoder.
le = LabelEncoder()
 
# Using .fit_transform function to fit label
# encoder and return encoded label
label3 = le.fit_transform(X2['season_survey_year'])
label4 = le.fit_transform(X2['geography'])
label5 = le.fit_transform(X2['dimension'])

#drop old column and replace with encoded values column
X2.drop("season_survey_year", axis=1, inplace=True)
X2['season_survey_year'] = label3

X2.drop("geography", axis=1, inplace=True)
X2['geography'] = label4

X2.drop("dimension", axis=1, inplace=True)
X2['dimension'] = label5
print(X2)

# Initialize the StandardScaler
scaler2 = StandardScaler()

# Fit the scaler to the features and transform
X2_scaled = scaler2.fit_transform(X2)

# Split the scaled data into training, validation, and testing sets (70%, 15%, 15%)
X2_train, X2_temp, y2_train, y2_temp = train_test_split(X2_scaled, y2, test_size=0.3, random_state=42)
X2_val, X2_test, y2_val, y2_test = train_test_split(X2_temp, y2_temp, test_size=0.5, random_state=42)

# Check the size of each set
(X2_train.shape, X2_val.shape, X2_test.shape)
'''
((117219, 4), (25119, 4), (25119, 4))
'''