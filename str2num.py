from functools import reduce
def fn(x,y):
    return 10*x+y

def char2num(s):
    digits  ={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9 }
    return digits[s]

res = reduce(fn,map(char2num,'2468'[::-1]))
print(res)
