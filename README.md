# datasci_9_data_prep

# Data Cleaning and Transformation Plan
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

## Dataset #1
A brief description of each dataset.
The intended machine learning task for each dataset (classification or regression).
The steps needed to clean and transform the data. Consider aspects like missing values, outliers, encoding categorical variables, standardizing or normalizing, etc.
Identify the independent (predictors) and dependent (target) variables in each dataset.

## Dataset #2
A brief description of each dataset.
The intended machine learning task for each dataset (classification or regression).
The steps needed to clean and transform the data. Consider aspects like missing values, outliers, encoding categorical variables, standardizing or normalizing, etc.
Identify the independent (predictors) and dependent (target) variables in each dataset.

