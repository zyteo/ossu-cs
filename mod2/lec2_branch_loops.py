##################
# EXAMPLE: strings 
##################
hi = "hello there"
name = "ana"
greet = hi + name  
print(greet)
greeting = hi + " " + name
print(greeting)
silly = hi + (" " + name)*3
print(silly)

###################
# EXAMPLE: output 
###################
x = 1
print(x)
x_str = str(x)
print("my fav number is", x, ".", "x=", x)
print("my fav number is", x_str + "." + "x=" + x_str)
print("my fav number is" + x_str + "." + "x=" + x_str)


###################
# EXAMPLE: input
###################
text = input("Type anything... ")
print(5*text)
num = int(input("Type a number... "))
print(5*num)


###################
# EXAMPLE: conditionals/branching 
###################
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
   print("x and y are equal")
   if y != 0:
       print("therefore, x / y is", x/y)
elif x < y:
   print("x is smaller")
elif x > y:
   print("y is smaller")
print("thanks!")

###################
# EXAMPLE: remainder 
###################
num = int(input("Enter a number: "))
if num % 2 == 0:
   print("number is even")
else:
   print("number is odd")

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


# alternative method
counter = -1
n = "right"
# set n to lower case

while n == "right":
    counter += 1
    print("You are in the Lost Forest")
    print("****************\n****************")

    if counter < 2:
        print(":)")
    elif counter == 2:
        print(":(")
    else:
        print("  (╯°□°）╯︵ ┻━┻")

    print("****************\n****************")

    n = input("Go left or right? ")
    n = n.lower()
          
print("\nYou got out of the Lost Forest!\n\o/")


n = 0
while n < 5:
   print(n)
   n = n+1


###################
# EXAMPLE: for loops
###################
for n in range(5):
   print(n)

mysum = 0
for i in range(10):
   mysum += i
print(mysum)

mysum = 0
for i in range(7, 10):
   mysum += i
print(mysum)

mysum = 0
for i in range(5, 11, 2):
   mysum += i
   if mysum == 5:
       break
       mysum += 1
print(mysum)



###################
# EXAMPLE: perfect squares
###################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
   neg_flag = True
while ans**2 < x:
   ans = ans + 1
if ans**2 == x:
   print("Square root of", x, "is", ans)
else:
   print(x, "is not a perfect square")
   if neg_flag:
       print("Just checking... did you mean", -x, "?")


###################
# TEST YOURSELF!
# Modify the perfect squares example to print 
# imaginary perfect sqrts if given a negative num.
###################
ans = 0
abs_x = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
   neg_flag = True
   abs_x = -x
while ans**2 < x:
   ans = ans + 1
if ans**2 == x:
   print("Square root of", x, "is", ans)
else:
   print(x, "is not a perfect square")
   if neg_flag:
      #  if x is not a perfect square, print imaginary perfect sqrts
      if ans**2 == abs_x:
         print("Square root of", x, "is", ans, "i")
      else:
         # for example, if x is -5. √-5 = √5 * √-1, so answer is √5i, since √-1 = i
         print("Square root of", x, "is", ans, "√", abs_x, "i")