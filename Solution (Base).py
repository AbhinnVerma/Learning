# Program using Dict to input date & check whether valid or not

m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:30, 9:31, 10:30, 11:31, 12:30}
idate = input('\nEnter the date in d/m/y : ')
idate = idate.split('/')
idate = [int(ele) for ele in idate] 
idate = tuple(idate)
        
# value assignment
if len(idate)>3:
    print('---------Invalid Input--------')
date,month,year = idate

# Rules
if year<100:
    if year % 4 == 0 and year % 100 != 0:
        mleap = {2:29}
        m.update(mleap)
    if date <= (m[month]):
        print('____________VALID date____________')
    else:
         print('____________INVALID date____________')
else:
        print('Invalid Format (use d/m/y) \n*Only double digit inputs supported')

