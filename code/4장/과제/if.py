## 4-33-2 if.py

month = int(input())
day = int(input())

if month == 8 and day == 15:
    print("광복절")
elif (month % 2 == 1 and day == 15) or (month % 2 == 0 and day == 16):
    print("그날")
else:
    print("평일")