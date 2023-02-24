###################
# EXAMPLE: while loops 
# Try expanding this code to show a sad face if you go right
# twice and flip the table any more times than that. 
# Hint: use a counter
###################
counter = 0
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
n = n.lower()
while n == "right":
    if counter < 1:
        counter += 1
        n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
        n = n.lower()
    elif counter == 1:
        counter += 1
        n = input("You are in the Lost Forest\n****************\n******       ***\n  :( \n****************\n****************\nGo left or right? ")
        n = n.lower()
    elif counter > 1:
        n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
        n = n.lower()
print("\nYou got out of the Lost Forest!\n\o/")