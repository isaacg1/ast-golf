for i in range(1, int(input())):
    print((not i % 3) * "Fizz" + (not i % 5) * "Buzz" or i)  
