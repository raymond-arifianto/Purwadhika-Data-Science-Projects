#adds tab and adjust based on requested size
def add_tab(msg, tab_size):                 #(message to print, total tab size wanted)
    str_msg = str(msg)                      #change into str to enable int to concatenate with str
    tab_qty = tab_size - len(str_msg)//8    #find how many tabs needed to reach size
    if tab_qty >= 0:
        for i in range(tab_qty):
            str_msg += '\t'
    return str_msg

#Hotel Rooms list
rooms = [ 
{
'Room'      : '01',
'Type'      : 'Standard',
'Status'    : 'Occupied',
'Guest'     : {
    'Name'          : 'Raymond Arifianto',
    'Origin'        : 'Indonesia',
    'Phone No.'     : '081284006098',
    'Email'         : 'raymond.arifianto11@gmail.com',
    'Marital Status': 'Unmarried'
    },
'Guest Qty.': 2,
'Check-out' : '22/05/2023' 
},
{
'Room'      : '02',
'Type'      : 'Standard',
'Status'    : 'Out of Service',
'Guest'     :{
    'Name'          : '-',
    'Origin'        : '-',
    'Phone No.'     : '-',
    'Email'         : '-',
    'Marital Status': '-'
    },
'Guest Qty.': 0,
'Check-out' : '-' 
},
{
'Room'      : '03',
'Type'      : 'Standard',
'Status'    : 'Vacant',
'Guest'     :{
    'Name'          : '-',
    'Origin'        : '-',
    'Phone No.'     : '-',
    'Email'         : '-',
    'Marital Status': '-'
    },
'Guest Qty.': 0,
'Check-out' : '-' 
},
{
'Room'      : '04',
'Type'      : 'Standard',
'Status'    : 'Vacant',
'Guest'     :{
    'Name'          : '-',
    'Origin'        : '-',
    'Phone No.'     : '-',
    'Email'         : '-',
    'Marital Status': '-'
    },
'Guest Qty.': 0,
'Check-out' : '-' 
},
{
'Room'      : '05',
'Type'      : 'Standard',
'Status'    : 'Vacant',
'Guest'     :{
    'Name'          : '-',
    'Origin'        : '-',
    'Phone No.'     : '-',
    'Email'         : '-',
    'Marital Status': '-'
    },
'Guest Qty.': 0,
'Check-out' : '-' 
},
{
'Room'      : '06',
'Type'      : 'Superior',
'Status'    : 'Occupied',
'Guest'     :{
    'Name'          : 'Gabriela Valerie',
    'Origin'        : 'Singapore',
    'Phone No.'     : '081298557638',
    'Email'         : 'garbiela.valerie@gmail.com',
    'Marital Status': 'Married'
    },
'Guest Qty.': 1,
'Check-out' : '30/05/2023' 
},
{
'Room'      : '07',
'Type'      : 'Superior',
'Status'    : 'Vacant',
'Guest'     :{
    'Name'          : '-',
    'Origin'        : '-',
    'Phone No.'     : '-',
    'Email'         : '-',
    'Marital Status': '-'
    },
'Guest Qty.': 0,
'Check-out' : '-' 
},
{
'Room'      : '08',
'Type'      : 'Superior',
'Status'    : 'Vacant',
'Guest'     :{
    'Name'          : '-',
    'Origin'        : '-',
    'Phone No.'     : '-',
    'Email'         : '-',
    'Marital Status': '-'
    },
'Guest Qty.': 0,
'Check-out' : '-' 
},
{
'Room'      : '09',
'Type'      : 'Deluxe',
'Status'    : 'Vacant',
'Guest'     :{
    'Name'          : '-',
    'Origin'        : '-',
    'Phone No.'     : '-',
    'Email'         : '-',
    'Marital Status': '-'
    },
'Guest Qty.': 0,
'Check-out' : '-' 
},
{
'Room'      : '10',
'Type'      : 'Deluxe',
'Status'    : 'Vacant',
'Guest'     :{
    'Name'          : '-',
    'Origin'        : '-',
    'Phone No.'     : '-',
    'Email'         : '-',
    'Marital Status': '-'
    },
'Guest Qty.': 0,
'Check-out' : '-' 
}
]

#Display Program Menu Options:

def main_menu():            #Main Menu - Hotel Room Management System (RMS)
    while True:
        print("\nWelcome to Horizon Hotel Room Management System (RMS)")
        print("List of Menu:")
        print("1. Show Room Status")
        print("2. Register New Room to RMS")
        print("3. Update Room Status")
        print("4. Remove Room from RMS")
        print("5. Exit Program")
        menu_no = input('Please input which Menu number you want to run: ')
        if menu_no == '1':
            read_menu()
        elif menu_no == '2':
            create_menu()
        elif menu_no == '3':
            update_menu()
        elif menu_no == '4':
            delete_menu()
        elif menu_no == '5':
            print("Closing RMS.. See you!")
            return
        else:
            print("Please enter a valid number")

def read_menu():            #[A] Read Menu - Check all room status & Guest info
    hotel_status()
    while True:
        print("Please choose which type of data you would like to see:")
        print("1. Show all Room Status")
        print("2. Show Guest Info of a specific Room")
        print("3. Return to Main Menu")
        menu_no = input('Please input which Menu number you want to run: ')
        if menu_no == '1':
            room_status()   #function to print all room status (except guest info other than name)
        elif menu_no == '2':
            if guest_qty > 0:
                guest_list()
                show_guest_info(input("Please input the room no. of the guest: ").capitalize())
            else:
                print("\nThere is no guest in this hotel\n")       
        elif menu_no == '3':
            return
        else:
            print("Please enter a valid number\n")

def hotel_status():                 #[A.a] Show General Hotel Status
    global guest_qty
    guest_qty = 0
    v_std = 0
    v_spr = 0
    v_dlx = 0
    o_std = 0
    o_spr = 0
    o_dlx = 0
    oos_std = 0
    oos_spr = 0
    oos_dlx = 0
    for i in range(len(rooms)):
        guest_qty += rooms[i]["Guest Qty."]
        if rooms[i]["Status"] == "Vacant":
            if rooms[i]["Type"] == "Standard":
                v_std += 1
            elif rooms[i]["Type"] == "Superior":
                v_spr += 1
            elif rooms[i]["Type"] == "Deluxe":
                v_dlx += 1
        elif rooms[i]["Status"] == "Occupied":
            if rooms[i]["Type"] == "Standard":
                o_std += 1
            elif rooms[i]["Type"] == "Superior":
                o_spr += 1
            elif rooms[i]["Type"] == "Deluxe":
                o_dlx += 1
        elif rooms[i]["Status"] == "Out of Service":
            if rooms[i]["Type"] == "Standard":
                oos_std += 1
            elif rooms[i]["Type"] == "Superior":
                oos_spr += 1
            elif rooms[i]["Type"] == "Deluxe":
                oos_dlx += 1     
    print("\nHotel Status")
    print(f"No. of Guests: {guest_qty}")
    print("Status\t\t| Standard\t| Superior\t| Deluxe")
    print(f"Vacant\t\t| {v_std}\t\t| {v_spr}\t\t| {v_dlx}")
    print(f"Occupied\t| {o_std}\t\t| {o_spr}\t\t| {o_dlx}")
    print(f"Out of Service\t| {oos_std}\t\t| {oos_spr}\t\t| {oos_dlx}\n")
    
def room_status():                  #[A.1] Show all room status/data (except detail guest info)
    print("\nCurrent Room Status:")
    print(f"{add_tab('Room No.',1)+add_tab('| Room Type',2)+add_tab('| Status',2)+add_tab('| Guest Name',3)+add_tab('| Guest Qty.',2)}| Check-Out Date")
    for i in range(len(rooms)):
        print(f"{add_tab(rooms[i]['Room'],1)+add_tab('| ' + rooms[i]['Type'],2)+add_tab('| ' + rooms[i]['Status'],2)+add_tab('| ' + rooms[i]['Guest']['Name'],3)+add_tab('| ' + str(rooms[i]['Guest Qty.']),2)+'| ' + rooms[i]['Check-out']}")
    print("\n")
            
def guest_list():                   #[A.2.a] Only show rooms with guests (Occupied)
    print("\nCurrent Rooms with guests:")
    print(f"{add_tab('Room No.',1)+add_tab('| ' + 'Guest Name',3)+add_tab('| ' + 'Guest Qty.',2)}| Check-Out Date")
    for i in range(len(rooms)):
        if rooms[i]['Status'] == 'Occupied':
            occupied_room = True
            print(f"{add_tab(rooms[i]['Room'],1)+add_tab('| ' + rooms[i]['Guest']['Name'],3)+add_tab('| ' + str(rooms[i]['Guest Qty.']),2)+ '| ' + rooms[i]['Check-out']}")
    print("\n")  
    
def show_guest_info(room_no):       #[A.2.b] Show detailed guest info of the requested room
    for i in range(len(rooms)):
        if rooms[i]["Status"] != "Occupied":
            continue
        elif room_no == rooms[i]["Room"]:
            print(f"Room No. {room_no}:")
            print(f"Guest Name: {rooms[i]['Guest']['Name']}")
            print(f"Country of Origin: {rooms[i]['Guest']['Origin']}")
            print(f"Phone No.: {rooms[i]['Guest']['Phone No.']}")
            print(f"Email: {rooms[i]['Guest']['Email']}")
            print(f"Marital Status: {rooms[i]['Guest']['Marital Status']}")
            print(f"No. of guests: {rooms[i]['Guest Qty.']}\n")
            return
    print("Sorry, the room number does not exist.")

def create_menu():          #[B] Create Menu - Add new room
    while True:
        hotel_status()
        print("1. Add New Room")
        print("2. Return to Main Menu")
        menu_no = input('Please input which Menu number you want to run: ')
        if menu_no == '1':
            room_no = check_room_no(input("Please input the new room number: ").capitalize())
            if room_no == False:
                continue
            else:
                room_type = add_room_type()
                rooms.append({
                    'Room'      : room_no,
                    'Type'      : room_type,
                    'Status'    : 'Vacant',
                    'Guest'     :{
                        'Name'          : '-',
                        'Origin'        : '-',
                        'Phone No.'     : '-',
                        'Email'         : '-',
                        'Marital Status': '-'
                        },
                    'Guest Qty.': 0,
                    'Check-out' : '-' 
                })
                print("Room has been added!\n")
                room_status()
        elif menu_no == '2':
            return
        else:
            print("Please enter a valid number\n")

def check_room_no(room):            #[B.1.a] Check if room exist and return False if it does  
    while True:
        for i in range(len(rooms)):
            if room == rooms[i]["Room"]:
                print("The room name has already exist.\n")
                return False
        return room

def add_room_type():                #[B.1.b] Choose room Type
    print("Please Choose Room Type: ")
    print("1. Standard")
    print("2. Superior")
    print("3. Deluxe")
    while True:
        type_no = input('Please input a Type no.: ')
        if type_no == '1':
            return "Standard"
        elif type_no == '2':
            return "Superior"
        elif type_no == '3':
            return "Deluxe"
        else:
            print("Please input a valid number")

def update_menu():          #[C] Update Menu - Change Room Status & Guest info
    global rooms
    while True:
        hotel_status()
        print("List of Update menu:")
        print("1. Update Room Status")
        print("2. Update Guest Info")
        print("3. Return to Main Menu")
        menu_no = input("Please input which Menu number you want to run: ")
        if menu_no == '1':
            update_room()
        elif menu_no == '2':
            guest_list()
            room_avail = False
            room_no = input("Please enter the number of the Room you want to update: ").capitalize()
            for i in rooms:
                if i["Room"] == room_no:
                    room_avail = True
                    index = rooms.index(i)
            if room_avail == False:
                print("sorry, the room does not exist\n")
            else:
                update_guest(index, True)
        elif menu_no == '3':
            return
        else:
            print("please enter a valid number")

def update_room():                  #[C.1] Handles Room Status Update 
    global rooms
    room_status()
    room_avail = False
    room_no = input("Please enter the number of the Room you want to update: ").capitalize()
    for i in rooms:
        if i["Room"] == room_no:
            room_avail = True
            index = rooms.index(i)
    if room_avail == False:
        print("sorry, the room does not exist\n")
    else:
        while True:
            print("V\t= Vacant")
            print("O\t= Occupied")
            print("OOS\t= Out of Service")
            print("C\t= Cancel the update")
            new_status = input(f"Please enter the status of Room {room_no} (V/O/OOS/C): ").upper()
            if new_status == "V":
                rooms[index]['Status'] = 'Vacant'
                update_guest(index,False)
                break
            elif new_status == "O":
                rooms[index]['Status'] = 'Occupied'
                update_guest(index,True)
                break
            elif new_status == "OOS":
                rooms[index]['Status'] = 'Out of Service'
                update_guest(index,False)
                break
            elif new_status == "C":
                break
            else:
                print("Sorry, but the status you entered is not valid.")     
            
def update_guest(index,fill):       #[C.2] Handles Guest Update needs (index of room, fill/erase)
    global rooms
    if fill == True:
        rooms[index]['Guest Qty.'] = int(input('Number of guest(s): '))             #NOTE: I know how to create a error handle so if input is not int, then we request them to fill in again instead of crashing using TRY, but i believe it's not part of this module so we aren't allowed to use it
        rooms[index]['Guest']['Name'] = input("Booking Name: ")
        rooms[index]['Guest']['Origin'] = input("Origin: ")
        rooms[index]['Guest']['Phone No.'] = input("Phone No.: ")
        rooms[index]['Guest']['Email'] = input("Email: ")
        rooms[index]['Guest']['Marital Status'] = input("Marital Status: ")
        co_day = input("Please enter Check-out day (DD): ")
        co_month = input("Please enter Check-out month (MM): ")
        co_year = input("Please enter Check-out year (YYYY): ")
        rooms[index]['Check-out'] = f"{co_day}/{co_month}/{co_year}"
    else:
        rooms[index]['Guest Qty.'] = 0
        rooms[index]['Guest']['Name'] = '-'
        rooms[index]['Guest']['Origin'] = '-'
        rooms[index]['Guest']['Phone No.'] = '-'
        rooms[index]['Guest']['Email'] = '-'
        rooms[index]['Guest']['Marital Status'] = '-'
        rooms[index]['Check-out'] = '-'
    print("Room Status is updated!")

def delete_menu():          #[D] Delete Menu - Delete a room or All rooms
    global rooms
    while True:
        room_status()
        print('List of menu:')
        print('1. Remove a specific room from database')
        print('2. Remove ALL rooms from database')
        print('3. Return to Main Menu')
        menu_no = input("Please input which Menu number you want to run: ")
        if menu_no == '1':
            room_avail = False
            room_no = input("Please enter the number of the Room you want to remove (type 'Cancel' to cancel): ").capitalize()
            if room_no != 'Cancel':
                for i in rooms:
                    if i["Room"] == room_no:
                        room_avail = True
                        index = rooms.index(i)
                if room_avail == False:
                    print("sorry, the room does not exist\n")
                else:
                    while True:
                        confirm_del = input(f"Are you sure you want to permanently remove Room {room_no}? (y/n): ").lower()
                        if confirm_del == "y":
                            del rooms[index]
                            print(f"Room {room_no} has been successfully removed!")
                            break
                        elif confirm_del == "n":
                            print("Request cancelled!")
                            break
                        else:
                            print("Please enter a valid option.")
        elif menu_no == '2':
            print("This option will delete ALL rooms from the RMS database.")
            confirm_del = input("Are you sure you would like to continue? (Type in YES to continue, or anything else to cancel): ")
            if confirm_del == 'YES':
                rooms = []
                print("All rooms has been succesfully removed from the database!")
            else:
                print('Wrong input received. Request cancelled!')
        elif menu_no == '3':
            return
        else:
            print("Please enter a valid number\n")

main_menu()
