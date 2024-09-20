no_of_days = 36
yrs = no_of_days // 365
months = (no_of_days % 365)// 30
days = (no_of_days % 365) % 30
print(yrs, months, days)
print(f"yrs: {yrs}, months: {months}, days:{days}")