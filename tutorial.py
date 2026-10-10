n = int(input())
a = list(map(int, input().split()))

max_val = a[0]

for i in range(n):
    if a[i] > max_val:
        max_val = a[i]

print("Max value is", max_val)
