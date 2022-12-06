def fact(n):
    if n==0:
        return 1

    return n * fact(n-1)


print('Input the number to find the factorial')
n = int(input())
result = fact(n)
print(result)