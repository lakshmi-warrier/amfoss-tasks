#no matter what the answer is always 1 or 2
length = int(input())
string = input()
num_0 = string.count("0")
num_1 = string.count("1")
if num_1 == num_0:
    print(2)
else:
    print(1)
