for i in range(1, int(input())):
    print("FizzBuzz|||Fizz||Buzz|Fizz|||Fizz|Buzz||Fizz||".split("|")[i%15] or i)
