def _odd_iter():
    n=1 
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x: x%n!=0  #取余不为0即为不整除(为ture，留下)，否则舍去

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n=next(it)
        yield n
        it = filter((_not_divisible),it)

for i in primes():
    if i<1000:
        print(i)
    else:
        break