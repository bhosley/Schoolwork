import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
import time

# Define utility functions to access state indices and vectors
def state_to_index(S,state):
    return np.where((S == tuple(state)).all(axis=1))[0][0]

def index_to_state(S,index):
    return S[index]

def lowest_sortie_capable_state(S,NUM_ACFT,MAX_SORTIES):
    state = [MAX_SORTIES,0,0,0,NUM_ACFT-MAX_SORTIES]
    index = state_to_index(S,state)
    return index

def sortie_capable_indices(S,NUM_ACFT,MAX_SORTIES):
    state = [MAX_SORTIES,0,0,0,NUM_ACFT-MAX_SORTIES]
    start_index = state_to_index(S,state)
    end_index = len(S)
    indices = range(start_index, end_index)
    return indices

def sortie_capable_probability(aN,S,NUM_ACFT,MAX_SORTIES):
    state = lowest_sortie_capable_state(S,NUM_ACFT,MAX_SORTIES)
    prob = np.sum(aN[0,state:])
    return prob

# Creation of P-matrix and State Space
def create_one_step_P_matrix(
        # Returns np.array of P-matrix, and State spaces
        # Define DTMC Model Parameters
        NUM_ACFT = 12,
        MAX_SORTIES = 8,
        PROB_PASS_POSTFLT_INSP = 0.8,
        PROB_REPAIR_FRONTSHOP = 0.7,
        PROB_PASS_POST_BACKSHOP_INSP = 0.8):

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

    ## Compute 1-step transition probability matrix
    # with timer
    tic = time.perf_counter()
    P = np.matrix(np.zeros((cardS,cardS)))
    for i_index in range(cardS):
        # Obtain State Variable
        X_n = index_to_state(S,i_index)

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
                        index_to_state(S,j_index_filtered)[4]==X_n[3] and
                        index_to_state(S,j_index_filtered)[3]==X_n[2] and
                        index_to_state(S,j_index_filtered)[2]<=X_n[1] and
                        index_to_state(S,j_index_filtered)[1]<=num_acft_fly+num_BS3):
            X_npl = index_to_state(S,j_index)
            P[i_index,j_index] = \
                pmf_Xnpl_FS[X_npl[1]]*pmf_Xnpl_BS1[X_npl[2]]*pmf_Xnpl_BS2[X_npl[3]]*pmf_Xnpl_BS3[X_npl[4]]

    # End Timer
    toc = time.perf_counter()

    print(f"\nP matrix computed in {toc-tic:0.4f} secs.")

    # Check P matrix rowsums and number of nonzeros
    print(f"\nSum of |S| = {cardS} rows is {np.sum(P)}.") # Exp 1820
    print(f"\nNumber of non-zero elements is {np.count_nonzero(P)}.") # Exp 30856

    return P, S

# Long term (pi) calculations
def get_pi(P):
    # Define the p-matrix
    cardS, _ = np.shape(P)
    I = np.matrix(np.eye(cardS))

    # Construct system of linear equations, Ax=b
    # LHS
    A_bal = I-P.T
    A_norm = np.matrix(np.ones(cardS))

    # RHS
    b_bal = np.matrix(np.zeros((cardS,1)))
    b_norm = np.matrix(1)

    # vertically stack
    A = np.vstack((A_bal,A_norm))
    b = np.vstack((b_bal,b_norm))

    # Remove an overdetermining member equation
    A = np.delete(A,0,0)
    b = np.delete(b,0,0)

    # Solve
    pi = np.linalg.solve(A,b)
    return pi.T

bake = get_pi

# First Passage Calculation
def first_passage_times(P,S,NUM_ACFT,MAX_SORTIES):
    cardS, _ = np.shape(P)
    I = np.matrix(np.eye(cardS))
    s = lowest_sortie_capable_state(S,NUM_ACFT,MAX_SORTIES)
    B = P[:s,:s]
    e = np.ones((cardS,1))
    m = np.linalg.solve(I-B,e)
    return m

# Display Functions
def display_behavior(a,P,S,NUM_ACFT,MAX_SORTIES,n=10,condition = 'Baseline',pi=None):
    pi = pi or get_pi(P)
    pie = 1-sortie_capable_probability(pi,S,NUM_ACFT,MAX_SORTIES)
    x,y,f = np.empty(0),np.empty(0),np.empty(0)
    i=0
    aN = a*P
    x = np.append(x,i*1200)
    f = np.append(f,pie)
    y = np.append(y,1-sortie_capable_probability(aN,S,NUM_ACFT,MAX_SORTIES))
    while (i<n):
        i+=1
        aN = aN*P
        x = np.append(x,i*1200)
        f = np.append(f,pie)
        y = np.append(y,1-sortie_capable_probability(aN,S,NUM_ACFT,MAX_SORTIES))

    fig, ax = plt.subplots()
    ax.plot(x,f, color='black', label='Long-term')
    ax.annotate('{}%'.format('%.3f'%(pie*100)) ,xy=(x[-1],f[0]),xytext=(x[-1]+100,f[0]+0.01))
    ax.fill_between(x, 0, y, alpha=0.5, color='red', label='Unmet')
    ax.fill_between(x, 1, y, alpha=0.5, label='Met')
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(0, 1)
    ax.set(xlabel='T+ hours', xticks=x, ylabel='',
        title='Probability of Meeting Sortie Requirement: {}'.format(condition))
    ax.legend(loc='upper right')
    ax.grid()



