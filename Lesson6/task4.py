'''
Сделайте словарь дней недели {1: "Monday", 2:... } в общем словарь.
И потом "переверните" чтоб было {"Monday": 1, ...

'''


days_of_week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

days_of_week = {value: key for key, value in days_of_week.items()}
print(days_of_week)