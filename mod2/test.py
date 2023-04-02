def primes_list_buggy(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    primes = []
    # i create this dict for keeping track of the number of times a number is not divisible by any of the primes
    checkLength = {"true": 0}
    if n >= 2:
        primes.append(2)
    # go through each elem of primes list
    for i in range(2, n + 1, 1):
        # go through each of 2...n
        print("i: ", i)
        for j in range(len(primes)):
            print(j, primes[j])
            # check if not divisible by elem of list
            if i % primes[j] != 0:
                checkLength["true"] += 1
                if checkLength["true"] == len(primes):
                    primes.append(i)
                    checkLength["true"] = 0
            elif i % primes[j] == 0:
                break
    return primes


# for a number to be prime, it is only divisible by 1 and itself
# so n % primes[j] != 0 means that n is not divisible by any of the primes, so it is prime
# likewise, as long as n % primes[j] == 0, n is not prime, so we can break out of the loop and move on to the next number

print(primes_list_buggy(2))
print(primes_list_buggy(15))

def primes_list(n):
    """
    input: n an integer > 1
    returns: list of all the primes up to and including n
    """
    # initialize primes list
    primes = [2]
    # go through each of 3...n
    for j in range(3,n+1):
        is_div = False
        # go through each elem of primes list
        for p in primes:
            if j%p == 0:
                is_div = True
        if not is_div:
            primes.append(j)
    return primes

print(primes_list(2) )               
print(primes_list(15)  )      