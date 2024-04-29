N = 30
S = 0
count = 0

for i in range(1, N + 1):
    S += 1 / i
    count += 1

print("suma:", S)
print("quantity", count)