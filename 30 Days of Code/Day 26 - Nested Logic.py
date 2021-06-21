# Enter your code here. Read input from STDIN. Print output to STDOUT
ret_date, ret_month, ret_year = map(int, input().split())
due_date, due_month, due_year = map(int, input().split())

fine = 0

if ret_year<due_year:
    fine=0
elif ret_year==due_year:
    if ret_month<due_month:
        fine=0
    elif ret_month==due_month:
        if ret_date<=due_date:
            fine = 0
        else:
            fine=15*(ret_date-due_date)
    else:
        fine = 500*(ret_month-due_month)
else:
    fine = 10000
print(fine)
        
            