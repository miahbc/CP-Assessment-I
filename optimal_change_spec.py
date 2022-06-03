from optimal_change import optimal_change



# Write your tests here!
print(optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100.00 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print(optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50.00 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

print(optimal_change(1,5) == "The optimal change for an item that costs $1.00 with an amount paid of $5.00 is 4 $1 bills.")

print(optimal_change(4,5) == "The optimal change for an item that costs $4.00 with an amount paid of $5.00 is 1 $1 bill.")

print(optimal_change(100.00, 500) == "The optimal change for an item that costs $100.00 with an amount paid of $500.00 is 4 $100 bills.")

print(optimal_change(20.00,120) == "The optimal change for an item that costs $20.00 with an amount paid of $120.00 is 1 $100 bill.")

##EDGE CASES
print(optimal_change(5,5) == "Thanks for using exact change.  Have a great day!")

print(optimal_change(0.00,5.00) == "This item is on the house, keep your $5.00.")

print(optimal_change(5.00,4.00) == "Sorry, you don't have enough money.  This item costs $5.00 and you only gave $4.00.")

print(optimal_change(0.00,0.00) == "This item is on the house!")

print(optimal_change(.01,100.00) == "The optimal change for an item that costs $0.01 with an amount paid of $100.00 is 1 $50 bill, 2 $20 bills, 1 $5 bill, 4 $1 bills, 3 quarters, 2 dimes, and 4 pennies.")

