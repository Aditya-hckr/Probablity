import numpy as np
# not changing payoff matrix in this part due to error not rectifiable by me
payoff = [
    [(0.5, 0, 0.5), (7/10, 0, 3/10), (5/11, 0, 6/11)], 
    [(3/10, 0, 7/10), (1/3, 1/3, 1/3), (3/10, 1/2, 1/5)], 
    [(6/11, 0, 5/11), (1/5, 1/2, 3/10), (1/10, 4/5, 1/10)]
]

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if 15*self.points > 29*(len(self.results)-self.points):
            return 2
        else:
            return 0
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = np.random.choice([0, 1, 2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result
 

def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    a_style = alice.play_move()
    b_style = bob.play_move()
    monte_carlo_randum_num = np.random.rand()
    if a_style == 0 and b_style == 0:
        pb = alice.points / (alice.points + bob.points)
        pa = bob.points / (alice.points + bob.points)
        if monte_carlo_randum_num < pa:
            alice.observe_result(a_style, b_style, 1)
            bob.observe_result(b_style, a_style, 0)
        else:
            alice.observe_result(a_style, b_style, 0)
            bob.observe_result(b_style, a_style, 1)
    else:
        pa, d, pb = payoff_matrix[a_style][b_style]
        if monte_carlo_randum_num < pa:
            alice.observe_result(a_style, b_style, 1)
            bob.observe_result(b_style, a_style, 0)
        elif pa < monte_carlo_randum_num < pa + d:
            alice.observe_result(a_style, b_style, 0.5)
            bob.observe_result(b_style, a_style, 0.5)
        else:
            alice.observe_result(a_style, b_style, 0)
            bob.observe_result(b_style, a_style, 1)


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    alice = Alice()
    bob = Bob()
    for _ in range(2,num_rounds):
        simulate_round(alice, bob, payoff)
    
    print(f"Alice's points: {alice.points}")
    print(f"Bob's points: {bob.points}")
    
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10**5)