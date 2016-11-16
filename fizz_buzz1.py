for i in range(1, 101):    # 5
    if not i % 15:         # 5
        print("FizzBuzz")  # 2
    elif not i % 3:        # 5
        print("Fizz")      # 2
    elif not i % 5:        # 5
        print("Buzz")      # 2
    else:                  # 1
        print(i)           # 2
