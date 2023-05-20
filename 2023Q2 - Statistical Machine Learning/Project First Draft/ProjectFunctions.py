from time import time
from sklearn.preprocessing import MinMaxScaler, QuantileTransformer
import random
from csv import DictWriter
from sklearn.metrics import f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from imblearn.under_sampling import RandomUnderSampler, OneSidedSelection, NearMiss, TomekLinks
from imblearn.over_sampling import RandomOverSampler, SMOTE, BorderlineSMOTE, ADASYN, SVMSMOTE


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
##                                           ##
##           Imbalance   Functions           ##
##                                           ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

def baseline(X,y):  return X,y


###   UNDERSAMPLING TECHNIQUES   ### 

def Undersample(X,y):  return RandomUnderSampler().fit_resample(X,y)
# Random Undersampling

def OneSided(X,y):  return OneSidedSelection().fit_resample(X,y)
# Undersampling using a Nearest Neighbor Strategy
#  to attempt to remove less informative data points    

def Near_Miss(X,y):  return NearMiss().fit_resample(X,y)
# Calculate the distance between the members of the majority class 
#  and members of the minority class.

def Tomek_Links(X,y):  return TomekLinks().fit_resample(X,y)


###   OVERSAMPLING TECHNIQUES   ###

def Oversample(X,y):  return RandomOverSampler().fit_resample(X, y)
# Random Oversampling

def smote(X,y):  return SMOTE().fit_resample(X,y)
# Oversample with additional synthetic members

def borderline_smote(X,y):  return BorderlineSMOTE().fit_resample(X,y)
# SMOTE biased toward the boundary

def adasyn(X,y):  return ADASYN().fit_resample(X,y)
# Resampling where the minority samples are weighted 
#   based on difficulty of NN classification 

def svmsmote(X,y):  return SVMSMOTE().fit_resample(X,y)
# Resampling where the minority samples are synthesized 
#   from and area determined using an SVM algorithm.


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
##                                           ##
##           Classifier  Functions           ##
##                                           ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def KNN(X_aug,y_aug,X_tt,y_tt):
    # defining parameter range
    param_grid = dict(n_neighbors = [1,3,5,7,9,11,13,15,17,19] )  #odd numbers because there are 2 classes in target coulmn
    gridKNN = GridSearchCV(KNeighborsClassifier(), param_grid, refit = True, scoring='f1')

    # fitting the model for grid search
    gridKNN.fit(X_aug,y_aug)

    # extract the relevant parameters
    train_f1 = gridKNN.best_score_
    params = {'k': gridKNN.best_params_['n_neighbors']}
    test_f1 = f1_score(y_tt,gridKNN.predict(X_tt))
    return train_f1, test_f1, params


def DecisionTree(X_aug,y_aug,X_tt,y_tt):
    dt = DecisionTreeClassifier()
    dt = dt.fit(X_aug,y_aug)

    # defining parameter range
    param_grid = {'max_depth':range(1, dt.tree_.max_depth+1, 2),
                'max_features': range(1, len(dt.feature_importances_)+1)}  
    gridDT = GridSearchCV(DecisionTreeClassifier(), param_grid, n_jobs=-1, refit = True, scoring='f1')
    
    # fitting the model for grid search
    gridDT.fit(X_aug,y_aug)
    
    # extract the relevant parameters
    train_f1 = gridDT.best_score_
    params = {'MaxDepth': gridDT.best_params_['max_depth'],'MaxFeatures': gridDT.best_params_['max_features']}
    test_f1 = f1_score(y_tt,gridDT.predict(X_tt))
    return train_f1, test_f1, params


def RandomForest(X_aug,y_aug,X_tt,y_tt):
    RF = RandomForestClassifier(oob_score=True, 
                                warm_start=True,
                                n_jobs=-1)
    param_grid = {'n_estimators':[15, 20, 30, 40, 50, 100, 150, 200, 300, 400]
                }  
    gridRF = GridSearchCV(RF, param_grid, scoring='f1')
    gridRF.fit(X_aug,y_aug)
    
    train_f1 = gridRF.best_score_ 
    params = {'n-Estimators': gridRF.best_params_['n_estimators']}
    test_f1 = f1_score(y_tt,gridRF.predict(X_tt))
    return train_f1, test_f1, params


def ExtraTrees(X_aug,y_aug,X_tt,y_tt):
    ET = ExtraTreesClassifier(oob_score=True, bootstrap=True,
                            warm_start=True,
                            n_jobs=-1)
    param_grid = {'n_estimators':[15, 20, 30, 40, 50, 100, 150, 200, 300, 400]
                }  
    gridRF = GridSearchCV(ET, param_grid, scoring='f1')
    gridRF.fit(X_aug,y_aug)
    
    train_f1 = gridRF.best_score_ 
    params = {'n-Estimators': gridRF.best_params_['n_estimators']}
    test_f1 = f1_score(y_tt,gridRF.predict(X_tt))
    return train_f1, test_f1, params


## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
##                                           ##
##           Experiment  Functions           ##
##                                           ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##


def test(df, rho, tech, classifier, fields, label='Diabetes', filename = 'test_results.csv', trainSize=0.2):

    # Perform synthetic minoritization
    df_r, minor_count = subsample(df, label, 1, rho)
    X = df_r.drop(label, axis=1)
    y = df_r[label]
    
    # Train and Test Split
    X_tn, X_tt, y_tn, y_tt = train_test_split(X, y, train_size= trainSize)

    # Perform imbalance handling technique on new data
    start_time = time()
    X_aug,y_aug = tech(X_tn,y_tn)
    tech_time = (time()-start_time)

    # Test the chosen classifier
    start_time = time()
    train_f1, test_f1, params = classifier(X_aug,y_aug,X_tt,y_tt)
    runtime = (time()-start_time+tech_time)
    results = {'Rho': rho,'Imbalance Technique': tech.__name__, 'Classifier': classifier.__name__, 
                'Minority Count': minor_count, 'Training f1': train_f1, 'Test f1': test_f1,
                'Runtime': runtime} | params

    # Write the results to the csv record
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = DictWriter(csvfile, fieldnames = fields)                                        
        # writing the data rows 
        csvwriter.writerow(results)
        csvfile.close()
# End Test


def subsample(df, label_column, target_label, rho):
    """
    Removes a random subsample of data with a specific label from a pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        label_column (str): The column name containing the labels.
        target_label: The label for which the subsample will be removed.
        rho (int): The size of the desired ratio of majority/minority.

    Returns:
        pd.DataFrame: The updated DataFrame with the subsample removed.
    """
    # Filter the DataFrame to include only the data with the target label
    target_df = df[df[label_column] == target_label]

    # Determine the size necessary to produce the desired Rho value
    minor_size = len(target_df)
    sample_size = int( minor_size / rho)

    # Calculate the samples needed to be dropped to meet Rho goal
    drop_size = minor_size - sample_size

    # Randomly select sample_size number of indices to remove
    random_indices = random.sample(target_df.index.tolist(), drop_size)

    # Remove the selected indices from the DataFrame
    updated_df = df.drop(random_indices)

    return updated_df, sample_size
# End Subsample


def scrub_diabetes(df, verbose=False):
    """
    Clean and process the diabets data using the processed developed by Solafa Jobi
        at https://www.kaggle.com/code/solafajobi/diabetes-perfect-prediction

    Args:
        df (pd.DataFrame): The DataFrame containing the data.

    Returns:
        pd.DataFrame: The updated DataFrame after cleaning.
    """

    # Select variables that are medically likely to predict diabetes
    dm = df[["Age", "HighChol", "BMI", "PhysActivity", "PhysHlth", "HighBP", "Diabetes"]]

    # Scale and transform numeric columns
    mms = MinMaxScaler()
    qt = QuantileTransformer(n_quantiles=500, output_distribution='normal')
    dm[['BMI', 'Age', 'PhysHlth']] = mms.fit_transform(dm[['BMI', 'Age', 'PhysHlth']])
    dm[['BMI', 'PhysHlth']] = qt.fit_transform(dm[['BMI', 'PhysHlth']])
    
    # Output a summary
    if verbose:
        print(dm.head())
    
    return dm
# End Scrub Diabetes


def newFile(filename, fields):
    with open(filename, 'w') as csvfile:
        csvwriter = DictWriter(csvfile, fieldnames = fields)                                        
        # writing the data rows 
        csvwriter.writeheader()
        csvfile.close()