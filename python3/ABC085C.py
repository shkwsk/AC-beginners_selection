def main():
    N, Y = [int(x) for x in input().split()]
    tmp = 0
    x, y, z = 0, 0, 0
    for i in range(N):
        if tmp + 10000 <= Y:
            tmp += 10000
            x += 1
    print(tmp,x,y,z)
    for i in range(N - x):
        if tmp + 5000 <= Y:
            tmp += 5000
            y += 1
    print(tmp,x,y,z)
    for i in range(N - x - y):
        if tmp + 1000 <= Y:
            tmp += 1000
            z += 1
    print(tmp,x,y,z)
    if not tmp == Y:
        x, y, z = -1, -1, -1
    print(x,y,z)

if __name__ == '__main__':
    main()
