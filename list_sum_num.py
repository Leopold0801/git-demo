from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)

L=[3,5,7,9]
print(prod(L))
