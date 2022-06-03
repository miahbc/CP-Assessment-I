# Write your solution here!
from unittest import TestSuite


def coin_change(item_cost, optimal_change):
    coins = {
        'hundred': 100,
        'fifty': 50,
        'twenty': 20,
        'ten': 10,
        'five': 5,
        'one': 1,
        'quarter': .25,
        'dime': .10,
        'nickel': .05,
        'penny': .01
    }

    cost = 0 + item_cost
    print(cost)
    for x in coins:
        coin_value = coins[x]
        coin_name = x
        # print(coin_name, coin_value)



# TESTS 
print(coin_change(62.13, 100))
print(coin_change(31.51, 50)) 
print(coin_change(1,5)) 
print(coin_change(4,5)) 


# print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

# print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")