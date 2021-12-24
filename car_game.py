command = ""
started = False
while True:
    # this is first github push
    # input asks to enter keywords
    command = input("> ").lower()
    # if and else logical conditions
    # I'm adding another line for TEST
    if command == 'start':
        if started:
            print('Hey car already started....!')
        else:
            started = True
            print('Car Started.....!')
    elif command == 'stop':
        if not started:
            print('car not started...!')
        else:
            started = False
            print('Car Stopped.....!')
    elif command == 'help':
        print("""
Start - To start the Car
Stop - To stop the car
quit - To Quit
        """)
    elif command == "quit":
        print('Quitted...! Thank you')
        break
    else:
        print("""
Sorry, I don't Understand....!
Enter HELP
        """)
