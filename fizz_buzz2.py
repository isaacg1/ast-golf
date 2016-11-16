for i in range(1, 101):
    print(["FizzBuzz", "Fizz", "Buzz", i][[i % divisor for divisor in [15, 3, 5, 1]].index(0)])
