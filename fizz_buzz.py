for i in range(1, 101):    # 5
    if not i % 15:         # 5
        print("FizzBuzz")  # 2
    elif not i % 3:        # 5
        print("Fizz")      # 2
    elif not i % 5:        # 5
        print("Buzz")      # 2
    else:                  # 1
        print(i)           # 2
# 29

#for i in range(1, 101): # 5
#    s = ""              # 3
#    if not i % 3:       # 5
#        s += "Fizz"     # 3
#    if not i % 5:       # 5
#        s += "Buzz"     # 3
#    print(s or i)       # 4
## 28
#
#for i in range(1, 101):                                                           # 5
#    for divisor, output in zip([15, 3, 5, 1], ["FizzBuzz", "Fizz", "Buzz", i]):   # 14
#        if not i % divisor:                                                       # 5
#            print(output)                                                         # 2
#            break                                                                 # 1
## 27
#
#for i in range(1, 101):                                                                         # 5
#    print(["FizzBuzz", "Fizz", "Buzz", i][[i % divisor for divisor in [15, 3, 5, 1]].index(0)]) # 20
## 25
#
#for i in range(1, 101):                                      # 5
#    print((not i % 3) * "Fizz" + (not i % 5) * "Buzz" or i)  # 18
## 23
