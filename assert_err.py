def foo(s):
    n = int(s)
    assert n!=0,'n is zero!' #assert条件若为假，则相当于pass
    return 10/n

def main():
    foo('0')

main()