from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10+y
    def en(x,y):
        return x*0.1+y
    def char2num(s):
        digits  ={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9 }
        return digits[s]

    i = s.index('.')
    zs = s[:i]
    xs = s[:i:-1]
    return reduce(fn,map(char2num,zs))+reduce(en,map(char2num,xs))*0.1
L='123.456'
print(str2float(L))
