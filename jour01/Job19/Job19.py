x = 1

while x < 101:
    if x % 3 == 0 and x % 5 == 0: #si divisible par 3 & 5
        print("FizzBuzz")
    elif x % 3 == 0: #si divisible par 3
        print("Fizz")
    elif x % 5 == 0: #si divisible par 5
        print("Buzz")
    else:
        print(x)
    x = x + 1

