# Problem 3b
def optimal_strategy(na, nb, tot_rounds):
    """
    Calculate the optimal strategy for Alice maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds left(tot_rounds).
    
    Returns: 
        0 : attack
        1 : balanced
        2 : defence
    """

    dp = [[[0 for i in range(na+1)] for j in range(nb+1)] for k in range(tot_rounds+1)]
    for i in range(2,na+1):
        for j in range(2,nb+1):
            for k in range(2,tot_rounds+1):
                dp[i][j][k] = max(dp[i-1][j][k-1]*()