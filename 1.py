with open('ex1.txt', 'r', encoding='utf-8') as f:
    a = f.readlines()
    a = list(map(lambda x: x.rstrip(), a))
b = []
for i in range(9,12,1):
    l = sorted(list(filter(lambda x: f'{i}' == x.split()[2], a)), key=lambda x: int(x.split()[3]))
    b.append(sum(map(int, [x.split()[3] for x in l]))/len(l))
print(*b)

