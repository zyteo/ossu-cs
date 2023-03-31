def primes_list_buggy(n):
   """
   input: n an integer > 1
   returns: list of all the primes up to and including n
   """
   # initialize primes list
   primes = []
   if n >= 2:
       primes.append(2)
   # go through each elem of primes list
   for i in range(2,n+1,1):
       # go through each of 2...n
       print("i: ", i)
       for j in range(len(primes)):
           print(j,primes[j])
           # check if not divisible by elem of list
           if i % primes[j] != 0:
                print(primes)
                
                # need to adjust this line
                primes.append(i)
           elif i % primes[j] == 0:
        
                break
   return primes
#
#for a number to be prime, it is only divisible by 1 and itself
# so n % primes[j] != 0 means that n is not divisible by any of the primes, so it is prime
# likewise, as long as n % primes[j] == 0, n is not prime, so we can break out of the loop and move on to the next number

## FIXES: --------------------------
## division by zero -> iterate through elems not indices

## forgot to return 
## infinite loop -> append j not i
##               -> list is getting modified as iterating over it!
##   
## n = 4 adds 4 -> need way to stop going once found a divisible num
##              -> use a flag
## --------------------------
print(primes_list_buggy(7))