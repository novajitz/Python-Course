import datetime

currentDate = datetime.date.today()

print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

print(currentDate.strftime('%d %b %Y'))

print(currentDate.strftime('Please attend our event on %A, %B, %d in the year %Y'))

birthday = input("Enter birthday (dd/mm/yyyy) :")
birthdate = datetime.datetime.strptime(birthday,"%d/%m/%Y")
print (birthdate)



