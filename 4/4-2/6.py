month_num, month_day = map(int, input().split())

month_days_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month_day == 1:
    prev_day = month_days_num[month_num - 2]
    prev_month = month_num - 1
    next_day = 2
    next_month = month_num
elif month_day == month_days_num[month_num - 1]:
    prev_day = month_day - 1
    prev_month = month_num
    next_day = 1
    next_month = month_num + 1
else:
    prev_day = month_day - 1
    prev_month = month_num
    next_day = month_day + 1
    next_month = month_num
    
print(f"{int(prev_month):02}.{int(prev_day):02} {int(next_month):02}.{int(next_day):02}")