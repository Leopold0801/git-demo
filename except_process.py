from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        print('你输入的是浮点数，已经帮你修复了')
        return float(s)
        

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()