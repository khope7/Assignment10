#Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

#Problem Statement: Develop a program that:

#Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#Implement functions to:
#Open a new service ticket.
#Update the status of an existing ticket.
#Display all tickets or filter by status.
#Initialize with some sample tickets and include functionality for additional ticket entry.
#Example ticket structure:

#service_tickets = {
#    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
#    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
#}


#Writing code for CustomerServiceDataHandlingTask1

#Instatiating service tickets dictionary sample tickets
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


#Implementing function to open a new service ticket that takes user input for customer and issue and sets default status of new ticket to open then prints confirmation
def add_ticket(cust_tickets, ticket, customer, issue,):
    if ticket not in cust_tickets:
        cust_tickets[ticket] = {"Customer": customer, "Issue": issue, "Status": "open"}
        print(f"Ticket '{ticket}' added.")

#Implementing function to update the status of an existing ticket
def update_status(cust_tickets, ticket):
#After checking ticket, checks status value and replaces string from closed to open or open to closed toggling ticket upon user entry and prints confirmation
    if ticket in cust_tickets:
        if cust_tickets[ticket]["Status"] == "closed":
            cust_tickets[ticket]["Status"] = "open"
        elif cust_tickets[ticket]["Status"] == "open":
            cust_tickets[ticket]["Status"] = "closed"
        print(f"{ticket} has been adjusted.")

#Implementing function to display all tickets
def display_tickets():
#using items function to convert nested dictionary to string and reprinting for each available iteration using for in loop
    for cust_tickets, ticket in service_tickets.items():
        print(f"{cust_tickets}"+ " " + f"{ticket}")
    
#Implementing function to filter tickets by status
def filter_status():
#Instantiating ticket number count and ticket name for both open and closed tickets
    o = 0
    c = 0
    o_number = ""
    c_number = ""

#Created seperate while loops for print priority that check full dictionary for all open and then closed status requests and breaks once all open and then closed requests have been found
    while True:
#Created try except KeyError to account for ticket number count beyond ticket entries allowing loop to break and move on to closed tickets
        try:
            o += 1
            o_number = "Ticket00" + f"{o}"
            if service_tickets[o_number]["Status"] == "open":
                print("first order" + f"{service_tickets[o_number]}")
        except KeyError:
            break
#After this while loop breaks filter status function completes
    while True:
        try:
            c += 1
            c_number = "Ticket00" + f"{c}"
            if service_tickets[c_number]["Status"] == "closed":
                print("second order" + f"{service_tickets[c_number]}")
        except KeyError:
            break

#Implementing function to exit run
def exiting():
        print("Exiting, thank you for using: Customer Service Data Handling Menu")
        exit()



#Instantiating ticket number count to start at 2 to account for sample tickets
n = 2

#Instantiating while loop that asks the user to enter an option from 1-5 that stops only if option 5 is entered
while True:
    print("\nCustomer Service Data Handling Menu")
    print("1: Add Service Ticket\n2: Update Service Ticket Status\n3: Display Tickets\n4: Filter by Status\n5: Quit")
    choice = input("Please enter your choice: ")

#Instantiating option 1 that creates additional ticket number, asks the user for customer and issue variables and creates new ticket dictionary with default status of open as defined in add_ticket function
    if choice == '1':
        n += 1
        tnumber = "Ticket00" + f"{n}"
        cust = input("Please enter the customer name: ")
        issue = input("Please enter the customer issue: ")
        add_ticket(service_tickets, tnumber, cust, issue)

#Instantiating option 2 that adjusts the status of all existing tickets, asks the user for the ticket number to change and if that ticket number exists, runs update status function to toggle open and closed status
    elif choice == '2':
        update_number = input("Please choose the ticket you would like to change the status of: ")
        ticket_number = "Ticket00" + update_number
        if ticket_number in service_tickets:
            update_status(service_tickets, ticket_number)

#Created elif to catch for other correct entry of full ticket number name
        elif update_number.title() in service_tickets:
            update_status(service_tickets, update_number.title())

#Created else statement to catch for all alternative entries
        else:
            print("Ticket number must been in Service Tickets")

#Instantiating option 3 that runs display_tickets function
    elif choice == '3':
        display_tickets()

 #Instantiating option 4 that runs filter_status function       
    elif choice == '4':
        filter_status()

 #Instantiating option 5 that runs exiting function   
    elif choice == '5':
        exiting()
#Created else statement to catch for all other entries
    else:
        print("Please choose a choice between 1 and 4")