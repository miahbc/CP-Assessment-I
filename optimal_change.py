# Write your solution here!
from unittest import TestSuite
import math


def optimal_change(item_cost, amount_paid):
    coins = {
        '$100 bill': 100,
        '$50 bill': 50,
        '$20 bill': 20,
        '$10 bill': 10,
        '$5 bill': 5,
        '$1 bill': 1,
        'quarter': .25,
        'dime': .10,
        'nickel': .05,
        'penny': .01
    }
    change_arr = []
    answer = ""
    change_due = amount_paid % item_cost
    cost = 0 + item_cost
    # print(cost)
    if item_cost == 0:
        return (f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is ${amount_paid}")
    
    elif item_cost > amount_paid:
        return (f"Sorry, you don't have enough money.  This item costs ${item_cost} and you only gave ${amount_paid}")
    
    else:
        for x in coins:
            coin_value = coins[x]
            coin_name = x
        # print(coin_name, coin_value) # to verify dictionary order is correct
            even_div = change_due / coin_value
            # print(f"even_div {even_div} = change due {change_due} / bill {coin_value} ")
            # print(even_div)
            if even_div >= 1:
                ind_arr = []
                ind_arr.append(math.floor(even_div))
                ind_arr.append(coin_name)
                change_arr.append(ind_arr)
                change_due -= (math.floor(even_div) * coin_value)
            else:
                continue
        # identify need for plural vs singular    
        for y in change_arr:
            # print(y)
            if y[0] > 1:
                if y[1] != 'penny':
                    y[1] += 's'
                    # print(y)
                else:
                    y[1] = 'pennies'
                    # print(y)
            else:
                continue
        for x in change_arr:
            x[0] = str(x[0])
            # print(x[0])
            new = " ".join(x)
            if x != change_arr[(len(change_arr))-1]:
                answer += new
                answer += ", "
            else:
                answer += ("and " + new + ".")
                # answer += "."
            # print(answer)
        # answer = " ".join(change_arr)
        # print(answer)
    # return change_arr
        return(f"The optimal change for an item that costs ${item_cost} with an amount paid of ${amount_paid} is {answer}")






# TESTS 
print(optimal_change(62.13, 100)) #37.87
# print(optimal_change(31.51, 50)) 
# print(optimal_change(1,5)) 
# print(optimal_change(4,5)) 


# print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

# print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")