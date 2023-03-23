# %%
import numpy as np

def affineScale(c,A,x_0,lam_0=1,alpha=0.5, 
                termination_criteria=0.01,max_iter=50):
    print('Iteration:',' '*20,'x_k / y_k:',' '*20,'Objective Value:')
    lam = lam_0
    I = np.eye(len(x_0))
    x_i = x_0
    for k in range(max_iter):
        D_i = np.diag(x_i)
        y_i = np.linalg.inv(D_i)@x_i
        c_bar = c@D_i

        c_p = (I - ((A@D_i).T @ np.linalg.inv(A@(D_i@D_i.T)@A.T)@(A@D_i)))@c_bar.T
        d_i = (-D_i)@c_p
        y_j = y_i - lam*c_p
        x_j = x_i + lam*(d_i)
        arr = x_i/(-d_i)
        lammax = np.where(arr > 0, arr, np.inf).argmin()
        
        lam = alpha*lammax
        x_i = x_j
        print(' '*3,'%2i'%(k+1),' '*3, 'x:', x_i, '\n', ' '*9, 'y:', y_j, ' ', c@x_i)
        if np.linalg.norm(c_p) < termination_criteria : break


# %%
c = np.array([-1,-2,0,0])
A = np.array([[ 1,-1, 1, 0],[ 1, 2, 0, 1]])
x_0 = np.array([0.5,0.5,1,0.5])

affineScale(c,A,x_0,lam_0=0.25,max_iter=20)


