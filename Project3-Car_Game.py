cmd = ''
started = False
while True:
    cmd = input('> ')
    if cmd.lower() == 'help':
        print(''' start - to start the car\n stop - to stop the car\n quit - to exit ''')
    elif cmd.lower() == 'start':
        if started:
            print("The car is already on the run!")
        else:
            started = True
            print("Car starts....Let's Go!")
    elif cmd.lower() == 'stop':
        if not started:
            print("Car is not running")
        else:
            print("Car Stops")
            started = False
        inter_state = 0
    elif cmd.lower() == 'quit':
        print("Game Over!")
        break;
    else:
        print("Sorry, I don't understand that...try 'help'")
