# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = list()
for i in range(n):
    arr.append(input())
for string in arr:
    even_char = "".join([ch for ch in string[::2]])
    odd_char = "".join([ch for ch in string[1::2]])
    print(even_char, odd_char) 
    