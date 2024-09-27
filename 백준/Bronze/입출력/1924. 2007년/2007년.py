m, d = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
days = ['SUN','MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT',]


def how_month():
    day = 0
    if m == 1:
        print(days[d % 7])
    else:
        for i in range(m - 1):
            day = day + month[i]
        
        print(days[(day + d) % 7])
        
how_month()