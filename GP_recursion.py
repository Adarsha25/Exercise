# given the first and second term of the GP, find the nth term

a= int(input('Give the first term of the GP: '))
b= int(input('Give the second term of the GP: '))
N= int(input('Give the n value of the GP: '))

r = b/a
s = a*r**(N-1)
print()