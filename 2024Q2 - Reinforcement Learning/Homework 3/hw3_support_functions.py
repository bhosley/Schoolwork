from scipy.stats.qmc import LatinHypercube
from joblib import Parallel, delayed
from datetime import datetime
import time

import matplotlib. pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures
from statsmodels.formula.api import ols

NUM_CPU_CORE_PROCS = 6
column_names = ["Run Index", "eps_a", "eps_b", "Init Qbar", "Sup EETDR", "Sup EETDR hw", "Mean Max EETDR", "Mean Max EETDR hw", "Time-Avg EETDR", "Time-Avg EETDR hw", "Secs per run", "Score"]

def parallel_lhs(experiment, num_runs=10, num_alg_feats=3, rng_seed=0):
    """ Execute LHS Experiment in Parallel """
     # Needs 40

    sampler = LatinHypercube(num_alg_feats, scramble=False, optimization="lloyd", seed=rng_seed)
    # sampler = LatinHypercube(num_alg_feats,seed=rng_seed)
    factor_table = sampler.random(n=num_runs)

    print(f"\nInitializing LHS experiment wie = time.time()th {num_runs} runs...")
    experiment_start_time = time.time()
    # create an instance of the Parallel object to manage execution of our processes
    parallel_manager = Parallel(n_jobs = NUM_CPU_CORE_PROCS)
    # generate a list of function calls to run_experiment () for each row of the factor table 
    # each row of the factor table is an algorithm design run 
    # delayed () creates the list without actually executing run_experiment ()
    run_list = (delayed (experiment)(run_index, factor_table[run_index]) for run_index in range (num_runs) )
    #execute the list of run_experiment() calls in parallel
    print ("\nExecuting experiment...")
    results_table = parallel_manager (run_list)
    results_table = np.array(results_table)
    print (f"\n\nCompleted experiment ({time.time () - experiment_start_time:.3f}s)")

    # combine the factor table with the results table, add column headers, and save the date to a CSV file
    # compute algorithm run score, the average of the 95% CI lowerbounds for maximum and mean performance
    maxEETDR_95CI_LB = results_table[:,3] - results_table[:,4]
    meanEETDR_95CI_LB = results_table[:,5] - results_table[:,6]
    score = 0.6*maxEETDR_95CI_LB + 0.4*meanEETDR_95CI_LB
    results_table = np.column_stack((results_table[:,0], factor_table, results_table[:,1:], score))
    # grab data for performance scatter plot
    results_table = np.row_stack((column_names, results_table))
    filename_DOE = "MCC_onpolicy_results_DOE_" + datetime.now().strftime('%Y%m%d_%H%M%S') + ".csv"
    np.savetxt(filename_DOE, results_table, delimiter = ",", fmt = "%s")

    return factor_table, results_table

def plot_results(results_table):
    x = np.array(results_table[1:,6],float) # 0-index appears to be title
    y = np.array(results_table[1:,8],float) # 0-index appears to be title
    # create scatter plot
    plt. scatter(x, y, label="MCC (on-policy) -- 40 reps per run, 10k episodes per rep")
    # setting title and labels
    plt.title("MCC (on-policy) LHS DOE Performance Results")
    plt.xlabel("Mean Maximum EETDR")
    plt.ylabel("Mean Time-Average EETDR")
    # grid on
    plt.grid()
    # legend on
    plt.legend(loc='upper left', fontsize=7)
    # display the plot
    plt.show()

def anova(factor_table, results_table, num_alg_feats=3):
    # Input data
    X = factor_table

    # Generate full factorial polynomial function up to degree 2
    poly = PolynomialFeatures(2)
    X_poly = poly.fit_transform(X)

    # Clean up the feature names
    input_features = column_names[1:num_alg_feats+1]
    feature_names = [name.replace(' ','_').replace('^','_pow_').replace('*','_times_')
                    for name in poly.get_feature_names_out(input_features=input_features)]
    df = pd.DataFrame(X_poly, columns=feature_names)

    # define response variable
    maxEETDR_95CI_LB  = np.array(results_table[1:,3],float) - np.array(results_table[1:,4],float)
    meanEETDR_95CI_LB = np.array(results_table[1:,5],float) - np.array(results_table[1:,6],float)
    score = 0.6*maxEETDR_95CI_LB + 0.4*meanEETDR_95CI_LB
    df['AlgScore'] = score

    # Create the formula string for the OLS model
    # Exclude the first column (the constant term) from the predictors
    predictors = '+'.join(df.columns[1:-1]) # Exclude '1' and 'y'
    formula = f'AlgScore ~ {predictors}'

    # Create and fit the OLS model
    model = ols(formula, data=df)
    results = model.fit()

    # Display the summary
    print ("\n\n" )
    print (results.summary())

    # Perform ANOVA and display the table
    anova_results = sm.stats.anova_lm(results, typ=2)
    print(anova_results)