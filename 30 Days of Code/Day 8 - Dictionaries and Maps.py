# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
details = dict()
for i in range(n):
    k, val = input().split()
    details[k] = val

while True:
    try:
        query = input()
        if(query in details.keys()):
            print("{0}={1}".format(query, details[query]))
        else:
            print("Not found")
    except:
        break

