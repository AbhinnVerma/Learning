# Program using Dict to input date & check whether valid or not

def method2():
    try:
        # Input
        
        idate = input('\nEnter the date in d/m/y : ')
        idate = idate.split('/')
        idate = [int(ele) for ele in idate] 
        idate = tuple(idate)
        
        # value assignment
        if len(idate)>3:
            print('---------Invalid Input--------')
            TryAgain()
        date,month,year = idate

        # Rules
        if year<100:
            if year % 4 == 0 and year % 100 != 0:
               mleap = {2:29}
               m.update(mleap)
            if date <= (m[month]):
                print('____________VALID date____________')
                TryAgain()
            else:
                print('____________INVALID date____________')
                TryAgain()
        else:
             print('Invalid Format (use d/m/y)')
             TryAgain()
    except (ValueError,KeyError):
        print('-------Invalid Input-------')
        TryAgain()

def TryAgain():
    TA = (input("\nTry Again? (y/n): "))
    TA.lower()
    if TA == ('y' or 'yes'):
        method2()
    elif TA == ('n' or 'no'):
        print('\nBYE!')
    else:
        print('---------Invalid Input--------')
        TryAgain()


m = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:30, 9:31, 10:30, 11:31, 12:30}
method2()

