N = int(input())

numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

X = int(input())

if X in numbers:
    print(numbers.index(X) + 1)  
else:
    print("-1")
