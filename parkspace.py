
def menu():
    print('=======Welcome=======\nMain Menu\n1:Reserve a parking space\n2:Check your parking\n')
    option = input('Enter the number of your option:')

    while True:
        if option.isnumeric()== False:
            print('\tThat is not an option.\n')
            option = input('\nEnter the number of your option:')
        else:
            option = int(option)
            break
    if option == 1:
        reserve()
    else:
        print('\tThat is not an option.\n')

    
def reserve():
    selected_day = None
    print('\n=======Parking Reservation=======\n~Select the day you wish to park from days 1-14 ~')
    
    while True:
        selected_day = input('Enter the number of your option:')
        if selected_day.isnumeric()== False:
            print('\tThat is not an option.\n')
        else:
            selected_day = int(selected_day)
            if selected_day>14 or selected_day<0:
                print('\tIncorrect input. Enter a day between 1-14.\n')
            else:
                #good option
                break
    occupied = len(parking_spaces[selected_day])
    if occupied<20:
        name = str(input('\nPlease insert your name:'))
        licenseplate = str(input('\nPlease insert your license plate:'))
        parking_spaces[selected_day].append({'name':name,'licenseplate':licenseplate})
        print('\n\n You have booked parking space number ' + str(occupied+1) + ' on day ' + str(selected_day))
        print('\n=======Booking complete=======')
    else:
        print('\n\tUnfortunately this parking space is not available.')

    #Verification. delete this after         
    #print('\n\n\nBookings:' + str(parking_spaces))

  
# Generates dictionary {1: [], 2: [], 3:[] . . . }
parking_spaces = dict()
for day in range(1,14):
    parking_spaces[day] = []

# time recorded at initial running of the program
from datetime import datetime, timedelta
start_time = datetime.now()
timeInTwoWeeks = datetime.now() + timedelta(weeks = 2)

#Function to reset parking spaces after 2 weeks
def reset_parking():
    for key in parking_spaces:
        parking_spaces[key] = []
        
        
while True:
    #Checks if 2 weeks have gone by before reseting the parking spaces
    if datetime.now() > timeInTwoWeeks:
        print('Parking data has been re-initialized')
        timeInTwoWeeks = datetime.now() + timedelta(minutes = 10)
        reset_parking()
    menu()
