def win_probability(p, q, k, N):
    """
    Return the probability of winning a game of chance.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    N : int, maximum wealth
    """
    if k == 0:
        return 0
    if p == 0:
        return 0
    if p == q:
        return k/N
    r = float(q/p)
    numerator =  1 - pow(r,k)
    denominator = 1 - pow(r,N)
    return numerator/denominator

def limit_win_probability(p, q, k):
    """
    Return the probability of winning when the maximum wealth is infinity.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if p == 0:
        return 0
    if q >= p:
        return 0
    r = float(q/p)
    return 1 - pow(r,k)

def game_duration(p, q, k, N):
    """
    Return the expected number of rounds to either win or get ruined.
    
    p : float, 0 < p < 1, probability of winning a round
    q : float, q = 1 - p, probability of losing a round
    k : int, starting wealth
    """
    if k == 0 or k == N:
        return 0
    if p == 0:
        return k
    if q == 0:
        return N-k
    if p == q:
        return float(k*(N-k))
    r = float(q/p)
    numerator =  1 - pow(r,k)
    denominator = 1 - pow(r,N)
    res1 = float(k/(q-p)) 
    res2 = float((N/(q-p))*(numerator/denominator))
    ans = res1 - res2
    return ans