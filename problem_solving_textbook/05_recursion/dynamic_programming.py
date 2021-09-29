"""
Let's make an algorithm to find the minimum number of coins for change
    > We have a 
        - 1 c
        - 5 c
        - 10 c
        - 21 c
        - 25 c
    
    > say we want 
    A greedy method would try 25, 25, 10, 1, 1, 1
    But 21, 21, 21 is the optimal answer


The structure of recusion would be:
> Base case.. if we need to make change for the same amount as one of out coins, it would require 1 coin

"""

def make_change_1(coin_value_list, change):
    # The min amount of coins possible is to just return all 1c coins
    min_coins = change
    
    # BASE CASE if we have a coin that is the same value required as change we only need on coin
    if change in coin_value_list:
        return 1

    # Otherwise let's progress to the base case: looking to reduce the change
    # We will make recursive valls for each different coin value, less than the amount we are trying to make
    else:
        # Go through a smaller set of our coin list that has values less than change
        for coin_value in [coin for coin in coin_value_list if coin <= change]:
            
            # We will check through using our greedy method, check
            # i.e. go through each set of coin values in the smaller list and check those recursively
            num_coins = 1 + make_change_1(coin_value_list, change - coin_value)
            
            # For the current iteration of the coin value, if the method returns a min amount of coins less than our current min_coins counter... 
            if num_coins < min_coins:

                # set it as the min coins
                min_coins = num_coins
            return min_coins
    
print(make_change_1([1,5,10,25], 63))

"""
The above weould be very inefficient as we would often be recalcualting 
    > The below introduces caching or memorisation, cuts 67716925 calls to 221
"""

# To keep track of already calculated min coins for a certain amount of change, pass in known_results dictionary
def make_change_2(coin_value_list, change, known_results):
    min_coins = change

    # If we have a change amount that is in the change list, return 1 and update the dictionary
    if change in coin_value_list:
        known_results[change] = 1
        return 1

    # else the known_results[change] already has a value, use that instead
    elif known_results[change] > 0:
        return known_results[change]

    # Otherwise we can begin our journey into recursion calling
    else:

        # We will check through each possible branch coin value that is less than or equal to the change amount i.e. check recursion for 1, 5, 10, 25
        for coin_value in [coin for coin in coin_value_list if coin <= change]:

            # But this time making sure to pass in known results
            num_coins = 1 + make_change_1(coin_value_list, change - coin_value, known_results)

            # keeping updating min coins should we find amin value
            if num_coins < min_coins:
                min_coins = num_coins
            
            # Update the known results so any subsequent calls know this;
            known_results[change] = min_coins

    return min_coins

"""
Dynamic programming however
    > Would start at 1 cent and systematicalaly work up to the amount of change we require
    > This would ensure that at each step of the algorithm we already know the min number of coins to make change for a smaller amount
"""

# Will need to pass in a dictionary to count the min_coins
def make_change_3(coin_value_list, change, min_coins):
    
    # Go through each possible smaller value
    for cents in range(change+1):

        # Initialise a counter fo the given cents amount
        coin_count_min = cents

        # Go through all possible coin values that are less than the cents amount
        for coin_amount in [coin_value for coin_value in coin_value_list if coin_value <= cents]:
            
            # Check the dictionary for the smaller value after subtracting the cooin amount
            # that value we retrieved + 1 will be the min coins requires for the current coin amount
            # if that is less than the coint count, update the coin_count_min
            if min_coins[cents - coin_amount] + 1 < coin_count_min:
                coin_count_min = min_coins[cents - coin_amount] + 1

        # THen update the dictionary
        min_coins[cents] = coin_count_min

    # We shoudl have now populated our dictionary all the way up to change, can return it now
    return min_coins[change]


"""
If we keep track of the last coin added to the table 
"""
# We can extend this to account for the coins used
def make_change_4(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count_min = cents

        # init a new variable called new coun
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count_min:
                
                # If we've identified a smaller number of coins based on the 'j' coin amount, set it as the min as well as the new coin
                coin_count_min = min_coins[cents - j] + 1
                new_coin = j

        # For the current amount of cents, we will have two dictionaries,
        # One dictionary that tells use the min amount of coins needed as change
        # The other dictionary telling us what coin that was used as part of the change to get the min amount of coins
            # e.g. we check for 11 - 1 (1 coin), 11 - 5 (2 coins), 11 - 10 (1 coin). we will keep track of the 1c for 11, and we can go to 10 to realise we return 10c    
        min_coins[cents] = coin_count_min
        coins_used[cents] = new_coin
    return min_coins[change]

# given a coins used table and a change amount, goes through the table to print out couns
def print_coins(coins_used, change):

    coin = change
    
    # Start a while loop and keep reducing "coin until zero"
    while coin > 0:
        
        # We will access the coins used table to find a coin to reduce to the change or "coin by"
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    
    print()

# notes that lists are just dictionary {1: item 1. 2: item 2.}
def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amnt + 1)
    coin_count = [0] * (amnt + 1)

    print(
       "Making change for {} requires the following {} coins: ".format(
             amnt, make_change_4(clist, amnt, coin_count, coins_used)
       ),
       end="",
    )
    print_coins(coins_used, amnt)
    print("The used list is as follows:")
    print(coins_used)


main()




    