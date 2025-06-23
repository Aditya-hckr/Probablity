import numpy as np
import time
def stationary_distribution(p, q, r, N):
    """
    Return a list of size N+1 containing the stationary distribution of the Markov chain.
    
    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    
    """
    P = np.zeros((N+1,N+1))
    for i in range(N+1):
        if i>0 and i<N:
            P[i,i]=r[i]
            P[i,i+1]=p[i]
            P[i,i-1]=q[i]
        elif i==0:
            P[i,i]=r[i]
            P[i,i+1]=p[i]
        elif i==N:
            P[i,i]=r[i]
            P[i,i-1]=q[i]
    A = P.T - np.eye(P.shape[0])
    A = np.vstack([A, np.ones(N+1)])
    b = np.zeros(N+2)
    b[-1] = 1
    dist = np.linalg.lstsq(A, b, rcond=None)[0]
    return dist

def expected_wealth(p, q, r, N):
    """
    Return the expected wealth of the gambler in the long run.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    """
    P = np.zeros((N+1,N+1))
    for i in range(N+1):
        if i>0 and i<N:
            P[i,i]=r[i]
            P[i,i+1]=p[i]
            P[i,i-1]=q[i]
        elif i==0:
            P[i,i]=r[i]
            P[i,i+1]=p[i]
        elif i==N:
            P[i,i]=r[i]
            P[i,i-1]=q[i]
    A = P.T - np.eye(P.shape[0])
    A = np.vstack([A, np.ones(N+1)])
    b = np.zeros(N+2).T
    b[-1] = 1
    dist = np.linalg.lstsq(A, b, rcond=None)[0]
    ans = 0
    for i in range(N+1):
        ans += i*dist[i]
    return ans
    
def expected_time(p, q, r, N, a, b):
    """
    Return the expected time for the price to reach b starting from a.

    p : array of size N+1, 0 < p[i] < 1, probability of price increase
    q : array of size N+1, 0 < q[i] < 1, probability of price decrease
    r : array of size N+1, r[i] = 1 - p[i] - q[i], probability of price remaining the same
    N : int, the maximum price of the stock
    a : int, the starting price
    b : int, the target price
    """
    T = np.zeros((b,b))
    for i in range(b):
        if i>0 and i<b-1:
            T[i,i]=1-r[i]
            T[i,i+1]=-p[i]
            T[i,i-1]=-q[i]
        elif i==0:
            T[i,i]=1-r[i]
            T[i,i+1]=-p[i]
        elif i==b-1:
            T[i,i]=1-r[i]
            T[i,i-1]=-q[i]
    B = np.ones(b)
    Exp_T = np.linalg.lstsq(T, B, rcond=None)[0]
    return Exp_T[a]