__author__ = "Travis Wilson"

'''
Items for Hire - Travis Wilson
https://github.com/Tukeyan/TravisWilsonCP1404Assignment-

The program will import the given data, and through the menu the user will select the actions taken to either,
hire, return, add and item to the store. When the user is finished, they will type Q for quit. After the user
 quits the information will be saved to the original cvs file, overwriting all information.'''

import csv #import the csv module

'''
open cvs file
read csv file

store data in list to be used later
display menu

get input from the user for menu
while input not Q
    if user input is A
        call add item function
    else if the input is H
        if there are still items to be hired
            call hire function
        otherwise display an error
    else if user input is R
        if there are no items for hire
            display error message
        otherwise
            call return function
    else if user input is L
        call list function
    else if user is Q
        display farewell

call write to file function
'''

def main():

    item_catalogue = loading_items()
    in_items, num_count = other_items(item_catalogue)

    user_input = 0 #Entering condition
    while user_input != "Q": #While the user doesn't enter Q
        print("",
num_count, '''items loaded from items.csv
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit''')

        user_input = str(input("Menu: ")).upper() #a string as an uppercase

        if user_input == "A": #If a is entered
            add_item(item_catalogue, in_items)

        elif user_input == "H": #If "H" is entered

            #For each item in in_items that returns a number below zero, x counter will count up once
            x = 0
            for items in in_items:
                if items < 0:
                    x += 1

            #If no items to hire are remaining, the user will get an error, otherwise run the hire_item function
            if x == len(in_items):
                print("No items left for hire, sorry. (Please return items to hire again.)")
                print("")
            elif x < len(in_items):
                hire_item(item_catalogue, in_items)
                item_hired = True
        #
        elif user_input == "R": #if r is entered after the user has hired an item

            #If an item in in_items return -2 (item number that has been hired), x counter will count up 1
            x = 0
            for items in in_items:
                if items == -2:
                    x += 1

            #if x = 0 (-2 is not in in_items) display error (item_hired wouldn't change to false), otherwise run return
            if x == 0:
                item_hired = False
                print("No items on hire.")
                print("")
            else:
                return_item(item_catalogue, in_items)

        elif user_input == "L": #if l is entered
            list_items(item_catalogue)

        elif user_input == "Q": #if the user enters q for quit, loop break
            print("Thank your for hiring with us!")
            print("")
        else:
            print("Invalid entry") #print error if the user doesn't enter the right value

    write_to_csv(item_catalogue) #this function writes the changes to the csv file allocated


def loading_items():
    item_hired = False #item_hired will force item_return to come up with an error, until an item is hired
    item_catalogue = [] #Create a list called item_catalogue

    #import the csv file (the default data or the updated data
    # item_data = open("items.csv", "r")
    item_data = open("itemsDefault.csv", "r")
    item_csv = csv.reader(item_data)

    num_count = -1 #Item counter to display how many items have been loaded in

    for item in item_csv: #Loop through each item of the file
            item_catalogue.append(item)#Add each item to a list
            num_count += 1 #add one for each item
            item.append(num_count)#Add the counter to each element of the list

    item_data.close()

    return item_catalogue

def other_items(item_catalogue):
    in_items = []
    item_data = open("itemsDefault.csv", "r")
    item_csv = csv.reader(item_data)
    num_count = -1

    for items in item_catalogue:
        in_items.append(items[4])
        print(in_items)

    item_data.close
    print("Welcome to items for hire by Travis Wilson")

    return in_items, num_count


'''
display header message
cycle through the items of the list
    if an item is out
        display with an asterisk
    otherwise
        display without an asterisk
'''
def list_items(item_catalogue):

    #display the entering message
    print("Items on file: ( * indicates item is hired out and not available )")

    #For items in item_catalogue, create a padding for formatting
    for items in item_catalogue:

        item = 15 - len(items[0])
        detail = 25 - len(items[1])
        pad = " "

        #if index 3 of the items equal out or userHired (items that are hired by the user in this session) display the items with an asterisk otherwise display without
        if items[3] == "out" or items[3] == "userHired":
            print(items[4], "-", items[0], (item*pad), "(" + items[1] + ")", (detail*pad), "= ", "$" + '{0:.2f}'.format(float(items[2])), "*")
        else:
            print(items[4], "-", items[0], (item*pad), "(" + items[1] + ")", (detail*pad), "= ", "$" + '{0:.2f}'.format(float(items[2])))

    input("Press Enter to continue.")
    print("")

    #Back to menu


'''
display header message
display items that aren't hired out
    if the item is in
        display item

get input from user
    loop while the input is invalid
        if the user input is in the list and isn't hired out
            change values to a hired item
        else if the input is not in the list
            display error message

return values
'''
def hire_item(item_catalogue, in_items):
    print("")
    print("Items available for hire: (Please enter the number of the item to be hired).")
    #Cycle through item_catalogue  and create the padding
    for items in item_catalogue:
        item = 12 - len(items[0])
        detail = 25 - len(items[1])
        pad = " "

        #if index 3 of the items is in and/or not userHired display those items
        if items[3] == "in" and items[3] != "userHired":
            print(items[4], "-", items[0], (item*pad), "(" + items[1] + ")", (detail*pad), "= ", "$" + '{0:.2f}'.format(float(items[2])) )

    #Cycle through the in_items list if the index is out, then replace the value in in_items with -1 (Item has been hired an another session
    #And if the index is userHired then the value must be -2 (The user has hired this item in this session)
    for items in in_items:
        if item_catalogue[items][3] == "out":
            in_items[items] = -1
        if item_catalogue[items][3] == "userHired":
            in_items[items] = -2

    user_input = -1 #forcing the loop

    #while the user inputs a number not within in_items (All items which has not been hired) or has entered a number of an item which is already out then
    #display an the error that the item is not available
    #If the input is within the list and doesn't equal -1 then the value (out or in) with be replaced with userHired, otherwise print an error
    while user_input not in in_items or user_input == -1:
        try:
            user_input = int(input("Number of item: "))
            if user_input == -1:
                print("Item not avaliable")
            elif user_input in in_items[:] and user_input != -1:
                item_catalogue[user_input][3] = "userHired"
                print(item_catalogue[user_input][0], "has been hired out for", "$" + '{0:.2f}'.format(float(item_catalogue[user_input][2])))
            else:
                print("Item not valid")
        except ValueError:
            print("Please enter a number, not a letter or symbol!")

    #The loop will run again to make sure all indexes inside in_items have been corrected
    for items in in_items:
        if item_catalogue[items][3] == "out":
            in_items[items] = -1
        if item_catalogue[items][3] == "userHired":
            in_items[items] = -2
    print("")
    return item_catalogue, in_items #Then returning item_catalogue and in_items to be used by other functions

'''
display header message
display items that have been hired

while input is not in the list
    if the input is in list
        change values back to unhired
    else if the input is not in the list
        display error message

return values
'''
def return_item(item_catalogue, in_items):

    print("Items you have hired: (Please enter the name of the item to be returned).")
    #for loop to create padding for display
    for items in item_catalogue:
        item = 12 - len(items[0])
        detail = 25 - len(items[1])
        pad = " "

        #if the index is userHired then display the item to be returned
        if items[3] == "userHired":
            print(items[4], "-", items[0], (item*pad), "(" + items[1] + ")", (detail*pad), "= ", "$" + '{0:.2f}'.format(float(items[2])))

    user_input = -5 #forced looping error

    #While the input is not in in_items or is -1, loop. if the user is to enter -1 display an error.
    #Else if the index of in_items user input has selected is equal to -2 then replace item_catalogue index of index from userHired to in
    #in_items index will be replaced from -2 to the orginal item listing number, which is detemined by the input, display that the items is returned
    #then return item_catalogue and in_items
    while user_input not in in_items or user_input == -1:
        try:
            user_input = int(input("Item: "))
            if user_input == -1:
                print("Item not hired.")
            elif in_items[user_input] == -2:
                item_catalogue[user_input][3] = "in"
                in_items[user_input] = user_input
                print(item_catalogue[user_input][0], "has been returned.")
        except ValueError:
            print("Please enter a number, not a letter.")
    print("")
    return item_catalogue, in_items

'''
display header message

create added item list

get user input of item name
append to added item
get user input for description of item
append to added item
get user input for price
if the input isn't an integer
    display error
else if the input is an integer
    append to added item list

append availability to the list
append number count to the list

append list to item catalogue

return values
'''
def add_item(item_catalogue, in_items):

    print("Please enter the name, details of the item, and the price.")
    added_item = [] #create a list to format the added item
    num_count = 0 #count to list the item number after the item is added

    #three inputs: name, detail and price, as each input is entered the item will be appended to the next index, then default in is appended
    name_add = str(input("Name of item: ")).title()
    added_item.append(name_add)
    detail_add = str(input("Detail of item: ")).title()
    added_item.append(detail_add)

    #while price isn't an integer loop
    price_add = "str"
    while price_add == "str":
        try:
            price_add = float(input("Enter price (with 2 decimal places): "))
        except ValueError:
            print("Please enter a number.")

    added_item.append(price_add)
    added_item.append("in")

    #a for loop to count how many items are in the item_catalogue, counts 1 for each item
    for items in item_catalogue:
        num_count += 1

    #appends number to added_item, appends added_item to item_catalogue and then adds the number to in_items
    added_item.append(num_count)
    item_catalogue.append(added_item)
    in_items.append(num_count)

    #dsplays the item that has been added
    print(added_item[0], "has been added to the catalogue.")
    print("")

    #Returns item_catalogue, in_items
    return item_catalogue, in_items

'''
close the old file
reopen the file is write mode

cycle through the items imported
    if the item is under userHired
        change the value to out
    write each item to the csv, replacing all data
'''

def write_to_csv(item_catalogue):

    item_data = open("items.csv", "w", newline='') #reopens the csv in write mode, as each line ends a new line is written
    item_csv = csv.writer(item_data) #using the csv writer built-in function

    #loops through the final list, and if any of those items have been hired, the value will be changed to out.
    #write the index[0:4] name, detail, price, availablity to the file, replacing all previous data
    for items in item_catalogue:
        if items[3] == "userHired":
            items[3] = "out"
        item_csv.writerow(items[0:4])

    print("Data successfully exported/saved to file 'items.csv'")

    #closes the file completely.
    item_data.close()

if __name__ == '__main__':
    main()