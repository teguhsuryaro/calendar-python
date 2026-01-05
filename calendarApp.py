import tools

def main():
    while True:
        tools.menu()
        menu = int(input("Select Menu [1,2,3,4] : "))
        print("-------------------------")
        if menu == 1:
            tools.fullCalendar()
        elif menu == 2:
            tools.onlyMonth()
        elif menu == 3:
            tools.countDays()
        elif menu == 4:
            print("Program is complete..")
            break
        else:
            print("Select the menu correctly !!")

if __name__ == "__main__":
    main()