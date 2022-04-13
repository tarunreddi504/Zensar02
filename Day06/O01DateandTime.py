
from datetime import  datetime
import dateutils

dt = datetime.now()
print(f"dt :{dt}")

print("-" * 40)
print("Day :", dt.strftime("%a"))
print("Day :", dt.strftime("%A"))

print("-" * 40)
print("Month :", dt.strftime("%b"))
print("Month :", dt.strftime("%B"))

print("-" * 40)
print("Date :", dt.strftime("%d"))
print("Date :", dt.strftime("%D"))
print("Date :", dt.strftime("%x"))

print("-" * 40)
print("Year :", dt.strftime("%y"))
print("Year :", dt.strftime("%Y"))

print("-" * 40)
print("Time :", dt.strftime("%T"))
print("Time :", dt.strftime("%X"))

print("-" * 40)
dt1 = dt.strftime("%d-%m-%Y")
print(f"dt1 :{dt1}")
dt2 = dt.strftime("%d-%m-%y")
print(f"dt2 :{dt2}")
dt3 = dt.strftime("%d-%b-%Y")
print(f"dt3 :{dt3}")

print("-" * 40)
dt4 = "Wednesday, April 13, 2022"
print(f"dt4 :{dt4}")
print(type(dt4))

print("-" * 40)
dt5 = "Monday, January 13, 2021"
print(f"dt5 :{dt5}")
print(type(dt5))

print("-" * 40)
actdt1 = datetime.strptime(dt4, "%A, %B %d, %Y")
print(f"actdt1 :{actdt1}")
print(type(actdt1))

print("-" * 40)
actdt2 = datetime.strptime(dt5, "%A, %B %d, %Y")
print(f"actdt2 :{actdt2}")
print(type(actdt2))

print("-" * 40)
print(actdt1 - actdt2)

print("-" * 40)
print("Difference in Days :", dateutils.days(actdt1, actdt2))

print("-" * 40)
print("Difference in Weeks :", dateutils.weeks(actdt1, actdt2))

print("-" * 40)
print("Difference in Months :", dateutils.months(actdt1, actdt2))

print("-" * 40)
print("Difference in Years :", dateutils.years(actdt1, actdt2))
