def f(S):
    if S == 'dreamer' or S == 'eraser' or S == 'dream' or S == 'erase':
        # print('true')
        return True
    # print('next?')
    if len(S) > 7:
        if S.endswith('dreamer'):
            # print(S, S[:-7], S[-7:])
            return f(S[:-7])
    if len(S) > 6:
        if S.endswith('eraser'):
            # print(S, S[:-6], S[-6:])
            return f(S[:-6])
    if len(S) > 5:
        if S.endswith('dream') or S.endswith('erase'):
            # print(S, S[:-5], S[-5:])
            return f(S[:-5])
    # print('false')
    return False

def main():
    S = input()
    if f(S):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
