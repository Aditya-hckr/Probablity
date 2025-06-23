"""
Use the following functions to add, multiply and divide, taking care of the modulo operation.
Use mod_add to add two numbers taking modulo 1000000007. ex : c=a+b --> c=mod_add(a,b)
Use mod_multiply to multiply two numbers taking modulo 1000000007. ex : c=a*b --> c=mod_multiply(a,b)
Use mod_divide to divide two numbers taking modulo 1000000007. ex : c=a/b --> c=mod_divide(a,b)
"""
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))

def fact_mod(n):
    result = 1
    for i in range(2, n + 1):
        result = mod_multiply(result, i)
    return result

# Problem 1a

def calc_prob(alice_wins, bob_wins):
    prob = [[0 for i in range(bob_wins + 1)] for j in range(alice_wins + 1)]

    prob[1][1] = 1  
    
    for i in range(2, alice_wins + 1):
        prob[i][1] = mod_divide(1, fact_mod(i))
    for i in range(2, bob_wins + 1):
        prob[1][i] = mod_divide(1, fact_mod(i))
    
    for i in range(2, alice_wins + 1):
        for j in range(2, bob_wins + 1):
            term1 = mod_multiply(prob[i-1][j], mod_divide(j, (i+j-1)))
            term2 = mod_multiply(prob[i][j-1], mod_divide(i, (i+j-1)))
            prob[i][j] = mod_add(term1, term2)

    return prob[alice_wins][bob_wins]

# Problem 1b (Expectation)      
def calc_expectation(t):
    prob = [[0 for i in range(t + 1)] for j in range(t + 1)]

    prob[1][1] = 1
    prob[1][2] = mod_divide(1, 2)  
    prob[2][1] = mod_divide(1, 2)  
    
    for i in range(2, t + 1):
        prob[i][1] = mod_divide(1, fact_mod(i))
    for i in range(2, t + 1):
        prob[1][i] = mod_divide(1, fact_mod(i))
    
    for i in range(2, t + 1):
        for j in range(2, t + 1):
            term1 = mod_multiply(prob[i-1][j], mod_divide(j, (i+j-1)))
            term2 = mod_multiply(prob[i][j-1], mod_divide(i, (i+j-1)))
            prob[i][j] = mod_add(term1, term2)
    Expectation=0
    for y in range(-(t-2), t-1, 2):
        i=(t+y)//2 
        j=(t-y)//2 
        Expectation = mod_add(Expectation, mod_multiply(y,prob[i][j]))
    return Expectation

# Problem 1b (Variance)
def calc_variance(t):
    prob = [[0 for i in range(t + 1)] for j in range(t + 1)]

    prob[1][1] = 1
    prob[1][2] = mod_divide(1, 2)  
    prob[2][1] = mod_divide(1, 2)  
    
    for i in range(2, t + 1):
        prob[i][1] = mod_divide(1, fact_mod(i))
    for i in range(2, t + 1):
        prob[1][i] = mod_divide(1, fact_mod(i))
    
    for i in range(2, t + 1):
        for j in range(2, t + 1):
            term1 = mod_multiply(prob[i-1][j], mod_divide(j, (i+j-1)))
            term2 = mod_multiply(prob[i][j-1], mod_divide(i, (i+j-1)))
            prob[i][j] = mod_add(term1, term2)

    Variance=0
    for y in range(-(t-2), t-1, 2):
        i=(t+y)//2
        j=(t-y)//2
        y=y**2
        Variance = mod_add(Variance, mod_multiply(y,prob[i][j]))
    return Variance
    
print(f"Probability of Alice winning 93 rounds and Bob winning 61 rounds",calc_prob(93,61))
print(f"Expectation value for total of 61 rounds",calc_expectation(61))
print(f"Variance for total of 61 rounds",calc_variance(61))

