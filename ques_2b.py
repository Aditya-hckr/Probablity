import numpy as np

class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1

    def play_move(self):
        """
        Decide Alice's play style for the current round. If you think there is no better strategy than 2a,
        then implement the same strategy here. Else implement that non greedy strategy here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if self.results[-1] == 1:  
            na = self.points
            nb = len(self.results) - na
            if nb / len(self.results) >= 6 / 11:
                return 0  
            else:
                return 2  
        elif self.results[-1] == 0: 
            return 1  
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
        if self.results[-1] == 1:
            return 2
        elif self.results[-1] == 0.5:
            return 1
        else:  
            return 0
        
        
    
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
        payoff_matrix[0][0] = alice.points / (alice.points + bob.points)
        payoff_matrix[0][2] = bob.points / (alice.points + bob.points)
        if monte_carlo_randum_num < payoff_matrix[0][0]:
            alice.observe_result(a_style, b_style, 1)
            bob.observe_result(b_style, a_style, 0)
        else:
            alice.observe_result(a_style, b_style, 0)
            bob.observe_result(b_style, a_style, 1)
    else:
        prob_alice, prob_draw, prob_bob = payoff_matrix[a_style][b_style]
        if monte_carlo_randum_num < prob_alice:
            alice.observe_result(a_style, b_style, 1)
            bob.observe_result(b_style, a_style, 0)
        elif prob_alice < monte_carlo_randum_num < prob_alice + prob_draw:
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
    payoff = [
    [(0.5, 0, 0.5), (7/10, 0, 3/10), (5/11, 0, 6/11)], 
    [(3/10, 0, 7/10), (1/3, 1/3, 1/3), (3/10, 1/2, 1/5)], 
    [(6/11, 0, 5/11), (1/5, 1/2, 3/10), (1/10, 4/5, 1/10)]
    ]
    for r in range(num_rounds):
        simulate_round(alice, bob, payoff)
    
    print(f"Alice's points after 10^5 rounds: {alice.points}")
    print(f"Bob's points after 10^5 rounds: {bob.points}")
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    monte_carlo(num_rounds=10**5)