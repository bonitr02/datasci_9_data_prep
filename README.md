# Week 9: Data Preparation for Machine Learning
## Dataset #1 - Maternal Sepsis Rates
This dataset contains risk factors and maternal sepsis rates among live births between 2016 and 2018.

The intended machine learning task is regression for this dataset.

The dependent variable (y) is Live Births % and the independent variables (x) are Risk Factor, Risk Factor Strata, Any Sepsis Incidence (N) and Any Sepsis Incidence per 100,000 Live Births.

Steps Needed to Clean and Transform Data:
1.	Load the dataset using pandas
2.	Preview the dataframe to understand potential uses of data
3.	Check for missing values and white space and drop any rows with missing values
4.	Clean column names to a standard lowercase format, removing special characters
5.	Run descriptive statistics to understand the data distribution
	    
        - Use .describe() for numerical data    
        - Use .value_counts() for categorical data
    
6.	Normalize data if there are extreme outliers
7.	Encode categorical data to convert strings to int prior to scaling
8.  Scale data prior to splitting dataset to obtain an even distribution
9.	Split data into training, validation and testing sets

### Dataset 1 Sets, with 70%, 15%, 15% breakdown:

Training set: 232 rows and 4 columns
Validation set: 50 rows and 4 columns
Testing set: 50 rows and 4 columns

### Next Steps
1. Train a model, using linear regression to establish baseline performance
2. Fine tune the model with the validation set
3. Evaluate the model using the testing set, repeating the linear regression test

## Dataset #2 - Influenza Vaccination Rates
This dataset contains influenza vaccination survey data, including geography, demographics and vaccination rate.

The intended machine learning task is classification for this dataset.

The dependent variable (y) is Estimate (%) and dependent variables(x) are Geography, Season/Survey Year, Month, and Dimension 


Steps Needed to Clean and Transform Data:
1.	Load the dataset using pandas
2.	Preview the dataframe to understand potential uses of data
3.	Check for missing values and white space and drop any rows with missing values
4.	Clean column names to a standard lowercase format, removing special characters
5.  Change column types when necessary
6.	Run descriptive statistics to understand the data distribution
	    
        - Use .describe() for numerical data    
        - Use .value_counts() for categorical data
    
7.	Encode categorical data to convert strings to int prior to scaling
8.  Scale data prior to splitting dataset to obtain an even distribution
9.	Split data into training, validation and testing sets

### Dataset 2 Sets, with 70%, 15%, 15% breakdown:

Training set: 117219 rows and 4 columns
Validation set: 25119 rows and 4 columns
Testing set: 25119 rows and 4 columns    

### Next Steps
1. Train a model, using a decision tree to establish baseline performance
2. Fine tune the model with the validation set
3. Evaluate the model using the testing set, repeating the decision tree

# Error messages
- Received the error message "ValueError: could not convert string to float: 'Alcohol abuse'" when attempting to scale data in Dataset #1
    - Resolved by using the scikit-learn labelEncoder to convert string columns to int

# General Data Cleaning, Transformation and Training Steps for Machine Learning 
1. Data Collection - gather large dataset
2. Data Preprocessing 
    - Clean the data (missing values, remove duplicates)
    - Encoding- change nominal categorical data into boolean or integer value
    - Perform feature engineering and selection
3. Data Splitting - split the dataset rows into training, validation and testing sets. Defining Ys and Xs
    - Training set - 60%-80% of original data set
    - Validation set - 10%-20% of oriignal data set
    - Test set - 10%-20% of original data set
    - Use train_test_split from sklearn.model_selection to split into 2 datasets, then perform again on the testing test to further split
4. Model selection - choose appropriate algorithms (regression(predict a numerical output) vs classification (predict a categorical output))
5. Training phase - train models using training set
6. Validation Phase
    -fine-tune hyperparameters using the validation set
    -choose the best performing model based on validation metrics
7. Evaluation phase - assess final model performance using the test set and evaluate metrics
8. Model deployment
9. Feedback loop
