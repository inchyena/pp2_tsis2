with open('test.txt', encoding='utf8') as f:
    x = [next(f) for i in range(int(input()))]
print(*x)