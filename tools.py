import calendar 

def menu():
     print('''
-------------------------
         MENU
-------------------------
1. Check 1 Calendar Year
2. Check 1 Calendar Month
3. Count Days in 1 Month
4. Exit
 -------------------------
              ''')

def fullCalendar():
    year = int(input("Enter Year : ")) 
    print(calendar.calendar(year, 2, 1, 8, 4))

def onlyMonth():
    month = int(input("Enter Month [1-12] : "))
    year = int(input("Enter Year : "))
    print("")
    print(calendar.month(year, month))

def countDays():
    month = int(input("Enter Month (1-12): "))
    year = int(input("Enter Year : "))
    
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    days = calendar.monthrange(year, month)[1]

    print("")
    print(f"The number of days in {month_names[month-1]} {year} is: {days}")