# 2 2    3     1  1
for i in range(1, 101):
#   2   2      2 2         3   21   1  1  1   21           1       1       2
    for divisor, output in zip([15, 3, 5, 1], ["FizzBuzz", "Fizz", "Buzz", i]):
#       2  2   2 2 2
        if not i % divisor:
#           3     2
            print(output)
#           1
            break
