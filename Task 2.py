def guest_greeting():
    print "Welcome Guest"


choice = 0

while choice != -1:
    print "Hello..."
    print "1. Returning Customer"
    print "2. New Customer"
    print "3. Guest"

    choice = raw_input("Please enter a number: ")

    if choice == '1':
        print"Returning Customer"
        choice = -1
    elif choice == '2':
        print "New Customer"
        choice = -1
    elif choice == '3':
        guest_greeting()
        choice = -1
    else:
        print "ERROR: Not Valid"
