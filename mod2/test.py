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
        while ans**2 < abs_x:
            ans = ans + 1
        if ans**2 == abs_x:
            print("Square root of", x, "is", ans, "i")
        else:  
            # for example, if x is -5. √-5 = √5 * √-1, so answer is √5i, since √-1 = i
            print("Square root of", x, "is", ans, "√", abs_x, "i")