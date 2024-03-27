# n = 10

# Output 0 1 1 2 3 5 8 13 21 34

## range : print 10 numbers

# def fibonacci(n):
#     fibs = [0,1]
#     for _ in range(n):
#         fibs.append(fibs[-1] + fibs[-2])
#     print(fibs)
# fibonacci(10)


## sum : print upto 10 means till it reaches 10

def fibonacci(n):
    fibs = [0,1]
    while fibs[-1] + fibs[-2] <=n:
        fibs.append(fibs[-1] + fibs[-2])
    print(fibs)
fibonacci(10)





