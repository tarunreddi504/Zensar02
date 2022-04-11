temp = [20, 30, 25, 32, 38]

print(f"temp :{temp}")
lst = list(map(lambda x: x / 1.8 + 32, temp))

print(f"lst :{lst}")
print("-" * 40)

expenses = [12,30,25,38]
res = list(map(lambda x : x * 75.8 ,expenses))
print(res)

print("-" * 40)
months = ['dec', 'aug', 'oct', 'nov', 'sep', 'jan', 'apr', 'mar', 'jul', 'feb', 'jun', 'may']

print(f"months :{months}")

from calendar import month_name
def srt_month(name):
    l = []
    for i in list(month_name):
        l.append(i[0:3].lower())
    return l.index(name)

srtMnts = sorted(months, key=srt_month)
print(f"srtMnts :{srtMnts}")


# convert srt_month into a lambda function



"""
problem
-------
months = ['dec', 'aug', 'oct', 'nov', 'sep', 'jan', 'apr', 'mar', 'jul', 'feb', 'jun', 'may']
sort it by months in the calendar

"""