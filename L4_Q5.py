from datetime import date

date1 = date(2013,6,7)
date2 = date(2022,6,7)

days = date2 - date1
print("Days between given dates are : ",(days).days)
