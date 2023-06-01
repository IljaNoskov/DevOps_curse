def calc_f(string):
    ans = eval(string)
    if isinstance(ans, tuple):
        print("use '.' with double and float number, not ','.")
        raise TypeError
    print(f'Ansver is {ans}')
    return ans


def calc_run():
    print("Enter 'end' to stop run")
    print("Enter your str to calculate:")
    st = input()
    n = 0
    while st != 'end':
        calc_f(st)
        print("Enter your str to calculate:")
        st = input()
        n += 1
    print(f'Thanks for use our calc. You had been use it {n} times')
    
