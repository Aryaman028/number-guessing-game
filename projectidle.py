print("||  APPLICATION FOR FINDING NUMBER OF DAYS HE SURVIVED  ||")
print()

dob = input("DATE OF BIRTH(DD/MM/YYYY)--> ")
c_date = input("CURRENT DATE(DD/MM/YYYY)--> ")
print()
print()
print("<--OUTPUT-->")
print("<--DATE OF BIRTH OF USER-->")
print(dob)
print("<--CURRENT DATE-->")
print(c_date)

y1 = int(dob[-4:])
y2 = int(c_date[-4:])
days = 0
for i in range(y1+1,y2):
    if i % 4 == 0:
        days += 366
    elif i % 4 != 0:
        days += 365
print(days)
month1 =  12 - int(dob[3:5])
month2 = int(c_date[3:5])-1
days = days + (month1 +month2)*30
d1 = 30 - int(dob[:2])
d2 = int(c_date[:2])
days = days + (d1 + d2)
print("<--Number of days he survived -->" )
print(days)
