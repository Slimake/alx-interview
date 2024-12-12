#!/usr/bin/python3
"""0-prime_game
"""

def isWinner(x, nums):
    """IsWinner function"""
    # Max number that needs to be considered
    max_n = max(nums)

    # Sieve of Eratosthenes to find all primes up to max_n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Function to simulate one round for a given n
    def determine_winner(n):
        """Determine winner function"""
        # List of primes <= n
        primes = [i for i in range(2, n + 1) if is_prime[i]]

        # Simulate the game, with Maria always starting
        available = [True] * (n + 1)  # Track available numbers
        moves = 0  # Number of moves made

        while True:
            # Find the first available prime
            found_move = False
            for prime in primes:
                if prime <= n and available[prime]:
                    found_move = True
                    # Mark prime and its multiples as unavailable
                    for multiple in range(prime, n + 1, prime):
                        available[multiple] = False
                    moves += 1
                    break

            if not found_move:
                # No valid move, current player loses
                break

        # If moves is odd, Maria wins (since Maria starts)
        return 'Maria' if moves % 2 == 1 else 'Ben'

    # Determine the winner for each round and count the results
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = determine_winner(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    # Return the player who won the most rounds, or None if it's a tie
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
