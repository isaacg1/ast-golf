# 2 2    3     1  1                                          9
for i in range(1, 101):
#   3      2   2 2 1  2 1      2  2   2 2 1  2 1      2  2   29
    print((not i % 3) * "Fizz" + (not i % 5) * "Buzz" or i)  
# 39
