## 4-33-4 while.py

i = 1
sum = 0

while i < 51:
    if i % 2 == 0 and i % 3 != 0:
        sum += i
    i += 1

print(sum)