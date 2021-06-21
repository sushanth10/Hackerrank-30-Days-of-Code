# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = map(int, input().split())
arr = sorted(arr)
count_dict = dict()
max_count = 1
for i in arr:
    if i not in count_dict:
        count_dict[i] = 1
    else:
        count_dict[i] += 1

mean = sum(arr)/n
median = arr[n//2]
mode = arr[0]
if n%2==0:
    median = arr[n//2]+arr[n//2-1]
    median /= 2

for i in count_dict.keys():
    if count_dict[i]>max_count:
        max_count = count_dict[i]
        mode = i 

print(f"{round(mean,1)}\n{round(median,1)}\n{mode}")


