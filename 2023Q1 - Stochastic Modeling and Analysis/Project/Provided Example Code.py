import numpy as np
from scipy.stats import binom
import time

# Define DTMC Model Parameters
NUM_ACFT = 12
MAX_SORTIES = 8
PROB_PASS_POSTFLT_INSP = 0.8
PROB_REPAIR_FRONTSHOP = 0.7
PROB_PASS_POST_BACKSHOP_INSP = 0.8

# Construct State space S, as an 1820x5 array; 
# row as an index label for the 5-tuple state variable
S = []
for x0 in range(NUM_ACFT+1):
    for x1 in range(NUM_ACFT+1-x0):
        for x2 in range(NUM_ACFT+1-x0-x1):
            for x3 in range(NUM_ACFT+1-x0-x1-x2):
                S.append([x0, x1, x2, x3, NUM_ACFT-x0-x1-x2-x3])

# Convert list to numpy array
S= np.array(S)
cardS = len(S)

# Define utility functions to access state indices and vectors
def state_to_index(state):
    return np.were((S == tuple(sstate)).all(axis=1))[0][0]

def index_to_state(index):
    return S[index]

## Compute 1-step transition probability matrix
# with timer
tic = time.perf_counter()
P = np.matrix(np.zeros((cardS,cardS)))
for i_index in range(cardS):
    # Obtain State Variable
    X_n = index_to_state(i_index)

    ### Compute pmf of X_np1[1], Front Shop first,
    ##  compute pmfs of intermediate random variables,
    # pmf of number of acft inbound to front shop from MC post inspection
    num_MC = X_n[0]
    num_acft_fly = np.min((MAX_SORTIES, num_MC))
    pmf_Yn_MC_failed = [binom.pmf(y,num_acft_fly,1-PROB_PASS_POSTFLT_INSP) for y in range(NUM_ACFT+1)]
    # PMF of acft inbound to front shop from back shop inspection
    num_BS3 = X_n[4]
    pmf_Yn_BS3_failed = [binom.pmf(y,num_BS3,1-PROB_PASS_POST_BACKSHOP_INSP) for y in range(NUM_ACFT+1)]
    pmf_Xnpl_FS = np.convolve(pmf_Yn_MC_failed,pmf_Yn_BS3_failed)
    
    ### Compute PMF of X_npl[2], Back Shop 1
    num_FS = X_n[1]
    pmf_Xnpl_BS1 = [binom.pmf(y,num_FS,1-PROB_REPAIR_FRONTSHOP) for y in range(NUM_ACFT+1)]
    ### Compute PMF of X_npl[3], Back Chop 2
    pmf_Xnpl_BS2 = np.zeros((NUM_ACFT+1))
    pmf_Xnpl_BS2[X_n[2]] = 1
    ### Compute PMF of X_npl[4], Back Chop 3
    pmf_Xnpl_BS3 = np.zeros((NUM_ACFT+1))
    pmf_Xnpl_BS3[X_n[3]] = 1
    ### PMF of X_npl[0], FMC aircraft is implicit as the 
    ## sum of previous four and this must equal NUM_ACFT.

    ### Assign 1-step probabilities based on PMFs
    ## SLOWER METHOD:
    # for j_index in range(cardS):
    #     X_npl = index_to_state(j_index)
    #     P[i_index,j_index] = \
    #         pmf_Xnpl_FS[X_npl[1]]*pmf_Xnpl_BS1[X_npl[2]]*pmf_Xnpl_BS2[X_npl[3]]*pmf_Xnpl_BS3[X_npl[4]]
    ## FASTER METHOD:
    for j_index in (j_index_filtered for j_index_filtered in range(cardS) if \
                    index_to_state(j_index_filtered)[4]==X_n[3] and
                    index_to_state(j_index_filtered)[3]==X_n[2] and
                    index_to_state(j_index_filtered)[2]<=X_n[1] and
                    index_to_state(j_index_filtered)[1]<=num_acft_fly+num_BS3):
        X_npl = index_to_state(j_index)
        P[i_index,j_index] = \
            pmf_Xnpl_FS[X_npl[1]]*pmf_Xnpl_BS1[X_npl[2]]*pmf_Xnpl_BS2[X_npl[3]]*pmf_Xnpl_BS3[X_npl[4]]

# End Timer
toc = time.perf_counter()

print(f"\nP matrix computed in {toc-tic:0.4f} secs.")

# Check P matrix rowsums and number of nonzeros
print(f"\nSum of |S| = {cardS} rows is {np.sum(P)}.") # Exp 1820
print(f"\nNumber of non-zero elements is {np.count_nonzero(P)}.") # Exp 30856