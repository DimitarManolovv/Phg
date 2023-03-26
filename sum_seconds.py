first_seconds=int(input())
second_seconds=int(input())
third_seconds=int(input())

total_time=first_seconds+second_seconds+third_seconds
total_minutes=total_time//60
total_seconds=total_time%60

if total_seconds >= 10:
    print(f'{total_minutes}:{total_seconds}')
else:
    print(f'{total_minutes}:0{total_seconds}')